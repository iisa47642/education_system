# Generated by Django 4.2.8 on 2024-11-15 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_typeoflesson_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='typeoflesson',
            options={'verbose_name': 'Тип занятия', 'verbose_name_plural': 'Тип занятий'},
        ),
        migrations.AlterModelTable(
            name='lessonlocation',
            table='lessonlocation',
        ),
        migrations.AlterModelTable(
            name='subject',
            table='subject',
        ),
        migrations.AlterModelTable(
            name='typeoflesson',
            table='typeoflesson',
        ),
    ]
