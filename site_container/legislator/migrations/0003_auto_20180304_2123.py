# Generated by Django 2.0.2 on 2018-03-05 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislator', '0002_opencorps_officers'),
    ]

    operations = [
        migrations.AddField(
            model_name='opencorps',
            name='status',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='opencorps',
            name='inactive',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='opencorps',
            name='officers',
            field=models.TextField(null=True),
        ),
    ]