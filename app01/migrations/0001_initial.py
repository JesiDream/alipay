# Generated by Django 2.1 on 2018-10-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('order_num', models.CharField(max_length=128)),
                ('status', models.IntegerField(choices=[(1, '未支付'), (2, '已支付')])),
            ],
        ),
    ]
