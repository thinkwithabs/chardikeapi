# Generated by Django 4.0.4 on 2022-06-09 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_categories_category_name_alter_countreies_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('slidername', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('status', models.BooleanField(default=False)),
                ('position', models.PositiveIntegerField()),
                ('home_shown', models.BooleanField(default=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_slider', to='products.categories', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Sliders',
            },
        ),
    ]
