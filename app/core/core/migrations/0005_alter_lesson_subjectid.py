# Generated by Django 4.2.8 on 2024-11-17 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_lesson_subjectid_alter_lesson_teacherid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='subjectId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subject'),
        ),
    ]
