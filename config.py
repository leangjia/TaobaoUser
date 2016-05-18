# -*- coding:utf-8 -*-
from selenium import webdriver

URL_FILE = 'file/urls.txt'

OUT_FILE = 'file/result.xls'

DRIVER = webdriver.Chrome()

TIMEOUT = 30

MAX_SCROLL_TIME = 10

ANONYMOUS_STR = '***'

MAX_STAR = 3

FILTER_STAR = True

STAR_INFO_URL = 'http://www.taoyitu.com/'

MAX_DAY = 10

WRONG_DATE_COUNT = 0

WRONG_DATE_MAX_COUNT = 50

NEXT_PAGE_COMMENTS = 1

FILTER_DATE = True

MAX_COMMENTS_COUNT = 2000

MAX_COMMENTS_LIMIT = True

NEXT_PAGE_WAIT = 2