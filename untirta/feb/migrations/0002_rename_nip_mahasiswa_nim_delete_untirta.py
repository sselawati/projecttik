# Generated by Django 4.1.1 on 2022-10-10 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mahasiswa',
            old_name='NIP',
            new_name='NIM',
        ),
        migrations.DeleteModel(
            name='untirta',
        ),
    ]
