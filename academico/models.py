from django.db import models

# Create your models here.
class curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=55)
    creditos = models.PositiveBigIntegerField()
    
    
    def __str__(self) -> str:
        return f"{self.nombre} ({self.creditos})"
