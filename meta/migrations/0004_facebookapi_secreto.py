# Generated by Django 4.2.3 on 2023-07-28 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0003_remove_facebookapi_apikey_remove_facebookapi_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebookapi',
            name='secreto',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
