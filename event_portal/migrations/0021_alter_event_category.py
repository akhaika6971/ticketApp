# Generated by Django 4.1.7 on 2023-03-11 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_portal', '0020_alter_event_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ManyToManyField(to='event_portal.category'),
        ),
    ]