# Generated by Django 4.0.2 on 2022-03-16 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_card', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(default='', null=True, upload_to='customers/'),
        ),
    ]
