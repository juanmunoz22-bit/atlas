from django.db import models

# Create your models here.

class File_Header(models.Model):
    """
    File_Header part
    """

    tipo_documento = models.CharField(max_length=2, null=False)
    numero_documento = models.IntegerField(null=False)
    razon_social = models.CharField(max_length=100, null=False)
    referencia = models.IntegerField(null=False)
    solicitud = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.tipo_documento + '-' + str(self.numero_documento)

class File_Fixed(models.Model):
    '''
    File Fixed part
    '''
    tipo_documento = models.CharField(max_length=2, null=False)
    numero_documento = models.IntegerField(null=False)
    nombre_cotizante = models.CharField(max_length=100, null=True)
    cargo = models.CharField(max_length=100, null=True)
    anio = models.IntegerField(null=False)
    mes = models.IntegerField(null=False)
    salario = models.IntegerField(null=True)
    dias_trab = models.IntegerField(null=True)
    dias_incap = models.IntegerField(null=True)
    dias_licen = models.IntegerField(null=True)
    f_ingreso = models.DateField(null=True)