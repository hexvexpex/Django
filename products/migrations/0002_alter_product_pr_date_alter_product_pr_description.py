# Generated by Django 4.1.4 on 2022-12-30 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pr_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='pr_description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
