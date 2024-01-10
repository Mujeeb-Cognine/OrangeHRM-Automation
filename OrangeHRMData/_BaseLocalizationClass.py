import locale


class _BaseLocalizationClass(object):
    """
    Base class for i18n/l10n language strings. All language string classes will need to extend this base class.

    Localized files are stored in a subdirectory: l10n > {LanguageCode}. Ex: .\l10n\en_GB\GlobalData.py
    The localized directory requires an __init__ file, and the file names are identical to that of the default files.
    The localized classes inside these files need to extend the default class of the same name.

    Language string format uses a combination of ISO 639-1 two-letter language codes,
    followed by the ISO 3166-1 two letter country codes (if applicable) (separated by underscore)
    Examples: en_US (English - United States), en_GB (English - Great Britain, fr (French - France),
              fr_CA (French - Canada), es (Spanish - Spain), ex_PR (Spanish - Puerto Rico) pt (Portuguese - Portugal),
              pt_BR (Portuguese - Brazil)

    For code references:
    ISO 639-1: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    ISO 3166-1 Alpha 2: http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements

    If a language code class file does not exist, it will default to the base English (US) class.
    If a language code class DOES exist, but does not contain a particular variable, it will use the default en_US one.
    """

    def __new__(cls, os_locale=None):

        windows_locale_map = {
            'da_dk': 'da',
            'de_de': 'de',
            'en_au': 'en_au',
            'en_gb': 'uk',
            'en_us': 'us',
            'es_es': 'es',
            'fi_fi': 'fi',
            'fr_fr': 'fr',
            'it_it': 'it',
            'nl_nl': 'nl',
            'no_no': 'no',
            'pl_pl': 'pl',
            'sv_se': 'sv'
        }

        if os_locale is None:
            os_locale = locale.getdefaultlocale()[0]
            locale.setlocale(locale.LC_ALL, '')
        elif os_locale.lower() in windows_locale_map:
            try:
                locale.setlocale(locale.LC_ALL, windows_locale_map[os_locale.lower()])
            except:
                return cls
        else:
            locale.setlocale(locale.LC_ALL, os_locale)

        # Fix for Mac Run
        if os_locale is None or os_locale.lower() == 'en_us':
            return cls
        else:
            _string_class = str(cls).split('\\')[0].split('.')[-1].split('\'')[0]
            _file_path = str(cls).split('\\')[0].split('.')[-2]
            try:
                return getattr(__import__("AutomationTests._Data.GoodPSAData.l10n.%s.%s" % (os_locale, _file_path),
                                          fromlist=[_string_class]), _string_class)
            # if it doesn't exist, we'll fall back on the default en_US class
            except:
                return cls


class _BaseNoLocalizationClass(_BaseLocalizationClass):
    """
    Base class for string classes that should not be localized to other languages
    """

    def __new__(cls, os_locale="en_us"):
        return cls
