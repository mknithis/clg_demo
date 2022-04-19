# Generated by Django 3.0.7 on 2022-04-07 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pis_com', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('person', models.CharField(blank=True, default='customer', max_length=200, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('payment', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('payment_type', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('dated', models.DateField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_ledger', to='pis_com.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
