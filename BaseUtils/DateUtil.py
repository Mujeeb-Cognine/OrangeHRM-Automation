import calendar
import datetime
import locale
import math
import random
import time
import pytz
from dateutil.relativedelta import relativedelta
from dateutil import rrule
from unidecode import unidecode
from BaseUtils.Utils import Utils
from OrangeHRMData.DateTimeFormats import DateTimeFormats
from OrangeHRMData.Strings import Strings

s = Strings()


def determine_date_diff():
    server_date = datetime.datetime.now(pytz.timezone(s.time_zone.utc))
    member_date = datetime.datetime.now(pytz.timezone(s.time_zone.us_eastern))

    if server_date.year == member_date.year:
        return server_date.timetuple().tm_yday > member_date.timetuple().tm_yday
    elif server_date.year > member_date.year:
        return True
    else:
        return False


def get_today_with_days_added(days_added=0, time_zone=s.time_zone.us_eastern,
                              format_func=s.dtf.days_added_default_format, date_diff_check=True):

    if determine_date_diff() and date_diff_check:
        time_zone = s.time_zone.utc

    if format_func is None:
        return (datetime.datetime.now(pytz.timezone(time_zone)) +
                datetime.timedelta(days=days_added)).replace(hour=0, minute=0, second=0, microsecond=0)
    else:
        return format_func(datetime.datetime.now(pytz.timezone(time_zone)) + datetime.timedelta(days=days_added))


def get_date_with_days_added_for_dependency(format=DateTimeFormats().datetime_base, days_added=0, date=None):
    """
    For work plan ticket dependency date calculations there are specific rules
    that's why we need these weekday calculation, because if date is on weekend we cannot
    set Start Date for the ticket

    :param days_added: amount of days to be added
    :param date - date to which days will be added
    :return: date with added days
    """
    mui_date_format = DateTimeFormats().short
    input_datetime_obj = datetime.datetime.strptime(str(date), format)

    # Numbers equals day count (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    if input_datetime_obj.weekday() >= 5:
        input_datetime_obj = get_next_monday(input_datetime_obj)
    if input_datetime_obj.weekday() == 4:
        input_datetime_obj = get_next_monday(input_datetime_obj)
        days_added = days_added - 1

    converted_datetime_str = input_datetime_obj.strftime(mui_date_format)
    final_date_obj = (datetime.datetime.strptime(converted_datetime_str, mui_date_format) +
                      datetime.timedelta(days=days_added)).replace(hour=13, minute=0, second=0, microsecond=0)
    if final_date_obj.weekday() >= 5:
        final_date_obj = get_next_monday(final_date_obj)

    return final_date_obj


def get_next_monday_plus_days(days_added=0):
    """
    :param days_added: amount of days to add to the next monday date
    :return: next monday plus days_added
    """
    current_date = datetime.datetime.now()
    formatted_next_monday = get_next_monday(current_date).strftime(DateTimeFormats().datetime_base)

    return (datetime.datetime.strptime(formatted_next_monday, DateTimeFormats().datetime_base) +
            datetime.timedelta(days=days_added)).replace(hour=13, minute=0, second=0, microsecond=0)


def get_next_monday(date):
    # Calculate the number of days until the next Monday (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    days_until_next_monday = (7 - date.weekday()) % 7
    return date + datetime.timedelta(days=days_until_next_monday)


