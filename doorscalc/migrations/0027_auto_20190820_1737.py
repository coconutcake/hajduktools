# Generated by Django 2.2.4 on 2019-08-20 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doorscalc', '0026_auto_20190820_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='nosna',
            field=models.CharField(choices=[('int(w)*int(h)+int(h)*int(d)', 'Tylko frontowa w narożnych i trójstronnych'), ('int(w)*int(h)', 'Cała')], help_text='Wybierz szybe nośną', max_length=50, null=True),
        ),
    ]
