import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "sn-cba"

    def start_requests(self):
        url = 'http://mibondiya.cba.gov.ar/Datos.aspx?pCodigoEmpresa=401&pCodigoLinea=24&pCodigoOrigen=124&pCodigoDestino=1&pServicio=SAN%20NICOLAS%20A%20CORDOBA%20CAPITAL&pCodigoParada=&pProveedor=yv'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        selectorItems = 'ul.servicios'
        data = response.css(selectorItems)

        horarios = data.css('div.salida')

        detalleHorario = []

        
        for horario in horarios:
            labels = horario.css('label::text')
            detalleHorario.append(labels.extract())

        yield {
            'data' : detalleHorario
        }
        