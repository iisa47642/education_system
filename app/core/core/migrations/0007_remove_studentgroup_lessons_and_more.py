# Generated by Django 4.2.8 on 2024-11-18 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_additionalmaterials_controlwork_test_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentgroup',
            name='lessons',
        ),
        migrations.AlterModelTable(
            name='additionalmaterials',
            table='AdditionalMaterials',
        ),
    ]
