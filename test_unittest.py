import os
import warnings
from werkzeug import test
from Project import app 
from selenium import webdriver
import traceback
import unittest
import time
from Project import models


test1_name="DEEPAKRAJ"
test1_email="deepakraj@gmail.com"
test1_password="Welcome@1234"
test1_rpassword="Welcome@1234"


test2_name="DEEPAK"
test2_email="deepakraj@gmail.com"
test2_password="Welcome@1234"
test2_rpassword="Welcome@1234"


test3_name="DEEPAK"
test3_email="deepak@gmail.com"
test3_password="Welcome@1234"
test3_rpassword="Welcome@12"


test4_name="DEEPAKRAJ"
test4_password="Welcome@1234"

test5_name="ABCD"
test5_password="AAAA"


test6_name="DEEPAKRAJ"
test6_password="Welcome@123"







BASE_URL = "http://127.0.0.1:5000"


class TestSetup(unittest.TestCase):

    def setUp(self):
        """
        Called in every test to activate the driver
        """
        # create a new Chrome session
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.maximize_window()

    def tearDown(self):
        # close the browser window
        self.driver.quit()



class UserRegistration(TestSetup):
    register_url = (BASE_URL + "/register")
    login_url = (BASE_URL + "/login")

    def test_registration(self):
       
        try:
        
            self.driver.get(self.register_url)
            self.driver.find_element_by_id("name").send_keys(test1_name)
            self.driver.find_element_by_id("email").send_keys(test1_email)
            self.driver.find_element_by_id("password").send_keys(test1_password)
            self.driver.find_element_by_id("re_password").send_keys(test1_password)

            self.driver.find_element_by_id("submit").click()
            time.sleep(1)

            success_message = self.driver.find_element_by_id("header1").text
            
            self.assertEqual("Please Sign in with your name",success_message)
            print("Successfully Registered")

        except Exception as e:
            print(traceback.format_exc())

        

            

    def test_registration_sameuser(self):
       
        try:
        
            self.driver.get(self.register_url)
            self.driver.find_element_by_id("name").send_keys(test2_name)
            self.driver.find_element_by_id("email").send_keys(test2_email)
            self.driver.find_element_by_id("password").send_keys(test2_password)
            self.driver.find_element_by_id("re_password").send_keys(test2_password)

            self.driver.find_element_by_id("submit").click()
            time.sleep(1)

            success_message = self.driver.find_element_by_id("error").text
            
            self.assertEqual("User/email id already existing",success_message)
            print("Sucessfully Checked Same user")


        except Exception as e:
            print(traceback.format_exc())
            print("user with same email id ")


    
            
            

        


    def test_registration_password_mismatch(self):
       
        try:
            self.driver.get(self.register_url)

            # Fill in registration form

            self.driver.find_element_by_id("name").send_keys(test3_name)
            self.driver.find_element_by_id("email").send_keys(test3_email)
            self.driver.find_element_by_id("password").send_keys(test3_password)
            self.driver.find_element_by_id("re_password").send_keys(test3_rpassword)

            self.driver.find_element_by_id("submit").click()

            time.sleep(1)

           
            success_message = self.driver.find_element_by_id("error").text

            
            self.assertEqual("Password mismatching",success_message)
            
            print("Successfully found Password Mismatch")
            

        except Exception as e:
            print(traceback.format_exc())




class Login(TestSetup):
    login_url = BASE_URL + "/login"
    user_url=BASE_URL+"/users"

    def test_login(self):
       
        self.driver.get(self.login_url)

        self.driver.find_element_by_id("username").send_keys(test4_name)
        self.driver.find_element_by_id("password").send_keys(test4_password)

        self.driver.find_element_by_id("login-submit").click()
        time.sleep(1)

        
        assert self.user_url in self.driver.current_url
        print("Correct Url Opened")

        value=self.driver.find_element_by_id("username").text

        self.assertEqual(test1_name,value)
        print("Login-Sucessfull")




    def test_login_invalid_user(self):

        self.driver.get(self.login_url)

        self.driver.find_element_by_id("username").send_keys(test5_name)
        self.driver.find_element_by_id("password").send_keys(test5_password)

        self.driver.find_element_by_id("login-submit").click()
        time.sleep(1)

        
        assert self.login_url in self.driver.current_url
        print("Correct Url Opened")

        value=self.driver.find_element_by_id("error").text

        self.assertEqual("User not exists please register !!!",value)

        print("Success checked Mismatch users")



    def test_login_user_pawword_mismatch(self):
        self.driver.get(self.login_url)

        self.driver.find_element_by_id("username").send_keys(test6_name)
        self.driver.find_element_by_id("password").send_keys(test6_password)

        self.driver.find_element_by_id("login-submit").click()
        time.sleep(1)

        
        assert self.login_url in self.driver.current_url
        print("Correct Url Opened")

        value=self.driver.find_element_by_id("error").text

        self.assertEqual("Username or password is wrong",value)

        print("Success checked wrong password")


class Navigation(TestSetup):

    user_url= BASE_URL+ "/users"
    material_url=BASE_URL + "/material"
    quiz_URL=BASE_URL + "/questions"

    def test_navigation_users(self):
        self.driver.get(self.user_url)
        self.driver.find_element_by_id("agile").click()

        assert self.material_url in self.driver.current_url

        value=self.driver.find_element_by_id("title1").text
        self.assertEqual("AGILE METHODOLOGY",value)
        print("Successfully  Navigated to Content Page")
    def test_navigation_quiz(self):
        self.driver.get(self.user_url)
        self.driver.find_element_by_id("quiz").click()

        assert self.material_url in self.driver.current_url

        value=self.driver.find_element_by_id("title2").text
        self.assertEqual("AGILE METHODOLOGY - ASSESMENT",value)
        print("Successfully Navigated to Question Page")

if __name__ =="__main__":
     with warnings.catch_warnings():
        warnings.simplefilter('ignore', category=ImportWarning)
        unittest.main()

