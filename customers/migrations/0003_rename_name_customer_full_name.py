# Generated by Django 3.2.8 on 2021-12-14 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20211215_0127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Name',
            new_name='Full_Name',
        ),
    ]
