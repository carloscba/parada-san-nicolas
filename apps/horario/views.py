from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import HorarioSerializer

from ..recorrido.models import Recorrido

import urllib2
from bs4 import BeautifulSoup

@api_view(['GET'])
def horario_list(request, pk, format=None):
    """
    Listado de proximos horarios
    """
    if request.method == 'GET':

        recorrido = Recorrido.objects.get(pk=pk)

        weburl = urllib2.urlopen(recorrido.url)

        if(weburl.getcode() == 200):

            data = weburl.read()
            soup = BeautifulSoup(data, 'html.parser')
            
            unidades = soup.find_all('li')
            
            horarios = []
            
            for unidad in unidades:

                salida =  unidad.find_all("div", "salida")        
                dataSalida = salida[0].find_all('label')

                llegada =  unidad.find_all("div", "llegada")    
                
                info =  unidad.find_all("div", "info")
                dataInfo= info[0].find_all('div')
                
                position =  unidad.find_all("a")
                
                horarios.append({
                    "arriba" : dataSalida[0].get_text().strip(),
                    "demora" : dataSalida[3].get_text().strip(),
                    "coche" : dataInfo[3].get_text().strip(),
                    "ubicacion" : position[0].get('href')
                })

        serializer = HorarioSerializer(horarios, many=True)
        return Response(serializer.data)

# Create your views here.
