# Generated by Django 2.2.4 on 2019-08-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doorscalc', '0023_auto_20190820_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='nosna',
            field=models.CharField(choices=[('int(w)*int(h)+int(h)*int(d)', 'int(w)*int(h)+int(h)*int(d)'), ('int(w)*int(h)', 'int(w)*int(h)')], help_text='Wybierz szybe nośną', max_length=50, null=True),
        ),
    ]
