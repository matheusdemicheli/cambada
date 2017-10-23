# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_cambada project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_cambada'

SPIDER_MODULES = ['scrapy_cambada.spiders']
NEWSPIDER_MODULE = 'scrapy_cambada.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_cambada (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
  'scrapy_cambada.pipelines.ScrapyCambadaPipeline': 800,
}
