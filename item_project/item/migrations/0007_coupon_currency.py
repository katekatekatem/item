# Generated by Django 4.2.7 on 2023-12-01 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_alter_coupon_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='currency',
            field=models.CharField(choices=[('rub', 'rubles'), ('usd', 'dollars')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
