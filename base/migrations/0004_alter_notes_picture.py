# Generated by Django 4.1.2 on 2022-10-21 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_notes_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='picture',
            field=models.ImageField(blank=True, default='media/body.jpg', null=True, upload_to='media'),
        ),
    ]