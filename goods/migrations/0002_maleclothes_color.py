# Generated by Django 5.0.6 on 2024-06-16 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maleclothes',
            name='color',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
