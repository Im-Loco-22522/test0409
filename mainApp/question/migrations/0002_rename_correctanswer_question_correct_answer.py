# Generated by Django 4.2.5 on 2023-09-09 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='correctAnswer',
            new_name='correct_answer',
        ),
    ]
