# Generated by Django 2.0.2 on 2018-03-05 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='opencorps',
            name='officers',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]