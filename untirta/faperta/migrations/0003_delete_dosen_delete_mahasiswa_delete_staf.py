# Generated by Django 4.1.1 on 2022-10-10 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faperta', '0002_rename_nip_mahasiswa_nim_delete_untirta'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dosen',
        ),
        migrations.DeleteModel(
            name='Mahasiswa',
        ),
        migrations.DeleteModel(
            name='Staf',
        ),
    ]
