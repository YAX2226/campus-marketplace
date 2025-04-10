# Generated by Django 5.2 on 2025-04-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('category', models.CharField(choices=[('Architecture', 'Architecture'), ('Engineering', 'Engineering'), ('Pharmacy', 'Pharmacy')], max_length=50)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
