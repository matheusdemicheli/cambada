from django.db import models

# Create your models here.
class FraseHistorica(models.Model):
    """
    Model para as Frases Historicas.
    """
    autor = models.TextField()
    data = models.TextField()
    texto = models.TextField()
