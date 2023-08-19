import time

import pytest

from PageObject.LoginPage import LoginPage
from PageObject.AddcustomerPage import AddCustomer
from PageObject.Searchcustomerpage import SearchCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_searchcustbyemail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchcustemail(self,setup):
        self.logger.info("******** search customer by email ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("****Login Successful****")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickoncustomermenu()
        self.addcust.clickoncustomermenuitem()

        self.logger.info("****************searching cust by emailid *************************")
        searchcust=SearchCustomer(self.driver)
      #  searchcust.searchicon()
        time.sleep(5)
        searchcust.setemail("victoria_victoria@nopCommerce.com")
        searchcust.clicksearch()
        time.sleep(5)
        status=searchcust.searchcustemail("victoria_victoria@nopCommerce.com")
        print(status)
        assert True==status
        self.logger.info("********** search by email finished *******************")
