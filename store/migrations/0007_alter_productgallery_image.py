# Generated by Django 3.2.5 on 2021-10-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20211004_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgallery',
            name='image',
            field=models.ImageField(max_length=255, upload_to='static/images/product_gallery'),
        ),
    ]
