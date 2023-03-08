# Generated by Django 4.1.4 on 2023-03-08 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qoyliq_app', '0003_remove_orderitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='qoyliq_app.product', verbose_name='Tovar'),
            preserve_default=False,
        ),
    ]
