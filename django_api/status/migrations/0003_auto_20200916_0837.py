# Generated by Django 3.1.1 on 2020-09-16 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_auto_20200916_0658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='contect',
            new_name='content',
        ),
    ]