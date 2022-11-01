# Generated by Django 4.1.1 on 2022-10-05 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='untirta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feb.dosen')),
                ('Mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feb.mahasiswa')),
                ('Staf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feb.staf')),
            ],
        ),
    ]
