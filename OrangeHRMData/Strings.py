class Strings(object):
    def __init__(self, locale=None):
        self._locale = locale
        super(Strings, self).__init__()

    @property
    def menu(self):
        try:
            return self.__menu
        except AttributeError:
            from OrangeHRMData.GlobalData import MenusAndSubMenus
            self.__menu = MenusAndSubMenus(os_locale=self._locale)
            return self.__menu

    @property
    def default_data(self):
        try:
            return self.__default_data
        except AttributeError:
            from OrangeHRMData.DefaultDataStrings import DefaultDataStrings
            self.__default_data = DefaultDataStrings(os_locale=self._locale)
            return self.__default_data

    @property
    def dd(self):
        return self.default_data
