from django.db import models


# Create your models here.
class APInfo(models.Model):
    name = models.CharField(max_length=120, verbose_name="AP名称")
    ip_address = models.GenericIPAddressField(protocol='IPv4', unpack_ipv4=False, verbose_name="IP地址")
    type = models.CharField(max_length=120, verbose_name="型号")
    position = models.CharField(max_length=200, verbose_name="位置")
    switch = models.GenericIPAddressField(protocol='IPv4', unpack_ipv4=False, verbose_name="交换机名称")
    port = models.CharField(max_length=100, verbose_name="端口号")

    class Meta:
        verbose_name = "无线接入点"
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     return self.name
    # def __unicode__(self):
    #     return self.name


class OfficeNetworkInfo(models.Model):
    office_port = models.CharField(max_length=200, verbose_name="工位端口编号")
    switch_name = models.CharField(max_length=120, verbose_name="交换机名称")
    switch_ip = models.GenericIPAddressField(protocol='IPv4', unpack_ipv4=False, verbose_name="交换机管理IP")
    switch_port = models.CharField(max_length=120, verbose_name="交换机端口")
    position = models.CharField(max_length=120, verbose_name="位置")
    remarks = models.CharField(max_length=200, blank=True, verbose_name="备注")

    class Meta:
        verbose_name = "办公网端口"
        verbose_name_plural = verbose_name


class SmartNetworkInfo(models.Model):
    smart_port = models.CharField(max_length=200, verbose_name="终端端口编号")
    switch_name = models.CharField(max_length=120, verbose_name="交换机名称")
    switch_ip = models.GenericIPAddressField(protocol='IPv4', unpack_ipv4=False, verbose_name="交换机管理IP")
    switch_port = models.CharField(max_length=120, verbose_name="交换机端口")
    position = models.CharField(max_length=120, verbose_name="位置")
    remarks = models.CharField(max_length=200, blank=True, verbose_name="备注")

    class Meta:
        verbose_name = "智能化端口"
        verbose_name_plural = verbose_name


class SystemLogin(models.Model):
    type = models.CharField(max_length=120, verbose_name="设备类型")
    name = models.CharField(max_length=120, verbose_name="平台名称")
    address = models.CharField(max_length=120, verbose_name="管理地址")
    image = models.ImageField(null=True, blank=True, upload_to="system_login", verbose_name='系统LOGO')

    class Meta:
        verbose_name = "内部系统登录"
        verbose_name_plural = verbose_name


class PhoneList(models.Model):
    # 定义号码状态的选项
    STATUS_CHOICES = [
        ('in_use', '在用'),  # 在用
        ('idle', '空闲'),  # 空闲
    ]

    tel_num = models.CharField(max_length=50,verbose_name='电话号码')
    department = models.CharField(max_length=200,verbose_name='部门/工作室')
    tel_user = models.CharField(max_length=100,verbose_name='使用人')
    office_port = models.CharField(max_length=100,verbose_name='桌面端口编号')
    tel_port = models.CharField(max_length=100, verbose_name='电话交换机端口')
    tel_state = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='空闲',  # 默认状态为 "空闲"
    )
    floor = models.CharField(max_length=100, verbose_name='楼层分布')
    remarks = models.CharField(max_length=200, blank=True, verbose_name="备注")

    class Meta:
        verbose_name = "电信固话号码"
        verbose_name_plural = verbose_name

class WifiInfo(models.Model):
    SECURITY_CHOICES = [
        ('WPA-WPA2','WPA-WPA2'),
        ('WPA2-PSK','WPA2-PSK'),
        ('open','open'),
    ]
    department = models.CharField(max_length=200,verbose_name='部门/工作室')
    ssid = models.CharField(max_length=100, verbose_name='WiFi 名称')
    password = models.CharField(max_length=100,blank=True,null=True,verbose_name='WiFi 密码')
    security_type = models.CharField(max_length=20, choices=SECURITY_CHOICES, default='WPA-WPA2',verbose_name='加密类型')
    public_ip = models.GenericIPAddressField(protocol='IPv4', unpack_ipv4=False,blank=True,null=True, verbose_name="公网IP")
    remarks = models.CharField(max_length=200, blank=True, null=True, verbose_name="备注")

    class Meta:
        verbose_name = "WiFi 信息"
        verbose_name_plural = verbose_name