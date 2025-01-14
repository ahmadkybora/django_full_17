# Generated by Django 4.2.11 on 2024-04-08 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='price')),
                ('image', models.ImageField(blank=True, upload_to='products/', verbose_name='image')),
                ('qty', models.IntegerField(verbose_name='qty')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated_time')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='categories.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
            },
        ),
    ]
