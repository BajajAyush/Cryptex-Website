# Generated by Django 4.0.7 on 2022-09-05 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortner', '0002_urlshortner_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortner',
            name='content',
            field=models.TextField(blank=True, max_length=999999, null=True),
        ),
    ]