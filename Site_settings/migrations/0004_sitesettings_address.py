# Generated by Django 3.2.4 on 2021-06-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_settings', '0003_auto_20210616_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='Address',
            field=models.CharField(blank=True, max_length=999, null=True, verbose_name='Your Address '),
        ),
    ]
