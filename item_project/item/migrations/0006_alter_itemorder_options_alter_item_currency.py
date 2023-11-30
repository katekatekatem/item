# Generated by Django 4.2.7 on 2023-11-30 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_alter_item_currency'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemorder',
            options={'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[(1, 'rub'), (2, 'dol')], max_length=3),
        ),
    ]