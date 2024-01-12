from OrangeHRMData._BaseLocalizationClass import _BaseNoLocalizationClass


class BasePageLocators(_BaseNoLocalizationClass):
    menu_button = "//button[contains(@class, 'oxd-main-menu-button')]"
    side_menu_close = "bi-chevron-left"
    menu_name_option = "//span[normalize-space()=%s]"
    all_menu_names = "//li[@class='oxd-main-menu-item-wrapper']"
    menu_search_field = "//input[@placeholder='Search']"
    menu_names = "//ul[@class='oxd-main-menu']"
    grid_checkbox = "//div[@class='oxd-table-card-cell-checkbox']//input[@type='checkbox']"
    delete_icon = "//i[contains(@class,'bi-trash')]"
    checkbox = "//input[@type='checkbox']"
    yes_or_delete_btn = "//div[contains(@class,'orangehrm-dialog-popup')]//button[@type='button'][2]"
    no_or_cancel_btn = "//div[contains(@class,'orangehrm-dialog-popup')]//button[@type='button'][1]"
    table_body = "//div[@class ='oxd-table-body']"
    orangehrm_dialog_popup = "//div[contains(@class,'orangehrm-dialog-popup')]"
    alert_success_text = "//div[contains(@class,'oxd-toast-container')]//p[text()='Success']"
    orangehrm_dialog = "//div[contains(@class,'orangehrm-dialog-modal')]//button[@type='button']"
    orangehrm_dialog_save_button = "//button[@type='submit']"
    toggle_switch_wrapper = "//div[contains(@class,'oxd-switch-wrapper')]//label//span"
    toggle_switch = "//span[contains(@class,'oxd-switch-input')]"
    cancel_button = "//button[normalize-space()='Cancel']"
    save_button = "//button[normalize-space()='Save']"
