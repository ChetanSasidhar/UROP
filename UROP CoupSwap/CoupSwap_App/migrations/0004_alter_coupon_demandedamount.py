# Generated by Django 4.2.3 on 2023-08-10 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoupSwap_App', '0003_coupon_demandedamount_user_cash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='demandedamount',
            field=models.IntegerField(default=0, verbose_name='Demanded Amount'),
        ),
    ]
