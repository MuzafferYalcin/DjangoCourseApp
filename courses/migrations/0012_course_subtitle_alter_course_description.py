# Generated by Django 4.2.2 on 2023-09-12 09:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_alter_course_options_remove_course_imageurl_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='subtitle',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]