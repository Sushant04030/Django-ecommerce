# Generated by Django 4.1.1 on 2022-10-20 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='qrimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=200, unique=True)),
                ('image', models.ImageField(upload_to='static/images')),
            ],
        ),
    ]
