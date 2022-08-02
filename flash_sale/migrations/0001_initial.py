# Generated by Django 4.0.5 on 2022-07-31 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlashProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('flash_price', models.FloatField(blank=True, null=True)),
                ('flash_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flash_product', to='products.products', verbose_name='Select Prodcut')),
            ],
            options={
                'verbose_name_plural': 'Flash Products Add',
            },
        ),
        migrations.CreateModel(
            name='FlashSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Flash Sale Name')),
                ('discount', models.PositiveIntegerField(blank=True, null=True, verbose_name='Flash Discount')),
                ('start_time', models.DateTimeField(null=True, verbose_name='Start Time')),
                ('end_time', models.DateTimeField(null=True, verbose_name='End Time')),
                ('products', models.ManyToManyField(related_name='flash_products', through='flash_sale.FlashProducts', to='products.products')),
            ],
            options={
                'verbose_name_plural': 'Flash Deal',
            },
        ),
        migrations.AddField(
            model_name='flashproducts',
            name='flash_sale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sale', to='flash_sale.flashsale'),
        ),
    ]
