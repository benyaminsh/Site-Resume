# Generated by Django 3.2.4 on 2021-06-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=999, verbose_name='Date ')),
                ('Title', models.CharField(max_length=999, verbose_name='Title ')),
                ('Description', models.TextField(verbose_name='Description ')),
            ],
        ),
    ]