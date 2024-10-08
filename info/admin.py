from django.contrib import admin
from django.utils.html import format_html
from info.models import APInfo, OfficeNetworkInfo, SmartNetworkInfo, SystemLogin, PhoneList, WifiInfo

admin.site.site_header = "IT信息管理"
admin.site.site_title = "IT管理系统"
admin.site.index_title = "让IT管理更加简单"


# 方式2：使用装饰器
@admin.register(APInfo)
class APInfoAdmin(admin.ModelAdmin):
    # 字段显示列表
    list_display = ['id', 'name', 'ip_address', 'type', 'position', 'switch', 'port']
    # 搜索
    search_fields = ['name']

    # 动作 复选框,默认在顶部
    # actions_on_top = False
    # actions_on_bottom = True

    # 每页显示数据 条数
    list_per_page = 25

    # 显示编辑页面中哪些字段可编辑,默认全部(除ID外)
    # 注意: fields 与 fieldsets 不能同时存在,选其一
    # 简单显示
    # fields = ['name', 'ip_address', 'type', 'switch']

    # 分组显示
    fieldsets = (
        ('基本', {'fields': ['name', 'ip_address', 'type']}),
        ('高级', {
            'fields': ['position', 'switch', 'port'],
            'classes': ['collapse', ]  # 是否折叠显示
        }),
    )

    # class Meta:
    #     app_label = 'AP'


class OfficeNetworkInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'office_port', 'switch_name', 'switch_ip', 'switch_port', 'position', 'remarks']
    # 搜索
    search_fields = ['office_port']
    # 默认 分页数量为100,可自定义调整
    list_per_page = 25


class SmartNetworkInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'smart_port', 'switch_name', 'switch_ip', 'switch_port', 'position', 'remarks']
    # 搜索
    search_fields = ['smart_port']
    list_per_page = 25


class SystemLoginAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'name', 'image', 'address_link']

    # list_display_links = ['address']
    def address_link(self, obj):
        return format_html('<a href="{}" target="_blank">点击登录</a>', obj.address)

    address_link.short_description = '登录'


class PhoneListAdmin(admin.ModelAdmin):
    list_display = ['id', 'tel_num', 'department', 'tel_user', 'office_port', 'tel_port', 'tel_state', 'floor',
                    'remarks']
    # 搜索
    search_fields = ['tel_num', 'tel_user', 'department']
    list_per_page = 25


class WiFiInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'department', 'ssid', 'password','security_type','public_ip','remarks']
    search_fields = ['department']
    list_per_page = 25

# 方式1
# admin.site.register(APInfo, APInfoAdmin)
admin.site.register(OfficeNetworkInfo, OfficeNetworkInfoAdmin)
admin.site.register(SmartNetworkInfo, SmartNetworkInfoAdmin)
admin.site.register(SystemLogin, SystemLoginAdmin)
admin.site.register(PhoneList, PhoneListAdmin)
admin.site.register(WifiInfo, WiFiInfoAdmin)
