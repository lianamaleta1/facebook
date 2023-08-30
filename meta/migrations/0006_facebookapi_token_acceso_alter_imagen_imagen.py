# Generated by Django 4.2.3 on 2023-08-24 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0005_remove_publicacion_cuentafac'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebookapi',
            name='token_acceso',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='imagen',
            field=models.ImageField(upload_to='media/'),
        ),
    ]