def get_today_with_months_added(months_added=0, dt=False, day_offset=None, initial_date=None, handle_leap_year=False,
                                format_func=s.dtf.days_added_default_format):
    """
    :param months_added:
    :param initial_date:
    :param format_func: function to execute on datetime object
    :param dt:
    :param day_offset: assumes your day_offset is less than 30 when using negative values.
    :param handle_leap_year: If the day we calculate falls of Feb 29 then we will set the date to Feb 28
    :return:
    """
    if initial_date is None:
        initial_date = datetime.datetime.now()

    month = initial_date.month - 1 + months_added
    year = initial_date.year + int(math.floor(month / 12))
    month = month % 12 + 1
    if day_offset is not None:
        if initial_date.day == 1 and day_offset < 0:
            day = get_last_day_of_month(month=month, year=year, format_func=None).day + \
                  (day_offset + 1)
            """
            Unclear why initial_date.month and initial_date.year was used instead of the month and year value set above. 
            Removed for now because day_offset was returning a value in the current month when months were removed
            instead of a date a few months back. Did not seem to break existing scripts with day_offset.
            """
            # month = initial_date.month
            # year = initial_date.year
        else:
            day = min(initial_date.day + day_offset, calendar.monthrange(year, month)[1])
    else:
        day = min(initial_date.day, calendar.monthrange(year, month)[1])

    if handle_leap_year:
        if month == 2 and day == 29:
            # Make 29 into 28
            day -= 1
    if format_func is None:
        if dt is True:
            return datetime.datetime(year, month, day, 0, 0, 0)
        else:
            return datetime.date(year, month, day)
    else:
        return format_func(datetime.date(year, month, day))


def get_date_with_weekday_time_utc(days_added=0, time_zone=s.time_zone.us_eastern,
                                   format_func=s.dtf.report_time_stamp_long, hours=0, minute=0):

    # Example default output: Wednesday 02/20/2019 12:00 AM UTC-05
    return format_func(datetime.datetime.now(pytz.timezone(time_zone)).replace(hour=hours, minute=minute) +
                       datetime.timedelta(days=days_added))


def get_nth_weekday_of_month(nth, weekday, month, year, format_func=s.dtf.days_added_default_format):
    """
    You can use this method to get the date of the nth weekday of a month.
    Example: Get the third Friday of August 2018
             | >>> get_nth_weekday_of_month(3, 4, 8, 2018)
             | '08/17/2018'
    :param nth:
        First = 1
        Second = 2
        Third = 3
        Forth = 4
        Fifth = 5 (there's not always a 5th, will return None)
        Last = -1
    :param weekday:
        Monday...Sunday = 0...6
    :param month:
        Jan...Dec = 1...12
    :param year:
        Year = YYYY
    :param format_func: function to execute on datetime object
    :return: formatted string, date object or None
    """
    if nth > 0:
        nth -= 1     # adjust to make the nth parameter when calling the function a bit more Pythonic
    first_weekday_of_month, days = calendar.monthrange(year, month)
    first = (weekday - first_weekday_of_month) % 7 + 1
    try:
        day = range(first, days+1, 7)[nth]
        if format_func is not None:
            return format_func(datetime.date(year, month, day))
        else:
            return datetime.datetime(year, month, day)
    except (IndexError, ValueError):
        return None


def get_time_object(time_string=None):
    """
    :type time_string: str
    :parameter time_string: Takes in a time to convert as a standardized string.
                            Must be in format "%I:%M%p" - ie "10:00AM"
    :return: returns time tuple
    """
    if time_string is None:
        return_value = datetime.datetime.now()
    else:
        return_value = datetime.datetime.strptime(time_string, "%H:%M")

    return return_value


def get_time_string(time_string=None, format_func=s.dtf.time_short):
    """
    :type time_string: str
    :param time_string: Takes in a time to convert as a standardized string.
                            Must be in format "%I:%M%p" - ie "10:00AM"
    :type format_func: function to execute on datetime object
    :type keep_leading_zeros: bool
    :return: returns a string that is formated to the global time format
    """
    return_value = get_time_object(time_string=time_string)

    if format_func is None:
        return return_value
    else:
        return format_func(return_value)


def get_datetime_string():
    return datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S")


def get_date_serial(suffix_length=4):
    suffix = Utils().unique_string(suffix_length)
    serial = datetime.datetime.now().strftime('%d%H%M%S')
    return serial + suffix


def get_day_serial():
    return datetime.datetime.now().strftime("%m%d%y")


def get_short_serial():
    return datetime.datetime.now().strftime("%H%M%S")


