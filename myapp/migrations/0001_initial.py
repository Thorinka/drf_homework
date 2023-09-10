# Generated by Django 4.2.4 on 2023-09-09 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='app/course/', verbose_name='превью')),
                ('description', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='app/course/', verbose_name='превью')),
                ('description', models.TextField(verbose_name='описание')),
                ('video', models.CharField(max_length=300, verbose_name='ссылка на видео')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')),
                ('amount', models.IntegerField(verbose_name='сумма')),
                ('method', models.CharField(choices=[('transaction', 'Перевод на счёт'), ('cash', 'Наличные')], default='transaction', max_length=20, verbose_name='метод оплаты')),
                ('paid_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.course', verbose_name='курс')),
                ('paid_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.lesson', verbose_name='урок')),
            ],
        ),
    ]
