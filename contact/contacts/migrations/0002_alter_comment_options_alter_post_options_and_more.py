# Generated by Django 4.1.5 on 2023-03-02 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['pub_date'], 'verbose_name': 'Коммент', 'verbose_name_plural': 'Комменты'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['public_data'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AddField(
            model_name='cuser',
            name='images',
            field=models.ManyToManyField(to='contacts.images', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='cuser',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cuser',
            name='city',
            field=models.CharField(blank=True, max_length=255, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='cuser',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='cuser',
            name='face',
            field=models.ImageField(blank=True, null=True, upload_to='faces/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='cuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', 'Мужчина'), ('m', 'Женщина'), ('other', 'Другой')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='cuser',
            name='interes',
            field=models.TextField(blank=True, null=True, verbose_name='Интересы'),
        ),
    ]
