# Generated by Django 4.2.8 on 2024-11-17 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_lesson_teacherid_delete_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='subjectId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjectId', to='core.subject'),
        ),
    ]
