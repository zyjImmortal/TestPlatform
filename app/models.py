from django.db import models


# Create your models here.

class AppCase(models.Model):
    app_case_name = models.CharField('用例名称', max_length=200)
    app_test_result = models.CharField('测试结果', max_length=200)
    app_tester = models.CharField('测试负责人', max_length=56)
    create_time = models.DateField('创建时间', auto_now=True)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'APP测试用例'
        verbose_name_plural = 'APP测试用例'

    def __str__(self):
        return self.app_case_name


class AppCaseStep(models.Model):
    app_case = models.ForeignKey(AppCase, on_delete=models.CASCADE, null=True)
    app_test_step = models.CharField('测试步骤', max_length=64)
    app_test_obj_name = models.CharField('测试对象名称', max_length=100)
    app_element = models.CharField('控件元素', max_length=800)
    app_find_method = models.CharField('定位方式', max_length=300)
    app_test_data = models.CharField('测试数据', max_length=300, null=True)
    app_assert_data = models.CharField('验证数据', max_length=300, null=True)
    app_test_result = models.BooleanField('测试结果')
    create_time = models.DateTimeField('创建时间', auto_now=True)

    def __str__(self):
        return self.app_test_step