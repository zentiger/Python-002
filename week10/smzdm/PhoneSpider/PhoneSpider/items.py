# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from smzdm_phone import models

class PhonespiderItem(DjangoItem):
    # define the fields for your item here like:
    print("In item: ")
    django_model = models.PhonespiderItem
