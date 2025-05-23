# Generated by Django 5.1.3 on 2024-12-19 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Designer', '0003_delete_tbl_work'),
        ('Guest', '0006_tbl_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=30)),
                ('work_details', models.CharField(max_length=30)),
                ('work_photo', models.FileField(max_length=30, upload_to='')),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_designer')),
            ],
        ),
    ]
