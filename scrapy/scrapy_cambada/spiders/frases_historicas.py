#-*- coding: utf-8 -*-
import scrapy
from scrapy.utils.url import urljoin_rfc
from scrapy.utils.response import get_base_url
from scrapy_cambada.items import FrasesHistoricasItem


class FrasesHistoricasSpider(scrapy.Spider):
    name = "frases_historicas"

    start_urls = [
        'file:///home/matheus/%C3%81rea%20de%20Trabalho/Frases%20Hist%C3%B3ricas/c27304110-t87bfc5ef83d83244.html/c27304110-t87bfc5ef83d83244.html',
    ]

    def parse(self, response):
        mensagens = response.xpath(
            '//div[@class="forumMetadata borderBottomSeparator"]'
        )
        for mensagem in mensagens:
            div_autor = mensagem.css('.typoTopicCreator')
            autor = div_autor.xpath('text()').extract()[0][:-3]

            div_data = mensagem.css('.typoSectionLessImportantText')
            data = div_data.xpath('text()').extract()[0]

            texto = ''
            for t in mensagem.xpath('div/text()').extract():
                texto += '%s<br>' % t

            item = FrasesHistoricasItem()
            item['autor'] = unicode(autor)
            item['data'] = unicode(data)
            item['texto'] = unicode(texto[:-4])
            yield item

        proxima_url = response.xpath(u"//a[text()='próxima >']/@href").extract()
        if proxima_url:
            link = urljoin_rfc(get_base_url(response), proxima_url[0])
            yield scrapy.Request(link, callback=self.parse)
