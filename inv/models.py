
from re import T
from tabnanny import verbose
from django.db import models
from bases.models import ClaseModelo

# Create your models here.
class Categoria(ClaseModelo):
    """ modelo Categoría"""
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la categoría',
        unique=True
    )

    def __str__(self):
        """ Descripción del modelo categoria"""
        return '{}'.format(self.descripcion)

    def save(self):
        """ el valor de categoría lo guardamos en mayusculas"""
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        """ nombre en plural(Muchos) del modelo"""
        verbose_name_plural = "Categorias"

class SubCategoria(ClaseModelo):
    """ modelo SubCategoría"""
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text="Descripción de la categoria",        
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)

    def save(self):
        """ el valor de subcategoría lo guardamos en mayúsculas"""
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        """ nombre en plural(Muchos) del modelo"""
        verbose_name_plural = "Sub Categorias"
        unique_together = ('categoria','descripcion')

class Marca(ClaseModelo):
    """ modelo Marca"""
    descripcion = models.CharField(
        max_length=100,
        help_text="Descripción de la marca",
        unique=True
    )

    def __str__(self):
        """ descripción del modelo marca"""
        return '{}'.format(self.descripcion)

    def save(self):
        """ el valor de marca lo guardamos en mayusculas"""
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()

    class Meta:
        """ nombre en plural(Muchos) del modelo"""
        verbose_name_plural = "Marcas"

class UnidadMedida(ClaseModelo):
    """ modelo Unidad de Medida"""
    descripcion = models.CharField(
        max_length=100,
        help_text="Descripción de la Unidad de Medida",
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        """ el valor de Unidad de Medida lo guardamos en mayúsculas"""
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).save()
    class Meta:
        """ nombre en plural(Muchos) del modelo"""
        verbose_name_plural = "Unidades de Medida"

class Producto(ClaseModelo):
    """ modelo Producto"""
    codigo = models.CharField(
        max_length=20,
        unique=True
    )
    codigo_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True) 

    # llaves foraneas
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    def __str__(self):
        """ descripción de producto"""
        return '{}'.format(self.descripcion)

    def save(self):
        """ el valor de Producto lo guardamos en mayúsculas"""
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()
    class Meta:        
        """ nombre en plural(Muchos) del modelo"""
        verbose_name_plural = "Productos"
        unique_together = ('codigo', 'codigo_barra')
