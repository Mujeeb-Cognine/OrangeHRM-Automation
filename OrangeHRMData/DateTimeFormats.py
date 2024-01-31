from OrangeHRMData._BaseLocalizationClass import _BaseLocalizationClass


class DateTimeFormats(_BaseLocalizationClass):
    standard = '%a %m/%d/%Y'                                        # Tue 09/03/2015
    standard_short = '%a %m/%d'                                     # Tue 09/03
    short = '%m/%d/%Y'                                              # 09/03/2015
    short_listview = '%m/%d/%y'                                     # 09/03/15
    weekday_separator_date = '%a, %m/%d/%Y'                         # Tue, 09/03/2015
    weekday_separator_date_year = '%a, %b %d, %I:%M %p %Y'          # Tue, Sep 03, 08:00 AM 2016
    weekday_short = '%a %m/%d/%Y'                                   # Tue 09/03/2015
    long = '%a, %b %d, %Y'                                          # Tue, Sep 03, 2015
    b_d = '%b %d'                                                   # Sep 03
    b_d_Y = '%b %d, %Y'                                             # Sep 03, 2015
    month_day = '%m/%d'                                             # 09/03
    weekday_separator_short = '%a, %b %d'                           # Tue, Sep 03
    time_h_m = '%I:%M %p'                                           # 09:06 AM
    api = '%Y-%m-%dT%H:%M:%SZ'                                      # 2015-09-03T14:06:05Z
    day_first = False
    day_short = '%a'                                                # Tue
    utc_hour_min = '%H:%M'
    midnight = '12:00 AM'
    ios_date = '%m:%d:%y'                                           # 10:31:16
    ios_time = '%I:%M:%S'                                           # 09:59:59
    tz_genymotion = '%m%d%H%M%Y.%S'                                 # 100611222016.22
    adb_time = '%Y%m%d.%H%M%S'                                      # 20160801.081931
    date_short_time = '%m/%d/%y %I:%M %p'                           # 07/22/20 06:00 PM
    date_time_rm_zero = '%#m/%#d/%y %#I:%M %p'                      # 7/22/20 6:00 PM
    time_range = short
    time_period = short
    datetime_base = '%Y-%m-%d %H:%M:%S'                             # 2021-7-22 18:30:10
    datetime_base_z = '%Y-%m-%d %H:%M:%S%z'                         # 2023-10-19 12:15:00-04:00