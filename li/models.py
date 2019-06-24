# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccessControlEquipment(models.Model):
    dept_code = models.CharField(db_column='DEPT_CODE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    equ_id = models.CharField(db_column='EQU_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    equ_mac = models.CharField(db_column='EQU_MAC', max_length=20)  # Field name made lowercase.
    equ_add = models.CharField(db_column='EQU_ADD', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'access_control_equipment'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DepartmentInformation(models.Model):
    dept_code = models.CharField(db_column='DEPT_CODE', primary_key=True, max_length=6)  # Field name made lowercase.
    dept_name = models.CharField(db_column='DEPT_NAME', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department_information'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class EmployeeInformation(models.Model):
    mark_no = models.CharField(db_column='MARK_NO', max_length=10)  # Field name made lowercase.
    empl_code = models.CharField(db_column='EMPL_CODE', primary_key=True, max_length=10)  # Field name made lowercase.
    empl_name = models.CharField(db_column='EMPL_NAME', max_length=100)  # Field name made lowercase.
    posi = models.CharField(db_column='POSI', max_length=100)  # Field name made lowercase.
    dept_code = models.CharField(db_column='DEPT_CODE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    sex_code = models.CharField(db_column='SEX_CODE', max_length=10)  # Field name made lowercase.
    education = models.CharField(db_column='EDUCATION', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee_information'


class G(models.Model):
    dept_code = models.CharField(db_column='DEPT_CODE', max_length=6)  # Field name made lowercase.
    dept_neme = models.CharField(db_column='DEPT_NEME', max_length=100)  # Field name made lowercase.
    dept_type = models.CharField(db_column='DEPT_TYPE', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g'


class OpenRecordThroughAccessControl(models.Model):
    mark_no = models.CharField(db_column='MARK_NO', primary_key=True, max_length=10)  # Field name made lowercase.
    empl_code = models.CharField(db_column='EMPL_CODE', max_length=10)  # Field name made lowercase.
    equ_id = models.CharField(db_column='EQU_ID', max_length=10)  # Field name made lowercase.
    open_date = models.DateField(db_column='OPEN_DATE')  # Field name made lowercase.
    open_time = models.TimeField(db_column='OPEN_TIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'open_record_through_access_control'
        unique_together = (('mark_no', 'open_date', 'open_time'),)


class User(models.Model):
    mark_no = models.CharField(db_column='MARK_NO', primary_key=True, max_length=10)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
