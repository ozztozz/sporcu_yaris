# Generated by Django 5.1.5 on 2025-03-18 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takim', '0004_alter_yarislar_tarih'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yarislar',
            name='zaman',
            field=models.TimeField(max_length=100),
        ),
    ]
