# Generated by Django 3.1.2 on 2022-05-30 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220530_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(null=True, upload_to='imagenesUsuarios')),
            ],
        ),
        migrations.DeleteModel(
            name='Marca',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
