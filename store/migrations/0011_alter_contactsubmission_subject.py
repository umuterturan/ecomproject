# Generated by Django 4.2.11 on 2024-03-10 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_contactsubmission_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactsubmission',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]
