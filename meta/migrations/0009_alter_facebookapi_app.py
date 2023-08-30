# Generated by Django 4.2.3 on 2023-08-24 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        ('meta', '0008_facebookapi_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebookapi',
            name='app',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, to='socialaccount.socialapp'),
        ),
    ]
