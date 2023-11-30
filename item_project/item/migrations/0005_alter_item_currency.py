# Generated by Django 4.2.7 on 2023-11-30 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_item_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('rub', 'rubles'), ('usd', 'dollars')], max_length=3),
        ),
    ]