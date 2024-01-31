import babel.dates
import datetime
import locale

from OrangeHRMData._BaseLocalizationClass import _BaseLocalizationClass


class DateTimeParser(_BaseLocalizationClass):

    @staticmethod
    def calendar(string):
        return datetime.datetime.strptime(string, '%a, %b %d, %Y')

    @staticmethod
    def calendar_range(string):
        date_range_text = string.split(" - ")
        end_date = datetime.datetime.strptime(date_range_text[1], '%b %d, %Y')
        try:
            start_date = datetime.datetime.strptime(
                '{0} {1}'.format(date_range_text[0], end_date.strftime('%Y')), '%b %d %Y')
        except ValueError as e:
            # Handle scenario that occurs if the dates occur in 2 different years
            start_date = datetime.datetime.strptime(
                '{0}'.format(date_range_text[0]), '%b %d, %Y')
        return {'start': start_date, 'end': end_date}

    @staticmethod
    def dt_api(string):
        return datetime.datetime.strptime(string, '%Y-%m-%dT%H:%M:%SZ')

    @staticmethod
    def dt_standard_listview(string):
        return datetime.datetime.strptime(string, '%a %m/%d/%y %I:%M %p')

    @staticmethod
    def month(string):
        return datetime.datetime.strptime(string, '%B')

    @staticmethod
    def short(string):
        return datetime.datetime.strptime(string, '%m/%d/%Y')

    @staticmethod
    def short_listview(string):
        return datetime.datetime.strptime(string, '%m/%d/%y')

    @staticmethod
    def short_time(string):
        return datetime.datetime.strptime(string, '%m/%d/%Y %I:%M %p')

    @staticmethod
    def sla_date(string):
        return datetime.datetime.strptime(string, '%a %m/%d %I:%M %p')

    @staticmethod
    def standard(string):
        return datetime.datetime.strptime(string, '%a %m/%d/%Y')

    @staticmethod
    def time_h_m(string):
        return datetime.datetime.strptime(string, '%I:%M %p')

    @staticmethod
    def time_sheet_range(string):
        return datetime.datetime.strptime(string, '%m/%d/%Y')

    @staticmethod
    def soap_api(string):
        return datetime.datetime.strptime(string, '%Y-%m-%dT%H:%M:%S')

    @staticmethod
    def soap_api_alt(string):
        return datetime.datetime.strptime(string, '%m/%d/%Y %I:%M:%S %p')

    @staticmethod
    def activity_api_date(string):
        return DateTimeParser.short(string)

    @staticmethod
    def date_short(string):
        return DateTimeParser.short(string)

    @staticmethod
    def calendar_short(string):
        return DateTimeParser.short(string)

    @staticmethod
    def time_api_date(string):
        return DateTimeParser.short(string)

    @staticmethod
    def standard_parser(string):
        # Meant to be a cross-locale parse.
        # Due to how babel.dates.parse_date works this shouldn't need to be re-implemented in another locale file
        # Use where we previously used self.s.dt.XXXX if possible
        # Broadly, meant to for date strings made up only of ints and standard separators (period, comma, hyphen)
        t = babel.dates.parse_date(string, locale=locale.getdefaultlocale()[0])
        return datetime.datetime.combine(t, datetime.time.min)

    @staticmethod
    def portal_invoice_date(string):
        # Only define as needed. Here so it can work for NL. Other locales should be fine with the standard_parser
        return DateTimeParser.standard_parser(string=string)
