# Generated by Django 5.1.1 on 2024-11-20 01:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(default='imgavatar/predeterminado.jpg', upload_to='imgavatar')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Compras_M',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('carrito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appserviceshop.carrito')),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(default='Cliente', max_length=50)),
                ('average_rating', models.FloatField(default=0.0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_ratings', to=settings.AUTH_USER_MODEL)),
                ('rater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='given_ratings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reseña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('calificacion', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appserviceshop.compras_m')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('categoria', models.CharField(choices=[('Tecnologia', 'Tecnología'), ('Educacion', 'Educación'), ('Salud', 'Salud'), ('Alimentacion', 'Alimentación'), ('Servicios de Reparación y Mantenimiento', 'Servicios de Reparación y Mantenimiento'), ('Consultoría y Servicios Profesionales', 'Consultoría y Servicios Profesionales'), ('Belleza y Cuidado Personal', 'Belleza y Cuidado Personal'), ('Arte y Publicidad', 'Arte y Publicidad')], max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('zona', models.CharField(choices=[('Norte', 'Norte'), ('Sur', 'Sur'), ('Este', 'Este'), ('Oeste', 'Oeste')], max_length=20)),
                ('descripcion', models.TextField()),
                ('disponibilidadhoraria', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='imgservices/')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('actualizacion', models.DateTimeField(auto_now=True)),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicios', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='compras_m',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appserviceshop.servicio'),
        ),
        migrations.CreateModel(
            name='ServicioEnCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appserviceshop.carrito')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appserviceshop.servicio')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='servicios',
            field=models.ManyToManyField(through='appserviceshop.ServicioEnCarrito', to='appserviceshop.servicio'),
        ),
        migrations.CreateModel(
            name='Ventas_M',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fecha_venta', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('En curso', 'En curso'), ('Cancelado', 'Cancelado'), ('Completado', 'Completado')], default='En curso', max_length=20)),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('carrito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appserviceshop.carrito')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appserviceshop.servicio')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='compras_m',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compras', to='appserviceshop.ventas_m'),
        ),
    ]
