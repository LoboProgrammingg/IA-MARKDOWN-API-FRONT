# Generated by Django 5.2.3 on 2025-06-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_dashboarddata_alter_chatmessage_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='feedback',
            field=models.IntegerField(
                choices=[(1, 'Gostei'), (-1, 'Não Gostei'), (0, 'Nenhum')],
                default=0,
            ),
        ),
    ]
