from rest_framework import serializers

class HorarioSerializer(serializers.Serializer):
    
    arriba = serializers.CharField(required=True, allow_blank=False, max_length=255)
    demora = serializers.CharField(required=True, allow_blank=False, max_length=255)
    coche = serializers.CharField(required=True, allow_blank=False, max_length=255)
    ubicacion = serializers.CharField(required=True, allow_blank=False, max_length=255)