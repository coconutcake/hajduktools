# Generated by Django 2.2.4 on 2019-08-20 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doorscalc', '0021_auto_20190820_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='nosna',
            field=models.CharField(choices=[('int(x)*int(h)+int(h)*int(d)', 'int(x)*int(y)+int(h)*int(d)'), ('int(x)*int(h)', 'int(x)*int(y)')], help_text='Wybierz szybe nośną', max_length=50, null=True),
        ),
    ]
