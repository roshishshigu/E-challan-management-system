# Generated by Django 3.1.7 on 2021-05-10 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Collab_Project', '0007_auto_20210508_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('head', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
    ]