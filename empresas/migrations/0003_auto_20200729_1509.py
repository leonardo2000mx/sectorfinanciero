# Generated by Django 3.0.8 on 2020-07-29 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_auto_20200708_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precioempresa',
            name='id_empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emp', to='empresas.Empresa'),
        ),
    ]
