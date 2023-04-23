from django.db import models

# Create your models here.
class AcaoModel(models.Model):

    codigo = models.CharField(max_length=8)
    descricao = models.TextField()
    data = models.DateField(auto_now_add=True)
    open = models.FloatField()
    closed = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    volume = models.FloatField()

    def __str__(self):
        return self.codigo