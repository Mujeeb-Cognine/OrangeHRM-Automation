from OrangeHRMData._BaseLocalizationClass import _BaseNoLocalizationClass


class LoginPageLocators(_BaseNoLocalizationClass):
    user_name_field = "//input[@name='username']"
    password_field = "//input[@name='password']"
    submit_button = "//button[@type='submit']"
