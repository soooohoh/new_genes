# Generated by Django 2.2 on 2023-05-22 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gene', '0013_user_fat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_fat',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gene.Gene'),
        ),
    ]