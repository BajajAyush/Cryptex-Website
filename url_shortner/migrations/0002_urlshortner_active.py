# Generated by Django 4.0.7 on 2022-09-04 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshortner',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
