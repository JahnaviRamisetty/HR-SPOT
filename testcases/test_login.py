import time

import pytest
from selenium import webdriver
from pageobject.loginpage import Gmail
from utilities.readproperities import readconfig

class TestLogin:
    baseurl = readconfig.getApplicationURL()
    username = readconfig.getusername()
    password = readconfig.getpassword()

    def test_loginpage(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.g = Gmail(self.driver)
        self.g.setusername(self.username)
        time.sleep(4)
        #self.g.userNextClick()
        self.g.settryagain()
        self.g.setusername(self.username)
        self.g.setpswdnme(self.password)
        self.g.docompose()



