# Generated by Django 5.1.5 on 2025-03-18 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takim', '0008_remove_yarislar_zaman1_alter_yarislar_zaman'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yarislar',
            name='zaman',
            field=models.DateTimeField(max_length=30),
        ),
    ]
