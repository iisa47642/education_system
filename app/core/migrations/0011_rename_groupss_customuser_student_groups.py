# Generated by Django 4.2.8 on 2024-11-19 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_customuser_role_customuser_groupss_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='groupss',
            new_name='student_groups',
        ),
    ]