# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Departamento(models.Model):
    nombredepartamento = models.CharField(db_column='NOMBREDEPARTAMENTO', max_length=15)  # Field name made lowercase.

    class Meta:
        db_table = 'departamento'

class Ciudad(models.Model):
    nombreciudad = models.CharField(db_column='NOMBRECIUDAD', max_length=15)  # Field name made lowercase.
    departamento_iddepartamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='departamento_IDDEPARTAMENTO')  # Field name made lowercase.

    class Meta:
        db_table = 'ciudad'

class Usuario(models.Model):
    pinusuario = models.CharField(db_column='PINUSUARIO', max_length=6)  # Field name made lowercase.
    nombreusuario = models.CharField(db_column='NOMBREUSUARIO', max_length=255)  # Field name made lowercase.
    correousuario = models.CharField(db_column='CORREOUSUARIO', max_length=255)  # Field name made lowercase.
    passwordusuario = models.CharField(db_column='PASSWORDUSUARIO', max_length=100)  # Field name made lowercase.
    celularusuario = models.BigIntegerField(db_column='CELULARUSUARIO')  # Field name made lowercase.
    rol = models.IntegerField(db_column='ROL')  # Field name made lowercase.
    ciudad_idciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_IDCIUDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'usuario'

class Canchas(models.Model):
    nombrecancha = models.CharField(db_column='NOMBRECANCHA', max_length=25)  # Field name made lowercase.
    telefonocancha = models.IntegerField(db_column='TELEFONOCANCHA')  # Field name made lowercase.
    diasdisponible = models.CharField(db_column='DIASDISPONIBLE', max_length=60)  # Field name made lowercase.
    horaabrir = models.TimeField(db_column='HORAABRIR')  # Field name made lowercase.
    horacerrar = models.TimeField(db_column='HORACERRAR')  # Field name made lowercase.
    ubicacion = models.CharField(db_column='UBICACION', max_length=50)  # Field name made lowercase.
    tarifa = models.IntegerField(db_column='TARIFA')  # Field name made lowercase.
    caracteristicas = models.CharField(db_column='CARACTERISTICAS', max_length=100)  # Field name made lowercase.
    ciudad_idciudad = models.ForeignKey('Ciudad', models.DO_NOTHING, db_column='ciudad_IDCIUDAD')  # Field name made lowercase.
    usuario_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_IDUSUARIO')  # Field name made lowercase.

    class Meta:
        db_table = 'canchas'

class Calificarcancha(models.Model):
    usuario_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_IDUSUARIO')  # Field name made lowercase.
    canchas_idcancha = models.ForeignKey('Canchas', models.DO_NOTHING, db_column='canchas_IDCANCHA')  # Field name made lowercase.
    estrellascancha = models.IntegerField(db_column='ESTRELLASCANCHA')  # Field name made lowercase.
    comentariocancha = models.CharField(db_column='COMENTARIOCANCHA', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'calificarcancha'

class Calificarusuario(models.Model):
    #usuario_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_IDUSUARIO')  # Field name made lowercase.
    usuario_idusuariocalif = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_IDUSUARIOCALIF')  # Field name made lowercase.
    estrellasusuario = models.IntegerField(db_column='ESTRELLASUSUARIO')  # Field name made lowercase.
    comentariousuario = models.CharField(db_column='COMENTARIOUSUARIO', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'calificarusuario'

class Feedback(models.Model):
    correofeed = models.CharField(db_column='CORREOFEED', max_length=50)  # Field name made lowercase.
    mensajefeed = models.CharField(db_column='MENSAJEFEED', max_length=200)  # Field name made lowercase.

    class Meta:
        db_table = 'feedback'

class Imagen(models.Model):
    nombreimagen = models.CharField(db_column='NOMBREIMAGEN', max_length=52)  # Field name made lowercase.
    imagenpath = models.CharField(db_column='IMAGENPATH', max_length=1024)  # Field name made lowercase.
    canchas_idcancha = models.ForeignKey(Canchas, models.DO_NOTHING, db_column='canchas_IDCANCHA')  # Field name made lowercase.

    class Meta:
        db_table = 'imagen'

class Imagenverif(models.Model):
    nombreimagenverif = models.CharField(db_column='NOMBREIMAGENVERIF', max_length=52)  # Field name made lowercase.
    imagenverifpath = models.CharField(db_column='IMAGENVERIFPATH', max_length=1024)  # Field name made lowercase.
    usuario_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_IDUSUARIO')  # Field name made lowercase.

    class Meta:
        db_table = 'imagenverif'

class Reservarcancha(models.Model):
    usuario_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_IDUSUARIO')  # Field name made lowercase.
    canchas_idcancha = models.ForeignKey(Canchas, models.DO_NOTHING, db_column='canchas_IDCANCHA')  # Field name made lowercase.
    horainicio = models.DateTimeField(db_column='HORAINICIO')  # Field name made lowercase.
    horafin = models.DateTimeField(db_column='HORAFIN')  # Field name made lowercase.
    estado = models.IntegerField(db_column='ESTADO')  # Field name made lowercase.

    class Meta:
        db_table = 'reservarcancha'
