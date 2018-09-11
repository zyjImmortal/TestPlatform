from django.db import models


# Create your models here.


class Product(models.Model):
    product_name = models.CharField('产品名称', max_length=64)
    product_desc = models.CharField('产品描述', max_length=200)
    producter = models.CharField('产品负责人', max_length=200)
    create_time = models.DateTimeField('创建时间', auto_now=True)

    class Meta:
        verbose_name = '产品管理'
        verbose_name_plural = '产品管理'

    def __str__(self):
        return self.product_name

    def __repr__(self):
        return 'Product<product_name:{}>'.format(self.product_name)


class Env(models.Model):
    name = models.CharField('环境名称', max_length=20)
    env_url = models.CharField('环境URL', max_length=50)
    url = models.URLField('URL', max_length=60)

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Env<{}>'.format(self.name)

    class Meta:
        verbose_name = '环境访问地址'
        verbose_name_plural = '环境访问地址'


class Version(models.Model):
    version = models.CharField('版本', max_length=30)

    def __str__(self):
        return self.version

    class Meta:
        verbose_name = '版本号'
        verbose_name_plural = '版本号'


class DataBaseConfig(models.Model):
    db_name = models.CharField('数据库名称', max_length=50)
    db_host = models.CharField('数据库地址', max_length=100)
    db_port = models.IntegerField('端口')
    db_user = models.CharField('用户', max_length=20)
    db_pwd = models.CharField('密码', max_length=30)

    def __str__(self):
        return self.db_name

    class Meta:
        verbose_name = '数据库'
        verbose_name_plural = '数据库'
