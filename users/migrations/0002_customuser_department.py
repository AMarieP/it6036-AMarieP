# Generated by Django 4.2.4 on 2023-08-17 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='department',
            field=models.CharField(default='agent', max_length=100),
            preserve_default=False,
        ),
    ]