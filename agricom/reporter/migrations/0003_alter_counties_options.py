# Generated by Django 4.0.1 on 2022-03-09 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0002_counties'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='counties',
            options={'verbose_name_plural': 'Counties'},
        ),
    ]
