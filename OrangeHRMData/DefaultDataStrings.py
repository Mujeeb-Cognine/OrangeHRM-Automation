from OrangeHRMData._BaseLocalizationClass import _BaseNoLocalizationClass


class AdminUserRoles(_BaseNoLocalizationClass):
    admin = 'Admin'
    ess = 'ESS'


class AdminStatus(_BaseNoLocalizationClass):
    enabled = 'Enabled'
    disabled = 'Disabled'


class UserNames(_BaseNoLocalizationClass):
    admin = 'Admin'
    john_smith = 'John.Smith'
    peter_anderson = 'Peter.Anderson'
    garry_white = 'Garry.White'
    russel_hamilton = 'Russel.Hamilton'


class DefaultDataStrings(_BaseNoLocalizationClass):
    admin_user_roles = AdminUserRoles
    admin_status = AdminStatus
    user_names = UserNames
