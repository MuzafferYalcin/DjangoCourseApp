# Generated by Django 4.2.2 on 2023-08-12 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_category_alter_course_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]