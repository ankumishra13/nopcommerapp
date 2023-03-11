import pytest
import time
from selenium.webdriver.common.by import By
from PageObject.AddcustomerPage import AddCustomer
from PageObject.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import string
import random


class Test_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addcustomer(self,setup):
        self.logger.info("******** Test add customer  ************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("****Login Successful****")

        self.logger.info("****starting add customer test****")

        self.addcust= AddCustomer(self.driver)

        self.addcust.clickoncustomermenu()
        self.addcust.clickoncustomermenuitem()

        self.addcust.clickonaddnew()
        self.logger.info("*********providing cust info *********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setemail(self.email)
        self.addcust.password("test123")
        self.addcust.fitstname("Abk")
       # self.addcust.customerole("Administrators")
        self.addcust.clickonsave()
        self.logger.info("********saving cust info ***********")

        self.logger.info("******** validation started **********")

        self.msg= self.driver.find_element(By.TAG_NAME,"body").text

       # print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("*********cutomer added **********")
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test add customer.png")
            self.logger.info("***********add customer failed *****")
            assert True == False

        self.driver.close()
        self.logger.info("**Ending add customer**")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return  ''.join(random.choice(chars) for x in range(size))