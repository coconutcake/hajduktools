# Generated by Django 2.1.11 on 2019-08-14 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doorscalc', '0009_auto_20190814_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='door',
            name='photo',
        ),
    ]
