# Generated by Django 5.0.3 on 2024-03-08 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_contactsubmission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
