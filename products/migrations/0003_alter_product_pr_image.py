# Generated by Django 4.1.4 on 2023-01-01 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_pr_date_alter_product_pr_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pr_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
