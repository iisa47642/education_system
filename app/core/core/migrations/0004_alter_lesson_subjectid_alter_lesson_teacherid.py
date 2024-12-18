# Generated by Django 4.2.8 on 2024-11-17 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_lesson_subjectid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='subjectId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='core.subject'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='teacherId',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
    ]
