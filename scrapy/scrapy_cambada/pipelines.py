# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ScrapyCambadaPipeline(object):

    def open_spider(self, spider):
        self.arquivo = open('frases_historicas.json', 'w')

    def close_spider(self, spider):
        self.arquivo.close()

    def process_item(self, item, spider):
        line = {
            'pk': None,
            'model': 'frases_historicas.FraseHistorica',
            'fields': dict(item)
        }
        line = json.dumps(line)
        self.arquivo.write(line + ',\n')
        return item
