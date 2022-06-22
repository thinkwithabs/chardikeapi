# Generated by Django 4.0.4 on 2022-05-23 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('total', models.PositiveIntegerField()),
                ('complete', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('coupon_name', models.CharField(max_length=100, null=True, verbose_name='Coupon Name')),
                ('coupon_type', models.CharField(choices=[('Fixed Cart Discount', 'Fixed Cart Discount'), ('Parcentage Discount', 'Parcentage Discount')], default=None, max_length=20, null=True, verbose_name='Coupon Type')),
                ('coupon_amount', models.FloatField(default=0.0, null=True, verbose_name='Coupon Amount')),
                ('free_shipping', models.BooleanField(default=False, null=True, verbose_name='Free Shipping Allow ?')),
                ('expire_date', models.DateField(blank=True, null=True)),
                ('minimum_user', models.IntegerField(blank=True, default=0, null=True, verbose_name='Minimum Users')),
                ('minimum_sale', models.IntegerField(blank=True, null=True, verbose_name='Minimum Sale')),
                ('maximum_sale', models.IntegerField(blank=True, null=True, verbose_name='Maximum Sale')),
            ],
            options={
                'verbose_name_plural': 'Coupon',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('mobile', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=255)),
                ('total', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField()),
                ('order_status', models.CharField(choices=[('Order Received', 'Order Received'), ('Order Processing', 'Order Processing'), ('On the way', 'On the way'), ('Order Completed', 'Order Completed'), ('Order Canceled', 'Order Canceled')], default='Order Received', max_length=100)),
                ('payment_complete', models.BooleanField(blank=True, default=False, null=True)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.cart')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('subtotal', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.cart')),
                ('product', models.ManyToManyField(to='products.products')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]