from django.db import models
from django.utils import timezone


class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    cemail = models.EmailField(blank=True, default="")
    celular = models.IntegerField(default=8)
    fecha_reserva = models.DateTimeField(
            blank=True, null=False)
    text = models.TextField()

def publish(self):
    self.fecha_reserva = timezone.now()
    self.save()

def __str__(self):
    return self.title