def get_datetime_string_with_utc(t_datetime, replace_tz=True, include_day=False, format_func_1=None,
                                 format_func_2=None, return_datetime=False):
    """
    format_func_1: override dtf for day format
    format_func_2: override dtf for time format

    return_datetime: Allows for just the datetime object to be returned. Default behavior is for a formatted string
                    to be returned
    """
    # Handle overrides
    if format_func_1 is not None:
        day_dtf = format_func_1
    else:
        day_dtf = s.dtf.short_input

    if format_func_2 is not None:
        time_dtf = format_func_2
    else:
        time_dtf = s.dtf.history_timestamp_time

    if isinstance(t_datetime, str):
        t_datetime = s.dtp.short_time(t_datetime)
    if t_datetime is None:
        t_datetime = datetime.datetime.now(pytz.timezone(s.time_zone.us_eastern))

    if replace_tz:
        t_datetime = t_datetime.replace(tzinfo=pytz.timezone(s.time_zone.us_eastern))
    if include_day:
        output = '{0} {1} {2} UTC{3}'.format(s.dtf.day_short(t_datetime), day_dtf(t_datetime),
                                             time_dtf(t_datetime),
                                             t_datetime.strftime('%z')[:-2])
    else:
        output = '{0} {1} UTC{2}'.format(day_dtf(t_datetime),
                                         time_dtf(t_datetime),
                                         t_datetime.strftime('%z')[:-2])
    if return_datetime:
        return t_datetime
    else:
        return output


def get_unique_dollar_amount():
    return float('{0}.{1}'.format(str(random.randint(1, 500)), str(random.randint(10, 99))))


def get_current_date_range(week_offset=0, form="long", dt=False, format_func=s.dtf.current_date_range, day_offset=0,
                           zero_times=False):
    """
    Returns a date range string in the format used on the Time Sheet view.
    :param week_offset: Default = 0 -  Takes an int value. Will cause the function to return a date range for the
                                current week plus the number of weeks passed in.
                                The function accepts a negative week_offset to get a previous week.
    :param form: Default = "long" - Takes "short" as an option. This changes the format of the string that is returned.
                                long example =  01/01/2014 - 01/07/2014
                                short example = 01/01/2014-01/07/2014
    :param dt: bool, return a datetime or a string
    :param format_func: return string format
    :param day_offset:
    :param zero_times:
    """
    # returns current day as int 0 = Monday
    offset_days = week_offset * 7
    current_day = datetime.datetime.today().weekday() + day_offset

    if current_day == 5:
        week_start_date = datetime.datetime.today() + datetime.timedelta(days=offset_days)
    elif current_day == 6:
        week_start_date = datetime.datetime.today() + datetime.timedelta(days=-1 + offset_days)
    else:
        week_start_date = datetime.datetime.today() + datetime.timedelta(days=-current_day + -2 + offset_days)

    week_end_date = week_start_date + datetime.timedelta(days=6)

    week_start_date = week_start_date.replace(hour=0, minute=0, second=0) if zero_times else week_start_date
    week_end_date = week_end_date.replace(hour=0, minute=0, second=0) if zero_times else week_end_date
    if dt is True:
        return week_start_date, week_end_date.replace(hour=0, minute=0, second=0)
    if form == "long":
        return format_func(week_start_date) + " - " + format_func(week_end_date)
    elif form == "short":
        return format_func(week_start_date) + "-" + format_func(week_end_date)
    else:
        return None


def get_last_day_of_month(month=datetime.datetime.today().month, year=datetime.datetime.today().year,
                          return_day_int=False, format_func=s.dtf.days_added_default_format, dt=None,
                          handle_leap_year=False):
    if dt is not None:
        month = dt.month
        year = dt.year

    month_range = calendar.monthrange(year, month)
    day = month_range[1]

    if handle_leap_year:
        if month == 2 and month_range[1] == 29:
            # Make 29 into 28
            day -= 1

    if return_day_int:
        return day
    elif format_func is None:
        return datetime.datetime(year, month, day)
    else:
        return format_func(datetime.date(year, month, day))


