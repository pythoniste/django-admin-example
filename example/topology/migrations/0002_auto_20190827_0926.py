# Generated by Django 2.2.4 on 2019-08-27 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topology', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='theme',
            options={'ordering': ('label',), 'verbose_name': 'theme', 'verbose_name_plural': 'theme_set'},
        ),
        migrations.RemoveField(
            model_name='test',
            name='themes',
        ),
        migrations.RemoveField(
            model_name='test',
            name='themes2',
        ),
        migrations.RemoveField(
            model_name='test',
            name='themes3',
        ),
        migrations.RemoveField(
            model_name='test',
            name='themes4',
        ),
        migrations.RemoveField(
            model_name='test',
            name='themes5',
        ),
        migrations.RemoveField(
            model_name='test',
            name='themes6',
        ),
        migrations.AddField(
            model_name='test',
            name='theme_set',
            field=models.ManyToManyField(blank=True, related_name='test_set', to='topology.Theme', verbose_name='theme_set'),
        ),
        migrations.AddField(
            model_name='test',
            name='theme_set2',
            field=models.ManyToManyField(blank=True, related_name='test2_set', to='topology.Theme', verbose_name='theme_set 2'),
        ),
        migrations.AddField(
            model_name='test',
            name='theme_set3',
            field=models.ManyToManyField(blank=True, related_name='test3_set', to='topology.Theme', verbose_name='theme_set 3'),
        ),
        migrations.AddField(
            model_name='test',
            name='theme_set4',
            field=models.ManyToManyField(blank=True, related_name='test4_set', to='topology.Theme', verbose_name='theme_set 4'),
        ),
        migrations.AddField(
            model_name='test',
            name='theme_set5',
            field=models.ManyToManyField(blank=True, related_name='test5_set', to='topology.Theme', verbose_name='theme_set 5'),
        ),
        migrations.AddField(
            model_name='test',
            name='theme_set6',
            field=models.ManyToManyField(blank=True, related_name='test6_set', to='topology.Theme', verbose_name='theme_set 6'),
        ),
        migrations.AlterField(
            model_name='test',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='test_set', to='topology.Category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='test',
            name='category2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test2_set', to='topology.Category', verbose_name='category 2'),
        ),
        migrations.AlterField(
            model_name='test',
            name='category3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test3_set', to='topology.Category', verbose_name='category 3'),
        ),
        migrations.AlterField(
            model_name='test',
            name='category4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test4_set', to='topology.Category', verbose_name='category 4'),
        ),
        migrations.AlterField(
            model_name='test',
            name='category5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test5_set', to='topology.Category', verbose_name='category 5'),
        ),
        migrations.AlterField(
            model_name='test',
            name='category6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test6_set', to='topology.Category', verbose_name='category 6'),
        ),
        migrations.AlterField(
            model_name='test',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tag_set', through='topology.Mapping', to='topology.Tag', verbose_name='theme_set'),
        ),
    ]
