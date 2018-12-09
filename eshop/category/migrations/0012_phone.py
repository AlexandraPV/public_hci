# Generated by Django 2.1.3 on 2018-12-09 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0011_laptop_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255, verbose_name='Модель телефона')),
                ('brand', models.CharField(default='Apple', max_length=255, verbose_name='Бренд ')),
                ('oper_system', models.CharField(choices=[('mac', 'MacOS'), ('linux', 'Linux'), ('windows', 'Windows')], max_length=255, verbose_name='Операционная система')),
                ('oper_memory', models.IntegerField(default=16, verbose_name='ОЗУ')),
                ('count_core', models.IntegerField(default=8, verbose_name='Количество ядер')),
                ('price', models.IntegerField(default='2000', verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка')),
                ('desc', models.TextField(default='no desc', max_length=500, verbose_name='Описание ')),
                ('category', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
            ],
        ),
    ]