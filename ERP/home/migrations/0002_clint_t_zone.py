# Generated by Django 4.1.1 on 2022-09-30 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clint',
            name='T_ZONE',
            field=models.TextField(blank=True, max_length=25, null=True),
        ),
    ]
