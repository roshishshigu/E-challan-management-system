# Generated by Django 3.1.7 on 2021-05-07 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Collab_Project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challan',
            name='createdby',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='challan',
            name='lisencenumber',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='challan',
            name='place',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='challan',
            name='vehiclenumber',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='challan',
            name='vehicletype',
            field=models.CharField(max_length=30),
        ),
    ]
