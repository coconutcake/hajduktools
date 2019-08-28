# Generated by Django 2.2.3 on 2019-08-28 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doorscalc', '0038_auto_20190828_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='handle_site',
            field=models.CharField(blank=True, choices=[('Right', 'Right'), ('Left', 'Left'), ('Top', 'Top'), ('Bottom', 'Bottom')], help_text='Strona klamki', max_length=50, null=True, verbose_name='Handle'),
        ),
    ]
