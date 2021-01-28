from django.db import models
from django.contrib.auth.models import User

#Este modelo es la base para otros modelos usados en otras aplicaciones
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    modificador = models.IntegerField(blank=True, null=True)

    class Meta:
    #Le indicamos que no haga migraciones de este modelo
        abstract = True