# Generated by Django 2.2 on 2020-09-14 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catatan', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pinjam',
            new_name='Catatan',
        ),
    ]