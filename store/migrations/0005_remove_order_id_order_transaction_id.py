# Generated by Django 4.0 on 2022-01-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_order_transaction_id_alter_orderitem_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(blank=True, editable=False, max_length=200, primary_key=True, serialize=False),
        ),
    ]
