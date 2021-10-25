# Generated by Django 2.2 on 2021-10-20 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='resultadoOperaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certComercioProveedor', models.CharField(max_length=20)),
                ('celularCliente', models.CharField(max_length=10)),
                ('digitoVerificadorCliente', models.IntegerField()),
                ('nombreCliente', models.CharField(max_length=40)),
                ('claveInstitucionCliente', models.IntegerField()),
                ('tipoCuentaCliente', models.IntegerField()),
                ('numeroCuentaCliente', models.CharField(max_length=20)),
                ('idMensajeCobro', models.CharField(max_length=20)),
                ('concepto', models.CharField(max_length=40)),
                ('monto', models.IntegerField()),
                ('claveRastreo', models.CharField(max_length=30)),
                ('resultadoMensajeCobro', models.IntegerField()),
                ('horaSolicitudMensajeCobro', models.IntegerField()),
                ('horaProcMensajeCobro', models.IntegerField()),
                ('certBdeM', models.CharField(max_length=20)),
                ('horaEnvioMensaje', models.IntegerField()),
            ],
        ),
    ]