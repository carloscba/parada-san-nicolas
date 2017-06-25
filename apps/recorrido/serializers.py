from rest_framework import serializers
from .models import Recorrido

class RecorridoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recorrido
        fields = ('nombre', 'url','endpoint',)