import pytz

from datetime import datetime
from OrangeHRMData.GlobalData import TimeZones
from OrangeHRMData._BaseLocalizationClass import _BaseLocalizationClass


class DateTimeFormatter(_BaseLocalizationClass):

    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    @staticmethod
    def report_screenshot_datetime(dt):
        return dt.strftime("%Y_%m_%d_%H_%M")

    @staticmethod
    def localize_date(_dt, date_diff_check):
        if date_diff_check:
            return _dt.replace(tzinfo=pytz.timezone(TimeZones.utc)).astimezone(
                pytz.timezone(TimeZones.us_eastern))
        else:
            return _dt

    @staticmethod
    def get_formatted_weekday(dt):
        """
        WARNING: DO NOT USE THIS OUTSIDE OF THIS FILE. day_short SHOULD BE USED INSTEAD

        :type dt: datetime.datetime
        """
        return DateTimeFormatter.weekdays[dt.weekday()]

    @staticmethod
    def b_d(dt):
        return dt.strftime('%b %d')

    @staticmethod
    def d_b(dt):
        return dt.strftime('%d %B')

    @staticmethod
    def b_d_Y(dt):
        return dt.strftime('%b %d, %Y')

    @staticmethod
    def dispatch_monthly_header(dt):
        return dt.strftime('%b %Y')

    @staticmethod
    def b_y_full_month(dt):
        return dt.strftime('%B %Y')

    @staticmethod
    def dispatch_90_full_month(dt):
        return DateTimeFormatter.b_y_full_month(dt)

    @staticmethod
    def calendar_day_month_houronly(dt):
        return (dt.strftime('%I%p').lower()).lstrip("0")

    @staticmethod
    def calendar_header(dt):
        return dt.strftime('%B %d, %Y')

    @staticmethod
    def date_picker_flyout(dt):
        return '{dt:%b} {dt.day}, {dt.year}'.format(dt=dt)

    @staticmethod
    def date_time_standard_utc(dt):
        return '{short_lv} {time} {utc}'.format(short_lv=DateTimeFormatter.standard(dt),
                                                time=DateTimeFormatter.time_short(dt),
                                                utc=DateTimeFormatter.utc(dt))

    @staticmethod
    def date_time_utc(dt):
        return '{short_lv} {time} {utc}'.format(short_lv=DateTimeFormatter.short_listview(dt),
                                                time=DateTimeFormatter.time_short(dt),
                                                utc=DateTimeFormatter.utc(dt))

    @staticmethod
    def day_first():
        return False

    @staticmethod
    def day_full(dt):
        return dt.strftime('%A')

    @staticmethod
    def day_short(dt):
        return dt.strftime('%a')

    @staticmethod
    def day_name(dt):
        return dt.strftime('%A')

    @staticmethod
    def resource_time(dt):
        return dt.strftime('%I:%M%p').lstrip('0').lower()[:-1]

    @staticmethod
    def history_timestamp_date(dt, react=False, date_diff_check=True):
        """
        We need to handle the member date being before the server date
        """

        if react:
            return DateTimeFormatter.short(DateTimeFormatter.localize_date(dt, date_diff_check))
        else:
            return DateTimeFormatter.standard(DateTimeFormatter.localize_date(dt, date_diff_check))

    @staticmethod
    def history_timestamp_time(dt):
        return DateTimeFormatter.time_short(dt)

    @staticmethod
    def ios_date(dt):
        return dt.strftime('%m:%d:%y')

    @staticmethod
    def last_update(dt):
        return '{0} {1}'.format(DateTimeFormatter.standard(dt),
                                DateTimeFormatter.time_short(dt))

    @staticmethod
    def last_update_utc(dt):
        # No leading zeros on hours, month or day
        return '{standard_date} {time} {utc}'.format(standard_date=DateTimeFormatter.standard(dt),
                                                     time=DateTimeFormatter.time_short(dt),
                                                     utc=DateTimeFormatter.utc(dt))

    @staticmethod
    def last_update_date_time(dt):
        # No leading zeros on hours, month or day
        return '{short_date} {time} {utc}'.format(short_date=DateTimeFormatter.short(dt),
                                                  time=DateTimeFormatter.time_short(dt),
                                                  utc=DateTimeFormatter.utc(dt))

    @staticmethod
    def long(dt):
        return dt.strftime('%a, %b %d, %Y')

    @staticmethod
    def midnight():
        return '12:00 AM'

    @staticmethod
    def month_day(dt):
        return dt.strftime('%m/%d')

    @staticmethod
    def month_name(dt):
        return dt.strftime('%B')

    @staticmethod
    def month_abr(dt):
        return dt.strftime('%b')

    @staticmethod
    def day_abr(dt):
        return dt.strftime('%a')

    @staticmethod
    def react_input_date(dt, date_diff_check=False):
        _dt = DateTimeFormatter.localize_date(dt, date_diff_check)
        return _dt.strftime('%a, {dt.month}/{dt.day}/{dt.year}'.format(dt=dt))

    @staticmethod
    def rw_full_12(dt):
        return dt.strftime('%I %M %p %d %B %Y')

    @staticmethod
    def rw_short_date(dt):
        return dt.strftime('%#m/%#d/%Y')

    @staticmethod
    def qbo_short_date_time(dt):
        return dt.strftime('%m/%d/%Y %I:%M %p')  # '08/26/2019 12:00 AM'

    @staticmethod
    def rw_short_date_time(dt):
        return dt.strftime('%#m/%#d/%Y %#I:%M %p')  # '8/26/2019 12:00 AM'

    @staticmethod
    def workflow_short_date_time(dt):
        return dt.strftime('%#m/%#d/%Y %#I:%M:%S %p')  # 8/26/2019 12:00:00 AM

    @staticmethod
    def rw_time_short(dt):
        return dt.strftime('%I:%M %p').lstrip('0')

    @staticmethod
    def short(dt):
        return '{dt.month}/{dt.day}/{dt.year}'.format(dt=dt)  # 1/4/2022

    @staticmethod
    def short_date_time(dt):
        string = dt.strftime('%m/%d/%Y - %I:%M %p')
        return string.replace('/0', '/').replace(' 0', ' ').lstrip('0')

    @staticmethod
    def short_input(dt):
        return dt.strftime('%m/%d/%Y')  # 01/04/2022

    @staticmethod
    def short_year(dt):
        return dt.strftime('%m/%d/%y')

    @staticmethod
    def short_listview(dt):
        return dt.strftime('{dt.month}/{dt.day}/%y'.format(dt=dt))

    @staticmethod
    def sql(dt):
        return dt.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def standard(dt):
        return dt.strftime('%a %m/%d/%Y')

    @staticmethod
    def standard_with_zero_stripped(dt):
        """
        leading zero stripped
        e.g. Mon 8/7/2020
        """
        month = dt.strftime('%m').lstrip('0')
        date = dt.strftime('%d').lstrip('0')
        return dt.strftime('%a {}/{}/%Y').format(month, date)

    @staticmethod
    def standard_long(dt):
        return dt.strftime('%A %m/%d/%Y')

    @staticmethod
    def standard_short(dt):
        return dt.strftime('%a %m/%d')

    @staticmethod
    def standard_short_new(dt):
        return dt.strftime('%a %m/%d')

    @staticmethod
    def standard_listview(dt):
        return '{0} {1}'.format(DateTimeFormatter.day_short(dt), DateTimeFormatter.short_listview(dt))

    @staticmethod
    def standard_short_weekday(dt):
        return DateTimeFormatter.standard(dt)

    @staticmethod
    def time_12_only(dt):
        return dt.strftime('%I:%M').lstrip('0')

    @staticmethod
    def time_24(dt):
        return dt.strftime('%H:%M:%S')

    @staticmethod
    def time_h_m(dt):
        return dt.strftime('%I:%M %p')

    @staticmethod
    def time_short(dt):
        return dt.strftime('%I:%M %p').lstrip('0')  # 8:00 AM

    @staticmethod
    def report_time(dt):
        return dt.strftime('%I:%M %p').lstrip('0')  # 8:00 AM

    @staticmethod
    def tz_genymotion(dt):
        return dt.strftime('%m%d%H%M%Y.%S')

    @staticmethod
    def utc(dt):
        return dt.strftime('UTC%z')[:-2]

    @staticmethod
    def utc_hour_min(dt):
        return dt.strftime('%H:%M')

    @staticmethod
    def valid_format(year, month, day):
        return '{month}/{day}/{year}'.format(year=year, month=month, day=day)

    @staticmethod
    def weekday_separator_date(dt):
        return dt.strftime('%a, %m/%d/%Y')

    @staticmethod
    def weekday_separator_date_year(dt):
        return dt.strftime('%a, %b %d, %I:%M %p %Y')

    @staticmethod
    def weekday_separator_short(dt):
        return dt.strftime('%a, %b %d')

    @staticmethod
    def weekday_short(dt):
        return DateTimeFormatter.standard(dt)

    @staticmethod
    def Y_M_D(dt):
        return dt.strftime('%Y-%m-%d')

    @staticmethod
    def YMD(dt):
        return dt.strftime('%Y%m%d')

    @staticmethod
    def year(dt):
        return dt.strftime('%Y')

    @staticmethod
    def twelve_hour_fmt(dt):
        # Keeping this format to use emails across all locales
        # Please don't change to DateTimeFormatter.time_h_m(dt)
        # Please don't create in different locales
        return dt.strftime('%I:%M %p').lstrip('0')

    @staticmethod
    def usa_short_input(dt):
        # Used as a workaround for places where usa format is used in diff locales
        # Don't create in different locales
        # Don't replace with short_input
        return dt.strftime('%m/%d/%Y')

    @staticmethod
    def hour_min_only(dt):
        # Used as a workaround for places where usa format is used in diff locales
        # Don't create in different locales
        return dt.strftime('%H:%M').lstrip('0')

    @staticmethod
    def usa_time_extended(dt):
        # Used as a workaround for places where usa format is used in diff locales
        # Don't create in different locales
        return dt.strftime('%I:%M:%S %p')
    @staticmethod
    def get_datetime():
        """
        this returns datetime in us eastern timezone
        :return: datetime.datetime
        """
        return datetime.now(pytz.timezone(TimeZones.us_eastern))

    @staticmethod
    def days_added_default_format(dt):
        return DateTimeFormatter.short_input(dt)

    @staticmethod
    def calendar_flyout_format_short(dt):
        return DateTimeFormatter.short_input(dt)

    @staticmethod
    def resource_weekday(dt):
        return DateTimeFormatter.weekday_short(dt)

    @staticmethod
    def calendar_date_filter(dt):
        return DateTimeFormatter.short_input(dt)

    @staticmethod
    def email_connector_date(dt):
        return DateTimeFormatter.short(dt)

    @staticmethod
    def time_period(dt):
        return '{dt.month}/{dt.day}/{dt.year}'.format(dt=dt)

    @staticmethod
    def calendar_flyout_time(dt):
        return DateTimeFormatter.rw_time_short(dt)

    @staticmethod
    def time_reminder_date(dt):
        # March 1, 2022
        # No leading zero for day
        return '{dt:%B} {dt.day}, {dt.year}'.format(dt=dt)

    @staticmethod
    def time_short_validation(dt):
        return DateTimeFormatter.time_short(dt=dt)

    @staticmethod
    def mui_date_format(dt):
        """
        MUI project work plan date format
        :param dt:
        :return:
        """
        return dt.strftime('%#m/%#d/%Y')  # 6/4/2023

    @staticmethod
    def date_time_with_24hrs_format(dt):
        """
        :param dt:
        :return:
        """
        return dt.strftime('%m/%d/%Y, %H:%M')

    @staticmethod
    def notes_report_time_stamp_long(dt):
        # No Leading Zeros hours, month or day
        # Full length Weekday
        return '{standard_long_date} {time} {utc}'.format(standard_long_date=DateTimeFormatter.standard_long(dt),
                                                          time=DateTimeFormatter.time_short(dt),
                                                          utc=DateTimeFormatter.utc(dt))
