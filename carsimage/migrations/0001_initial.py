# Generated by Django 3.2 on 2022-12-22 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoGenFeaturedImageWhitelist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_image', models.CharField(max_length=255, unique=True)),
                ('whitelist_urls', models.TextField()),
            ],
        ),
    ]