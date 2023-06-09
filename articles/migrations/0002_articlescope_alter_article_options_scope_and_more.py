# Generated by Django 4.2.1 on 2023-05-08 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleScope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False, verbose_name='основной')),
            ],
            options={
                'verbose_name': 'тэг',
                'verbose_name_plural': 'тэги',
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Тематический раздел')),
                ('articles', models.ManyToManyField(through='articles.ArticleScope', to='articles.article')),
            ],
            options={
                'verbose_name': 'тематический раздел',
                'verbose_name_plural': 'разделы',
            },
        ),
        migrations.AddField(
            model_name='articlescope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
        migrations.AddField(
            model_name='articlescope',
            name='scope',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.scope'),
        ),
        migrations.AlterUniqueTogether(
            name='articlescope',
            unique_together={('article', 'scope')},
        ),
    ]
