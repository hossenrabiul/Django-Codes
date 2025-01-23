# Generated by Django 5.1.4 on 2025-01-19 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booksdetails',
            name='user_reviews',
        ),
        migrations.AlterField(
            model_name='booksdetails',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='books/media/uploads'),
        ),
    ]
