# Generated by Django 4.1.4 on 2023-02-21 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='Cart',
            new_name='cart',
        ),
    ]
