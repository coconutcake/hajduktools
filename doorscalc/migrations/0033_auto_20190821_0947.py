# Generated by Django 2.1.11 on 2019-08-21 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doorscalc', '0032_auto_20190821_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='nosna',
            field=models.CharField(choices=[('int(w)*int(h)+int(h)*int(d)', 'Cała narożna'), ('int(w)*int(h)', 'Cała frontowa'), ('int(w)*int(h)/2', 'Połowa frontowej')], help_text='Wybierz szybe nośną', max_length=50, null=True, verbose_name='Skrzydło nośne'),
        ),
    ]
