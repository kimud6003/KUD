# Generated by Django 4.0.3 on 2022-05-18 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0003_remove_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
