# Generated by Django 4.0.2 on 2022-03-11 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_card', '0002_item_card_img_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_num', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
    ]
