# Generated by Django 4.2.5 on 2023-09-08 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.FloatField(max_length=100.0)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='test.test')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
