# Generated by Django 4.1.4 on 2023-03-08 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qoyliq_app', '0005_alter_orderitem_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='orderitem',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='qoyliq_app.order', verbose_name='Buyurtma'),
        ),
    ]