def get_last_day_of_next_month(format_func=s.dtf.short_input):
    this_month = datetime.datetime.today().month
    if this_month == 12:
        next_month = 1
        year = datetime.datetime.today().year + 1
    else:
        next_month = this_month + 1
        year = datetime.datetime.today().year

    return format_func(datetime.date(year, next_month,
                                     get_last_day_of_month(next_month, year, return_day_int=True)))


def get_first_day_of_month(month=datetime.datetime.today().month, format_func=None,
                           year=datetime.datetime.today().year, dt=None):
    if dt is not None:
        month = dt.month
        year = dt.year

    if format_func is None:
        return datetime.datetime(year, month, 1)
    else:
        return format_func(datetime.date(year, month, 1))


def get_date_range_for_date(date=datetime.datetime.today(), start_weekday=5,
                            format_func=s.dtf.weekday_separator_short, dt=False):
    # Pass in a date, and it will return the range from the start of week through 6 days later
    # example: ("Sat, Mar 7 - Fri, Mar 14"), 5 = Saturday
    start = get_day_of_week_from_date(date=date, format_func=format_func, start_weekday=start_weekday)
    end = start
    end += datetime.timedelta(days=6)

    if dt:
        return [start, end]
    else:
        return '{0} - {1}'.format(format_func(start), format_func(end))


def get_date_range_for_date_no_leading_zero(date=datetime.datetime.today(), start_weekday=5,
                                            format_func=s.dtf.weekday_separator_short):
    # Pass in a date, and it will return the range from the start of week through 6 days later
    # example: ("Sat, Mar 7 - Fri, Mar 14"), 5 = Saturday
    start = get_day_of_week_from_date(date=date, format_func=format_func, start_weekday=start_weekday)
    end = start
    end += datetime.timedelta(days=6)

    return '{0} - {1}'.format(format_func(start).replace(' 0', ' '),
                              format_func(end).replace(' 0', ' '))


def get_day_of_week_from_date(date=datetime.datetime.today(), start_weekday=5,
                              format_func=s.dtf.weekday_separator_short, return_string=False):
    # 0 = Monday
    # 1 = Tuesday ...
    # 6 = Sunday

    # Pass in a date and it will go back to find the previous day, so if it's monday
    # and you need to get the last tuesday you can pass 1 in your day_of_week to get that date
    days = 0
    start = date
    while start.weekday() != start_weekday:
        days -= 1
        start = date + datetime.timedelta(days=days)

    if return_string:
        return format_func(start)
    else:
        return start


def weekday_name_to_isoweekday(weekday):
    """
    Want to avoid any weekday names with variable casing and with a period. Strip these out.

    Using Unidecode to avoid special characters
    """
    clean_weekday = weekday.replace('.', '')

    # Getting list of possible values
    week_short = [unidecode(_.lower().replace('.', '')) for _ in list(calendar.day_abbr)]
    week_full = [unidecode(_.lower().replace('.', '')) for _ in list(calendar.day_name)]

    # Determine index based on lists from above
    l_cleaned = unidecode(clean_weekday.lower())
    if l_cleaned in week_short:
        return week_short.index(l_cleaned) + 1
    else:
        return week_full.index(l_cleaned) + 1


def get_date_by_weekday(weekday=None, format_func=s.dtf.short_input):
    """
    Returns date for the given day of the week, within current date range
    :param weekday: Day of the week
    :param format_func: function to execute on datetime object
    :return: the date for the given day of the week within current range
    """
    if weekday is None:
        weekday = list(calendar.day_abbr)[0]

    today = get_today_with_days_added(format_func=None)
    return get_today_with_days_added(weekday_name_to_isoweekday(weekday) - today.isoweekday(), format_func=format_func)


def get_first_day_of_next_week(days_added=1, format_func=s.dtf.days_added_default_format):
    # first day of week is Saturday
    days_offset = 2
    today_num = datetime.datetime.today().isoweekday()
    return get_today_with_days_added(((14 - today_num - days_offset) % 7) + days_added, format_func=format_func)


