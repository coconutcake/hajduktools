# Generated by Django 2.1.11 on 2019-08-14 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doorscalc', '0010_remove_door_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='door',
            name='cover',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
