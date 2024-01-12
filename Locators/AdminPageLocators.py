from OrangeHRMData._BaseLocalizationClass import _BaseNoLocalizationClass


class AdminUserLocators(_BaseNoLocalizationClass):
    system_user_card = "//div[@class='oxd-table-filter']"
    username_field = "//div[@class='oxd-input-group oxd-input-field-bottom-space']/div/input"
    user_role_field_caret_icon = "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]"
    user_role_option = "//span[contains(text(), %s)]"
    emp_name_field = "//input[@placeholder='Type for hints...']"
    emp_name_option = "//span[contains(text(), %s)]"
    status_field_caret_icon = "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]"
    status_field_option = "//span[contains(text(), %s)]"
    submit_button = "//button[@type='submit']"
    add_button = "//button//i[contains(@class,'bi-plus')]"
    add_user_card = "//div[@class='orangehrm-card-container']"


class AdminAddUserLocators(_BaseNoLocalizationClass):
    user_name_field = "(//input[@class='oxd-input oxd-input--active'])[2]"
    password_field = "(//input[@type='password'])[1]"
    confirm_password_field = "(//input[@type='password'])[2]"