def get_last_day_of_current_week(format_func=s.dtf.short_input):
    return get_first_day_of_next_week(days_added=0, format_func=format_func)


def get_year(date_string=None, date_format=s.dt.standard, year_length='%Y'):
    """
    get_year takes a string in the format "Day MM/DD/YYYY", same formant as calendar date field
    get_year parses the string and return a string of the year.
    :param date_string: str or None
    :param date_format: str
    :param year_length: str
    :return:
    """

    # If no date is passed in, use current
    if date_string is None:
        return_date = datetime.datetime.now()
    else:
        return_date = datetime.datetime.strptime(date_string, date_format)

    return return_date.strftime(year_length)


def get_quarter_of_year(date_object=None):
    """
    get_quarter_of_year takes a string in the format "Day MM/DD/YYY" by default
    get_quarter_of_year parses the string and returns a string of the quarter of the year
    quarter is 1, 2, 3 or 4
    get_quarter_of_year with no paramter gets the current quarter of the year
    :param date_object:
    """

    if date_object is None:
        month = float(datetime.datetime.today().month)
    else:
        month = float(date_object.month)

    quarter = int(math.ceil(month/3))
    # return the quarter as a string
    return str(quarter)


def get_first_day_of_next_quarter(format_func=s.dtf.short_input):
    current_quarter = int(get_quarter_of_year())

    if current_quarter == 4:
        next_quarter = 1
        year = int(get_year()) + 1
    else:
        next_quarter = current_quarter + 1
        year = int(get_year())
    next_quarter_month = (next_quarter * 3) - 2

    if format_func is not None:
        return format_func(datetime.date(year, next_quarter_month, 1))
    else:
        return datetime.datetime(year, next_quarter_month, 1)


def get_first_day_of_the_quarter(format_func=s.dtf.short_input,
                                 quarter=get_quarter_of_year()):
    quarter = int(quarter)
    year = int(get_year())

    month = (quarter * 3) - 2

    if format_func is not None:
        return format_func(datetime.date(year, month, 1))
    else:
        return datetime.datetime(year, month, 1)


def get_last_day_of_quarter(quarter=int(get_quarter_of_year()), format_func=s.dtf.short_input):

    quarter_end_month = quarter*3
    return format_func(datetime.date(datetime.date.today().year, quarter_end_month, int(get_last_day_of_month(
        quarter_end_month, return_day_int=True))))


def get_last_day_of_next_quarter():
    next_quarter_first_string = get_first_day_of_next_quarter()
    next_quarter_first_datetime = datetime.datetime.strptime(next_quarter_first_string, s.dt.short)

    last_day = get_last_day_of_month(next_quarter_first_datetime.month, next_quarter_first_datetime.year)

    return s.dtf.short_input(datetime.date(int(next_quarter_first_datetime.year),
                                           int(next_quarter_first_datetime.month),
                                           int(last_day)))


def combine_date_and_time(t_datetime=None, t_time=None, t_zone=None):
    # If no datetime is specified, use the current datetime of US Eastern
    if t_datetime is None:
        t_datetime = datetime.datetime.now(pytz.timezone(s.time_zone.us_eastern) if t_zone is None else t_zone)

    if t_time is not None:
        if isinstance(t_time, str):
            t_time = get_time_object(t_time)
        if isinstance(t_time, datetime.datetime):
            t_time = t_time.time()
        t_datetime = datetime.datetime.combine(t_datetime, t_time)
        if t_zone is not None:
            tz = t_zone
        else:
            tz = pytz.timezone(s.time_zone.us_eastern)
        t_datetime = tz.localize(t_datetime)
    return t_datetime


