# Generated by Django 5.0.6 on 2024-06-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_maleclothes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maleclothes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='male_clothes/'),
        ),
    ]
