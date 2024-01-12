import time

from BaseUtils.HTMLAttributes import HTMLAttributes
from Locators.BasePageLocators import BasePageLocators
from _Wrapper.BaseClass import BaseClass
from OrangeHRMData.Constants import Constants


class BasePageFragments(BaseClass):

    def __init__(self):
        BaseClass.__init__(self)

    def menu_button(self):
        return BasePageLocators().menu_button

    def side_menu_close(self):
        return BasePageLocators().side_menu_close

    def menu_name_option(self):
        return BasePageLocators().menu_name_option

    def all_menu_items(self):
        return BasePageLocators().all_menu_names

    def menu_search_field(self):
        return BasePageLocators().menu_search_field

    def menu_names(self):
        return BasePageLocators().menu_names

    def grid_checkbox(self):
        return BasePageLocators().grid_checkbox

    def delete_icon(self):
        return BasePageLocators().delete_icon

    def checkbox(self):
        return BasePageLocators().checkbox

    def yes_or_delete_button(self):
        return BasePageLocators().yes_or_delete_btn

    def no_or_can_delete_button(self):
        return BasePageLocators().no_or_cancel_btn

    def table_body(self):
        return BasePageLocators().table_body

    def orangehrm_dialog_popup(self):
        return BasePageLocators().orangehrm_dialog_popup

    def alert_success_text(self):
        return BasePageLocators().alert_success_text

    def orangehrm_dialog(self):
        return BasePageLocators().orangehrm_dialog

    def orangehrm_dialog_save_button(self):
        return BasePageLocators().orangehrm_dialog_save_button

    def toggle_switch_wrapper(self):
        return BasePageLocators().toggle_switch_wrapper

    def toggle_switch(self):
        return BasePageLocators().toggle_switch

    def cancel_button(self):
        return BasePageLocators().cancel_button

    def save_button(self):
        return BasePageLocators().save_button

    def navigate_to_menu(self, menu_name):
        menu_button = self.find_element_by_xpath(self.menu_button())
        if self.side_menu_close() not in menu_button.get_attribute(HTMLAttributes().class_attr):
            menu_name_path = self.menu_name_option() % f'"{menu_name}"'
            self.click_element(element_locator=menu_name_path)
        else:
            self.click_element(menu_button)
            self.wait_for_all_elements_presence(elements_locator=self.all_menu_items())
            menu_name_path = self.menu_name_option() % f'"{menu_name}"'
            self.click_element(element_locator=menu_name_path)

    def search_and_select_menu(self, menu_name):
        menu_button = self.find_element_by_xpath(self.menu_button())
        if self.side_menu_close() not in self.get_attribute(element_locator=menu_button,
                                                            attribute_name=HTMLAttributes().class_attr):
            self.send_keys_to_element(element_locator=self.menu_search_field(), keys=menu_name)
            self.click_element(element_locator=self.menu_names())
        else:
            self.click_element(menu_button)
            self.wait_for_element_presence(element_locator=self.menu_names())
            self.send_keys_to_element(element_locator=self.menu_search_field(), keys=menu_name)
            self.click_element(element_locator=self.menu_names())

    def click_grid_checkbox_after_filter(self):
        self.click_element(element_locator=self.grid_checkbox())

    def click_delete_icon(self):
        self.click_element(element_locator=self.delete_icon())

    def click_checkbox(self):
        self.click_element(element_locator=self.checkbox())

    def click_yes_or_delete_in_dialog(self):
        self.click_element(element_locator=self.yes_or_delete_button())

    def click_no_or_cancel_in_dialog(self):
        self.click_element(element_locator=self.no_or_can_delete_button())

    def wait_until_grid_loads(self):
        self.wait_for_element_presence(element_locator=self.table_body())

    def wait_until_confirmation_dialog_appears(self):
        self.wait_for_element_presence(element_locator=self.orangehrm_dialog_popup())

    def verify_success(self):
        self.wait_for_element_presence(element_locator=self.alert_success_text())
        self.is_element_displayed(self.alert_success_text())

    def wait_until_ornghrm_dialog_appears(self):
        self.wait_for_element_presence(element_locator=self.orangehrm_dialog())

    def click_ornghrm_dialog_save(self):
        self.click_element(self.orangehrm_dialog_save_button())

    def click_toggle_switch(self):
        self.wait_for_element_presence(element_locator=self.toggle_switch_wrapper(), timeout=Constants.default_throttle)
        time.sleep(2)  # Added sleep as it is taking time to render on the UI.
        self.click_element(self.toggle_switch())

    def click_cancel(self):
        self.click_element(self.cancel_button())

    def click_save(self):
        self.click_element(self.save_button())
