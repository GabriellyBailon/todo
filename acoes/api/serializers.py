from rest_framework import serializers
from acoes import models

class AcoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AcaoModel
        fields = '__all__'