import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_1_login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()
    @pytest.mark.sanity
    def test_homepagetitle(self,setup):
        self.logger.info("******* homepage title**************")
        self.driver =setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******** title passed********")
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_homepagetitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("************** login test started ************************")
        self.driver =setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************** login test passsed ************************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_test_login_title.png")
            self.logger.info("************** title no matching ************************")
            self.driver.close()
            assert False
        self.logger.info("************** login tests completed ************************")

