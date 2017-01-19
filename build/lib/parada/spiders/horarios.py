import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "horarios"

    def start_requests(self):
        url = 'http://mibondiya.cba.gov.ar/Datos.aspx?pCodigoEmpresa=401&pCodigoLinea=24&pCodigoOrigen=124&pCodigoDestino=1&pServicio=SAN%20NICOLAS%20A%20CORDOBA%20CAPITAL&pCodigoParada=&pProveedor=yv'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        selectorItems = 'ul.servicios'
        data = response.css(selectorItems)

        info = data.css('div.salida')

        dataParse = []

        
        for pos in info:
            labels = pos.css('label::text')
            
            dataParse.append(labels.extract())
            '''
            for label in labels:
                dataParse.append(labels)
            '''
        yield {
            'data' : dataParse
        }
        