import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "cba-cp"

    def start_requests(self):
        url = 'http://mibondiya.cba.gov.ar/Datos.aspx?pCodigoEmpresa=401&pCodigoLinea=1&pCodigoOrigen=1&pCodigoDestino=2&pServicio=CORDOBA%20CAPITAL%20A%20VILLA%20CARLOS%20PAZ&pCodigoParada=0101&pProveedor=yv'
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
        