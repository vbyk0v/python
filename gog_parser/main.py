# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
import time



def download_pages():
    for page in range(1, 3):
        url_to_open = 'https://www.gog.com/games?sort=popularity&page=' + str(page)
        print("openning url:" + url_to_open + '...')
        page_id = urlopen(url_to_open).read()
        soup = BeautifulSoup(page_id, features='html.parser')
        dir = str(os.getcwd())
        search_all = soup.find_all()
        search_all = str(search_all)

       # finder = re.findall(r'supportUrl":"............................', search_all)
        finder = re.findall(r'"url":"........\w+', search_all)

        print(finder)

        new_finder=[]

        for game in finder:
            new_finder.append(game[15:])


        print(new_finder)


def sel():


    # options = Options()
    # options.add_argument("-headless")
    #
    # #options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    # options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    # chrome_driver_binary = dir = str(os.getcwd()) + "\chromedriver.exe"
    #
    # driver = webdriver.Chrome(dir, options=options)
    # #
    # driver = webdriver.PhantomJS()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")

    capabities = webdriver.DesiredCapabilities.CHROME
    capabities.update({"javascriptEnabled": True})
    driver = webdriver.Chrome(desired_capabilities=capabities, options=chrome_options)
    driver.get("http://httpbin.org/cookies")
    driver.add_cookie({"name": "drag", "value": "lol", "domain": "httpbin.org"})
    driver.refresh()
    driver.get_cookies()

    driver.get('https://www.gog.com/games?page=1&sort=title')

    sdf = driver.find_element_by_xpath('paginator.goToPage')
    print(sdf)

    html = driver.page_source
    soup = BeautifulSoup(html, features='html.parser')
    search_all = soup.find_all()
    search_all = str(search_all)
    finder = re.findall(r'"url":"........\w+', search_all)

    print(finder)


def firef():
    options = Options()
    options.add_argument('-headless')

    driver = webdriver.Firefox(
        executable_path='C:\\bitbucket\\test\gog_parser\\geckodriver.exe',
        firefox_binary='C:\\Program Files\\Mozilla Firefox\\firefox.exe',
        options=options
    )

    wait = WebDriverWait(driver, timeout=10)
    driver.get('https://www.gog.com/games?sort=popularity&page=17')
    html = driver.page_source
    soup = BeautifulSoup(html, features='html.parser')
    search_all = soup.find_all()
    search_all = str(search_all)
    finder = re.findall(r'"url":"........\w+', search_all)

    print(finder)
    pass

sel()

