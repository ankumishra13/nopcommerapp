import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomer():
    linkcustomermenu_xpath = '/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p'
    lincustomermenuitem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    addnewbtn_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    txtemail_xpath="/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[1]/div[2]/input"
    txtpassword_xpath='//*[@id="Password"]'
    txtfirstname_xpath='//*[@id="FirstName"]'
    txtcustomeroles_xpath='//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    listitemregister_xpath='//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[1]'
    listitemguest_xpath='// *[ @ id = "SelectedCustomerRoleIds_taglist"] / li[2] / span[1]'
    listiteadministrators_xpath="//[contains(text(),Administrators)]"
    btnsave_xpath="/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

    def __init__(self,driver):
        self.driver = driver

    def clickoncustomermenu(self):
        self.driver.find_element(By.XPATH,self.linkcustomermenu_xpath).click()

    def clickoncustomermenuitem(self):
        self.driver.find_element(By.XPATH, self.lincustomermenuitem_xpath).click()

    def clickonaddnew(self):
        self.driver.find_element(By.XPATH, self.addnewbtn_xpath).click()

    def setemail(self,email):
        self.driver.find_element(By.XPATH, self.txtemail_xpath).send_keys(email)

    def password(self,password):
        self.driver.find_element(By.XPATH, self.txtpassword_xpath).send_keys(password)

    def fitstname(self,firstname):
        self.driver.find_element(By.XPATH, self.txtfirstname_xpath).send_keys(firstname)

    def customerole(self,customerole):
        self.driver.find_element(By.XPATH, self.txtcustomeroles_xpath).send_keys(customerole)

    def clickonsave(self):
        self.driver.find_element(By.XPATH,self.btnsave_xpath).click()


