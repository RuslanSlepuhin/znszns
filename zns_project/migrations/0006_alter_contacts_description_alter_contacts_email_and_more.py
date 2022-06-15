# Generated by Django 4.0.5 on 2022-06-15 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zns_project', '0005_rename_first_name_contacts_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='description',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='last_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone_number',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='text_text',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='text_title',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
