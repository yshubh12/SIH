# Generated by Django 5.0.2 on 2024-09-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_featuredproduct_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredproduct',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