def get_raw_timestamp(t_datetime=None, t_time=None, time_zone=None, react=False, locale_au=False, leading_zero=True,
                      date_diff_check=True):
    """
    Will return a string of the datetime stamp used in many features of the application, such as Notes timestamp
    Example output: Wed 03/04/2015 5:46 PM UTC-05
    non React AU Format:
    These standards are per BA in Ticket #5931353
    """

    diff_date = determine_date_diff() if date_diff_check else False

    this_datetime = combine_date_and_time(t_datetime=t_datetime, t_time=t_time, t_zone=time_zone)

    # Non-React format
    if not react and not locale_au:
        output = '{0} {1} UTC{2}'.format(s.dtf.history_timestamp_date(this_datetime, date_diff_check=diff_date),
                                         s.dtf.history_timestamp_time(this_datetime),
                                         this_datetime.strftime('%z')[:-2])
    # Non-React AU format
    elif locale_au and not react:
        output = '{0} {1} UTC{2}'.format(s.dtf.history_timestamp_date_alt(this_datetime, date_diff_check=diff_date),
                                         s.dtf.history_timestamp_time(this_datetime, leading_zero),
                                         this_datetime.strftime('%z')[:-2])
    # React AU format: Tue, 19/01/2021, 1:19 pm GMT
    elif locale_au and react:
        output = '{0}, {1} {2}'.format(s.dtf.history_timestamp_date_alt(this_datetime, date_diff_check=diff_date,
                                                                        react=True),
                                       s.dtf.history_timestamp_time_12_hour(this_datetime, leading_zero),
                                       this_datetime.tzinfo._tzname)
    # React format
    else:
        output = '{0}, {1} {2}'.format(s.dtf.react_input_date(dt=this_datetime, date_diff_check=diff_date),
                                       s.dtf.history_timestamp_time(this_datetime),
                                       this_datetime.tzinfo._tzname)
    return output


def get_calendar_month_range(first_format=s.dtf.b_d, last_format=s.dtf.b_d_Y):
    # Set locale properly due to random reset issues
    if not locale.getlocale()[0].startswith('en_'):
        locale.setlocale(locale.LC_ALL, locale.getlocale()[0])

    # Returns the month matching the calendar format
    first = get_first_day_of_month(format_func=first_format)
    last = get_last_day_of_month(format_func=last_format)
    return first + " - " + last


def number_of_days(age_string):
    """
    Used to convert 'Age: (# days)d (# hours)h (# minutes)m' to float(# days)
    Example Usage: Age of Service Ticket on Service Ticket Page
    :param age_string:
    :return:
    """
    time_components = age_string.split()
    ticket_age = 0
    for this_time in time_components:
        if this_time[-1] == 'd':
            ticket_age += float(this_time[:-1:])
        elif this_time[-1] == 'h':
            ticket_age += float(this_time[:-1:]) / 24.0
        elif this_time[-1] == 'm':
            ticket_age += float(this_time[:-1:]) / 1440.0
    return round(ticket_age, 1)


def get_timezone():
    return time.strftime("%z", time.gmtime())


def get_military_time_in_range(start_time='0:00 AM', end_time='12:00 PM', increment=15):
    """
    taking in time_string start and stop, will return a list of all the time values as strings
    that are separated by increment value
    """

    times = [start_time, end_time]
    nums = [0, 0]

    # convert the time_strings into ints to work with
    for i in range(2):
        temp = times[i].split(':')
        try:
            temp_min, temp_am_pm = temp[1].split(' ')
            nums[i] = int(str(int(temp[0]) + 12) + temp_min) if temp_am_pm == 'PM' else int(str(temp[0] + temp_min))
        except:
            nums[i] = int(str(temp[0] + temp[1]))

    time_list = []
    temp_time = nums[0]

    while temp_time in range(nums[0], nums[1]):
        time_list.append("{:04}".format(temp_time))
        temp_time += increment
        if "{:04}".format(temp_time)[-2:] >= '60':
            temp_time += 40
    return time_list


def convert_utc(date_time, time_zone=s.time_zone.us_eastern, format_func=s.dtf.short_input):
    # if you are not passing in a datetime for date_time you need to make sure the string format is...
    # %Y-%m-%dT%H:%M:%SZ (full_utc)

    old_time = date_time
    if isinstance(date_time, str):
        old_time = datetime.datetime.strptime(date_time, s.dt.api)

    expected_time = old_time.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(time_zone))
    return format_func(expected_time) if format_func else expected_time


