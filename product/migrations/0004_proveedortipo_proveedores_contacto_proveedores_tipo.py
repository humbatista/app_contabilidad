# Generated by Django 4.0.2 on 2022-09-01 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_proveedores_direccion_proveedores_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProveedorTipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='proveedores',
            name='contacto',
            field=models.CharField(default='Jose Perez', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proveedores',
            name='tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.proveedortipo'),
            preserve_default=False,
        ),
    ]