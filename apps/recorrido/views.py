from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RecorridoSerializer
from .models import Recorrido

class RecorridoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Recorrido.objects.all()
    serializer_class = RecorridoSerializer