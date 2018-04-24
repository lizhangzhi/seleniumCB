from Util import *

# -*- coding: utf-8 -*-


class SamPage(BasePage):
    # SAM>affiliate定位
    affiliate_id_loc = (By.NAME, "selectAffiliate")
    # SAM>search by定位（通过CIN, Corporation name, Corporation ID）
    search_by_loc = (By.NAME, "columnName")
    # SAM>company id定位
    company_id_value_loc = (By.NAME, "columnValue")
    submit_button = (By.NAME, "submit_affiliate")
    search_button = (By.NAME, "submit_search")
    # SAM>company link定位
    company_link_loc = (By.XPATH, "//a[contains(@href,'EditComprehensiveView')]")

    # Edit company>user tab
    user_tab_loc = (By.XPATH, "//a[contains(@href,'corp/UserSearch/transferContext')]")
    # Edit company page>PA link
    pa_link_loc = (By.XPATH, "//a[contains(@href,'corp/corporationViewDetails/panelAuth')]")

    # Go to Edit corporation page
    def go_to_edit_corporation_page(self, affiliate_id, search_by, companyid):
        self.open_menu("CORPORATIONS", "CORPORATIONS")
        self.select_dropdown(self.affiliate_id_loc).select_by_value(affiliate_id)
        self.find_element(self.submit_button, clickable=True).click()
        self.select_dropdown(self.search_by_loc).select_by_value(search_by)
        self.send_keys(self.company_id_value_loc, companyid, True, True)
        self.find_element(self.search_button, clickable=True).click()
        self.find_element(self.company_link_loc, clickable=True).click()

    # Go to edit corporation>user tab
    def click_user_tab(self):
        self.find_element(self.user_tab_loc, clickable=True).click()

    # Go to edit corporation>PA page
    def click_pa_link(self):
        self.find_element(self.pa_link_loc, clickable=True).click()
