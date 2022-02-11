# Generated by Django 4.0.2 on 2022-02-11 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('conteudo', models.TextField()),
                ('excerto', models.TextField()),
                ('imagem', models.ImageField(upload_to='fotos_dos_posts/Y%/m%')),
                ('publicado', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(blank=True, null=None, on_delete=django.db.models.deletion.DO_NOTHING, to='categoria.categoria')),
            ],
        ),
    ]