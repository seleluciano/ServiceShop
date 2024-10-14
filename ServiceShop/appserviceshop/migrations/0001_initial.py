<<<<<<< HEAD
# Generated by Django 5.1.1 on 2024-10-14 22:53
=======
# Generated by Django 5.1.2 on 2024-10-14 22:26
>>>>>>> origin/sosa5

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
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('categoria', models.CharField(choices=[('Tecnologia', 'Tecnología'), ('Educacion', 'Educación'), ('Salud', 'Salud'), ('Alimentacion', 'Alimentación')], max_length=20)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('zona', models.CharField(choices=[('Norte', 'Norte'), ('Sur', 'Sur'), ('Este', 'Este'), ('Oeste', 'Oeste')], max_length=20)),
                ('descripcion', models.TextField()),
                ('disponibilidadhoraria', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='imgservices/')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('actualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
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
            name='CarritoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appserviceshop.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appserviceshop.producto')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='productos',
            field=models.ManyToManyField(through='appserviceshop.CarritoProducto', to='appserviceshop.producto'),
        ),
        migrations.CreateModel(
            name='Compras_M',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('fecha_compra', models.DateTimeField(auto_now_add=True)),
                ('comprador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('servicio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appserviceshop.servicio')),
=======
                ('fecha_venta', models.DateTimeField(auto_now_add=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(choices=[('completada', 'Completada'), ('cancelada', 'Cancelada')], max_length=50)),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appserviceshop.servicio')),
>>>>>>> origin/sosa5
            ],
        ),
        migrations.CreateModel(
            name='Ventas_M',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_venta', models.DateTimeField(auto_now_add=True)),
                ('servicio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appserviceshop.servicio')),
                ('vendedor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
