# Generated by Django 5.0 on 2024-05-29 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_cartitems_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='color_variant',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='size_variant',
        ),
    ]
