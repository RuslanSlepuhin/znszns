# Generated by Django 4.0.5 on 2022-06-15 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zns_project', '0003_alter_contacts_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='last_name',
            field=models.TextField(blank=True),
        ),
    ]
