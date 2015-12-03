# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
     #   unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
     #   unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
      #  unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
      #  unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Tlaboratorio(models.Model):
    id_laboratorio = models.AutoField(db_column='ID_LABORATORIO', primary_key=True)  # Field name made lowercase.
    nombre_laboratorio = models.CharField(db_column='NOMBRE_LABORATORIO', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Admin:
           list_display = ('ID_LABORATORIO', 'NOMBRE_LABORATORIO')
     
    class Meta:
        managed = False
        db_table = 'tlaboratorio'

   
class Tmedicamento(models.Model):
    id_medicamento = models.IntegerField(db_column='ID_MEDICAMENTO', primary_key=True)  # Field name made lowercase.
    nombre_medicamento = models.CharField(db_column='NOMBRE_MEDICAMENTO', max_length=80, blank=True, null=True)  # Field name made lowercase.
    cantidad_disponible = models.IntegerField(db_column='CANTIDAD_DISPONIBLE')  # Field name made lowercase.
    laboratorio = models.ForeignKey(Tlaboratorio, db_column='LABORATORIO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmedicamento'

   
class Tpantalla(models.Model):
    pantalla = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'tpantalla'

   
class Trol(models.Model):
    rolname = models.CharField(db_column='rolName', primary_key=True, max_length=50)  # Field name made lowercase.
    roldes = models.CharField(db_column='rolDes', max_length=225, blank=True, null=True)  # Field name made lowercase.
    admin = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'trol'

class Tpermiso(models.Model):
    rolname = models.ForeignKey('Trol', db_column='rolName')  # Field name made lowercase.
    pantalla = models.ForeignKey('Tpantalla', db_column='pantalla')
    acceso = models.TextField()  # This field type is a guess.
    modificacion = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tpermiso'
        unique_together = (('rolname', 'pantalla'),)
    
  
class Tusuario(models.Model):
    nombre = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    rolname = models.ForeignKey(Trol, db_column='rolName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tusuario'

  