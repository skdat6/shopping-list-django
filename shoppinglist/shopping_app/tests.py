from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import logging
import unittest
import time
import random

# Create your tests here.


USERNAME = 'test0'+str(random.randint(0, 435151361))
PASSWORD = 'test0'+str(random.randint(0, 435151361))
EMAIL = 'test0'+str(random.randint(0, 435151361))+'@test.com'
NOW = datetime.now().strftime('%Y-%m-%d---%H-%M-%S')


class UserForm(unittest.TestCase):
    logging.basicConfig(filename='/test_log-%s.log' % NOW,
                        level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s\n')

    def test_register_form(self):
        selenium = webdriver.Chrome()
        # Choose your url to visit
        selenium.get('http://127.0.0.1:8000/register/')
        # find the elements you need to submit form
        user_name = selenium.find_element(By.ID, "id_username")
        user_email = selenium.find_element(By.ID, "id_email")
        user_password = selenium.find_element(By.ID, "id_password")

        submit = selenium.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/input[2]")

        # populate the form with data
        user_name.send_keys(USERNAME)
        user_email.send_keys(EMAIL)
        user_password.send_keys(PASSWORD)

        # submit form
        submit.click()
        time.sleep(3)
        # check result; page source looks at entire html document
        try:
            self.assertEqual('Thank you for registexxxring',
                             selenium.find_element(By.XPATH, '/html/body/div/div/h1').text)
        except AssertionError as a:
            selenium.save_screenshot('screenshot-%s.png' % NOW)
            logging.info(a)


class UserFormLogin(unittest.TestCase):
    logging.basicConfig(filename='/test_log-%s.log' % NOW,
                        level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s\n')
    def test_login_form(self):
        selenium = webdriver.Chrome()
        # Choose your url to visit
        selenium.get('http://127.0.0.1:8000/user_login/')
        # find the elements you need to submit form
        user_email = selenium.find_element(By.ID, "email2")
        user_password = selenium.find_element(By.ID, "password2")

        submit = WebDriverWait(selenium, 20).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div/div/form/button")))

        # populate the form with data
        user_email.send_keys(USERNAME)
        user_password.send_keys(PASSWORD)

        # submit form
        submit.click()
        WebDriverWait(selenium, 20).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/ol/div/div/div/div/div[1]/div/h4")))

        try:
            self.assertFalse('fail it')

        except Exception as e:
            selenium.save_screenshot('screenshot-%s.png' % NOW)
            logging.info(e)


