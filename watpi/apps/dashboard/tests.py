# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from selenium import webdriver
import unittest
import os


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        chromedriver = '/usr/local/bin/chromedriver'
        self.browser = webdriver.Chrome(chromedriver)

    def tearDown(self):
        self.browser.quit()

    def test_django_server_running(self):
        # A new user tries WatPi for the first time. They decide
        # to visit the site first @ http://localhost:8000
        self.browser.get('http://localhost:8000')

    def test_dashboard_site_exists(self):
        # Then after logging in, they redirect to the dashboard URL.
        self.browser.get('http://localhost:8000/dashboard')

    def test_site_title_says_watpi(self):
        # At the top of the browser, they see the page title says "WatPi."
        self.browser.get('http://localhost:8000/dashboard')
        self.assertIn('WatPi', self.browser.title)

    def test_site_header_says_watpi(self):
        # Further down on the page, the header also identifies the site as "WatPi."
        self.browser.get('http://localhost:8000/dashboard')
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('WatPi', header_text)


if __name__ == '__main__':
    unittest.main()
