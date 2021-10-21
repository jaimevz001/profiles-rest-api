from django.db import models

# Create your models here.


class resultadoOperaciones(models.Model):
    """
    Modelo de la Base de Datos del resultado de las solicitudes de Mensajes de
    Cobro
    """

    certComercioProveedor = models.CharField(max_length=20)
    celularCliente = models.CharField(max_length=10)
    digitoVerificadorCliente = models.IntegerField()
    nombreCliente = models.CharField(max_length=40)
    claveInstitucionCliente = models.IntegerField()
    tipoCuentaCliente = models.IntegerField()
    numeroCuentaCliente = models.CharField(max_length=20)
    idMensajeCobro = models.CharField(max_length=20)
    concepto = models.CharField(max_length=40)
    monto = models.IntegerField()
    claveRastreo = models.CharField(max_length=30)
    resultadoMensajeCobro = models.IntegerField()
    horaSolicitudMensajeCobro = models.IntegerField()
    horaProcMensajeCobro = models.IntegerField()
    certBdeM = models.CharField(max_length=20)
    horaEnvioMensaje = models.IntegerField()
#    return resultado
