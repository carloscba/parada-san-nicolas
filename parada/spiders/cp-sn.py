import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "cp-sn"

    def start_requests(self):
        url = 'http://mibondiya.cba.gov.ar/Datos.aspx?pCodigoEmpresa=401&pCodigoLinea=24&pCodigoOrigen=2&pCodigoDestino=124&pServicio=VILLA%20CARLOS%20PAZ%20A%20SAN%20NICOLAS&pCodigoParada=&pProveedor=yv'
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
        