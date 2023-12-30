# Generated by Django 4.1.13 on 2023-12-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='AmazonReview',
        ),
    ]