# Generated by Django 2.2.13 on 2020-10-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhonespiderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_title', models.CharField(max_length=200)),
                ('comment_id', models.IntegerField()),
                ('comment_date', models.DateField()),
                ('comment_description', models.TextField()),
                ('comment_sentiments', models.FloatField()),
            ],
        ),
    ]
