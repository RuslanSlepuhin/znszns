# Generated by Django 4.0.5 on 2022-06-15 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zns_project', '0004_alter_contacts_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='first_name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='contacts',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='text_text',
            field=models.TextField(blank=True),
        ),
    ]