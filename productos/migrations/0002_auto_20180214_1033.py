# Generated by Django 2.0 on 2018-02-14 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='precio',
            field=models.FloatField(),
        ),
    ]
