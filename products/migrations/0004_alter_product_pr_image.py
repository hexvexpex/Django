# Generated by Django 4.1.4 on 2023-01-01 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_pr_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pr_image',
            field=models.ImageField(blank=True, null=True, upload_to='mediafiles/'),
        ),
    ]
