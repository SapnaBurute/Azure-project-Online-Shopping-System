# Generated by Django 4.0.2 on 2022-03-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_card', '0003_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_card',
            name='price',
            field=models.FloatField(default=200, null=True),
        ),
    ]
