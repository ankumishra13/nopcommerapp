import flag as flag
from selenium.webdriver.common.by import By


class SearchCustomer:
    txtemail_id = 'SearchEmail'
    searchicon_xpath = '/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[1]/div/div[1]/div[2]/i'
    searchbtn_id = 'search-customers'
    table_xpath = '//*[@id="customers-grid"]'
    tblerowcount_xpath = '//*[@id="customers-grid"]/tbody/tr'
    tblecolom_xpath = '//*[@id="customers-grid"]/tbody/tr/td'

    def __init__(self, driver):
        self.driver = driver

    def searchicon(self):
        self.driver.find_element(By.XPATH, self.searchicon).click()

    def setemail(self, email):
        self.driver.find_element(By.ID, self.txtemail_id).send_keys(email)

    def clicksearch(self):
        self.driver.find_element(By.ID, self.searchbtn_id).click()

    def getrowscount(self):
        return len(self.driver.find_elements(By.XPATH, self.tblerowcount_xpath))

    def getcolomscount(self):
        return len(self.driver.find_element(By.ID, self.tblerowcount_xpath))

    def searchcustemail(self,email):
        flag = False
        print("getting row")
        print(self.getrowscount())
        for r in range(1,self.getrowscount()+1):
            print("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]")
            emailid = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
           # return True
                flag = True
                break
        return flag


