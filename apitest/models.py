from django.db import models

# Create your models here.
from product.models import Product

REQUEST_MOTHOD = (('get', 'get'), ('post', 'post'))


class ApiTestCase(models.Model):
    api_case_name = models.CharField('接口测试用例名称', max_length=64)
    api_case_desc = models.CharField('用例描述', max_length=64, null=True)
    api_case_tester = models.CharField('执行人', max_length=64)
    api_case_result = models.BooleanField('测试结果')
    create_time = models.DateTimeField('创建时间', auto_now=True)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = '接口测试用例'
        verbose_name_plural = '接口测试用例'

    def __str__(self):
        return self.api_case_name


class ApiStep(models.Model):
    api_step = models.CharField('测试步骤', max_length=100, null=True)
    api_name = models.CharField('接口名称', max_length=64)
    api_url = models.CharField('接口地址', max_length=100)
    api_param = models.CharField('参数和值', max_length=800)
    api_method = models.CharField('请求方法', choices=REQUEST_MOTHOD, default='get', max_length=200, null=True)
    api_result = models.CharField('预期结果', max_length=200)
    api_status = models.BooleanField('是否通过')
    create_time = models.DateTimeField('创建时间', auto_now=True)
    api_case = models.ForeignKey(ApiTestCase, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.api_step


class Api(models.Model):
    api_name = models.CharField('接口名称', max_length=64)
    api_url = models.CharField('接口地址', max_length=100)
    api_param = models.CharField('参数和值', max_length=800)
    api_method = models.CharField('请求方法', choices=REQUEST_MOTHOD, default='get', max_length=200, null=True)
    api_result = models.CharField('预期结果', max_length=200)
    api_status = models.BooleanField('是否通过')
    create_time = models.DateTimeField('创建时间', auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = '单一场景接口'
        verbose_name_plural = '单一场景接口'

    def __str__(self):
        return self.api_name