def convert_long_to_short_date(date_string):
    """
    :param date_string: example: 'Friday, May 6, 2016 11:44:31.400 AM'
    :return: example: '5/6/2016'
    Used in avalara transactions logging test
    """
    month_dict = {"January": "1",
                  "February": "2",
                  "March": "3",
                  "April": "4",
                  "May": "5",
                  "June": "6",
                  "July": "7",
                  "August": "8",
                  "September": "9",
                  "October": "10",
                  "November": "11",
                  "December": "12"}
    str_list = date_string.split(" ")
    month = str_list[1]
    month_num = month_dict[month]
    day = str_list[2][:-1]
    year = str_list[3]
    new_date = month_num + '/' + day + '/' + year
    return new_date


def wait_until_the_right_time(min_sec=0, max_sec=10):
    while not (min_sec <= datetime.datetime.now().second <= max_sec):
        time.sleep(.5)


def get_one_year_date_range_by_month(month=datetime.datetime.today().month, format_func=None,
                                     year=datetime.datetime.today().year):
    """
    Ie. Pass in 8, 2012 and it can return [Aug 11, Sep 11, ..., Aug 12]
    """
    if format_func is None:
        return [datetime.datetime(year, month, 1) + relativedelta(months=i) for i in range(-12, 1)]
    else:
        return [format_func(datetime.datetime(year, month, 1) + relativedelta(months=i)) for i in range(-12, 1)]


def get_days_between_dates(begin_date, end_date, format_te=True, format_func=s.dt.time_range):
    """
    Returns a list with the days between two dates
    :param begin_date: datetime
    :param end_date: datetime
    :param format_te: boolean
    :param format_func: str
    :return: list
    """

    list_of_days = []

    def daterange(date1, date2):
        for n in range(int((date2 - date1).days) + 1):
            yield date1 + datetime.timedelta(n)

    for dt in daterange(begin_date, end_date):
        if format_te:
            list_of_days.append(dt.strftime(format_func))
        else:
            list_of_days.append(dt)

    return list_of_days


def get_amount_of_business_days(date1, date2):
    """
    Calculates the amount of working days (Mon-Fri) between 2 dates
    :param date1: date obj - start date
    :param date2: date obj - end date
    :return: int
    """

    weekdays = rrule.rrule(rrule.DAILY, byweekday=range(0, 5), dtstart=date1, until=date2)
    return len(list(weekdays))


def get_business_date_with_days_added(date1, days_added):
    """
    Get a date object of business days with an amount of days added
    :param date1: date obj - start date
    :param days_added: int - days to add
    :return: date
    """
    days_to_add = days_added
    current_date = date1.replace(tzinfo=None)

    while days_to_add > 0:
        current_date += datetime.timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5:
            continue
        days_to_add -= 1

    while days_to_add < 0:
        current_date += datetime.timedelta(days=-1)
        weekday = current_date.weekday()
        if weekday >= 5:
            continue
        days_to_add += 1

    return current_date


def get_month_abbreviations():
    month_abbrs = list()
    for i in range(1, 13):
        dt = datetime.datetime.now().replace(month=i, day=i)
        month_abbrs.append(s.dtf.month_abr(dt))

    return month_abbrs


def get_day_abbreviations():
    day_abbrs = list()
    for i in range(1, 8):
        dt = datetime.datetime.now().replace(month=1, day=i, year=2018)
        day_abbrs.append(unidecode(s.dtf.day_abr(dt)).replace('.', ''))

    return day_abbrs


class Stopwatch(object):

    _start_time = None
    _end_time = None

    def __init__(self):
        self._start_time = datetime.datetime.now()

    def start(self):
        self._start_time = datetime.datetime.now()

    def stop(self):
        self._end_time = datetime.datetime.now() - self._start_time
        return self.get_end_time_as_string()

    def get_start_time(self):
        return self._start_time

    def get_end_time(self):
        return self._end_time

    def get_end_time_as_string(self):
        return '%d.%d' % (self._end_time.seconds, self._end_time.microseconds)
