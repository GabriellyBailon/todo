from rest_framework import viewsets
from acoes.api import serializers
from acoes import models

class AcoesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AcoesSerializer
    queryset = models.AcaoModel.objects.all()