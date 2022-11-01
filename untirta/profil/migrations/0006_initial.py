# Generated by Django 4.1.1 on 2022-10-10 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profil', '0005_delete_dosen_delete_mahasiswa_delete_staf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dosen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIP', models.CharField(max_length=9)),
                ('Nama', models.CharField(max_length=9)),
                ('Tanggal_Lahir', models.CharField(max_length=9)),
                ('Photo', models.CharField(max_length=9)),
                ('Email', models.CharField(max_length=9)),
                ('Fakultas', models.CharField(max_length=9)),
                ('Prodi', models.CharField(max_length=9)),
                ('Alamat_Rumah', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIM', models.CharField(max_length=9)),
                ('Nama', models.CharField(max_length=9)),
                ('Tanggal_Lahir', models.CharField(max_length=9)),
                ('Photo', models.CharField(max_length=9)),
                ('Email', models.CharField(max_length=9)),
                ('Fakultas', models.CharField(max_length=9)),
                ('Prodi', models.CharField(max_length=9)),
                ('Alamat_Rumah', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Staf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIP', models.CharField(max_length=9)),
                ('Nama', models.CharField(max_length=9)),
                ('Tanggal_Lahir', models.CharField(max_length=9)),
                ('Photo', models.CharField(max_length=9)),
                ('Email', models.CharField(max_length=9)),
                ('Unit', models.CharField(max_length=9)),
                ('Alamat_Rumah', models.CharField(max_length=9)),
            ],
        ),
    ]
