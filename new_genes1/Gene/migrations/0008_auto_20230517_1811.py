# Generated by Django 2.2 on 2023-05-17 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gene', '0007_diary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='diary_image',
            field=models.ImageField(upload_to='diary_pics'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='diary_image2',
            field=models.ImageField(blank=True, upload_to='diary_pics'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='diary_image3',
            field=models.ImageField(blank=True, upload_to='diary_pics'),
        ),
    ]
