# Generated by Django 4.1.1 on 2022-10-01 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clint',
            name='T_ZONE',
            field=models.TextField(default='Null', max_length=25),
        ),
    ]
