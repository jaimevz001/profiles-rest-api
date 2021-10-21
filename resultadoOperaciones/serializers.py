from rest_framework import serializers

from resultadoOperaciones import models


class resultadoOperacionesSerializer(serializers.Serializer):
    certComercioProveedor = serializers.CharField(max_length=20)
    celularCliente = serializers.CharField(max_length=10)
    digitoVerificadorCliente = serializers.IntegerField()
    nombreCliente = serializers.CharField(max_length=40)
    claveInstitucionCliente = serializers.IntegerField()
    tipoCuentaCliente = serializers.IntegerField()
    numeroCuentaCliente = serializers.CharField(max_length=20)
    idMensajeCobro = serializers.CharField(max_length=20)
    concepto = serializers.CharField(max_length=40)
    monto = serializers.IntegerField()
    claveRastreo = serializers.CharField(max_length=30)
    resultadoMensajeCobro = serializers.IntegerField()
    horaSolicitudMensajeCobro = serializers.IntegerField()
    horaProcMensajeCobro = serializers.IntegerField()
    certBdeM = serializers.CharField(max_length=20)
    horaEnvioMensaje = serializers.IntegerField()

    def create(self, validated_data):
        """
        Crear y regresar una instancia del resultado, dados los datos validados.
        """
        return resultado.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Actualizando y regeresando una instancia de los resultados
        """
        instance.certComercioProveedor = validated_data.get(
            'certComercioProveedor', instance.certComercioProveedor)
        instance.celularCliente = validated_data.get(
            'celularCliente', instance.celularCliente)
        instance.digitoVerificadorCliente = validated_data.get(
            'digitoVerificadorCliente', instance.digitoVerificadorCliente)
        instance.nombreCliente = validated_data.get(
            'nombreCliente', instance.nombreCliente)
        instance.claveInstitucionCliente = validated_data.get(
            'claveInstitucionCliente', instance.claveInstitucionCliente)
        instance.tipoCuentaCliente = validated_data.get(
            'tipoCuentaCliente', instance.tipoCuentaCliente)
        instance.numeroCuentaCliente = validated_data.get(
            'numeroCuentaCliente', instance.numeroCuentaCliente)
        instance.idMensajeCobro = validated_data.get(
            'idMensajeCobro', instance.idMensajeCobro)
        instance.concepto = validated_data.get(
            'concepto', instance.concepto)
        instance.monto = validated_data.get(
            'monto', instance.monto)
        instance.claveRastreo = validated_data.get(
            'claveRastreo', instance.claveRastreo)
        instance.resultadoMensajeCobro = validated_data.get(
            'resultadoMensajeCobro', instance.resultadoMensajeCobro)
        instance.horaSolicitudMensajeCobro = validated_data.get(
            'horaSolicitudMensajeCobro', instance.horaSolicitudMensajeCobro)
        instance.horaProcMensajeCobro = validated_data.get(
            'horaProcMensajeCobro', instance.horaProcMensajeCobro)
        instance.certBdeM = validated_data.get(
            'certBdeM', instance.certBdeM)
        instance.horaEnvioMensaje = validated_data.get(
            'horaEnvioMensaje', instance.horaEnvioMensaje)
        return instance
