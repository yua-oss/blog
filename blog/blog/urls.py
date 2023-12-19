"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.http import HttpResponse
import logging

#
# # 创建日志获取
# logger = logging.getLogger('django')
#
#
# def log(request):
#     # 使用日志器记录信息
#     logger.info('info')
#     return HttpResponse('test')


urlpatterns = [
    path('admin/', admin.site.urls),
    # include 参数1要设置为元组（urlconf_module, app_name）
    # namespace 设置命名空间
    path('', include(('users.urls', 'users'), namespace='users')),
    # path('', log),
    path('', include(('home.urls', 'home'), namespace='home')),
]
# 5.1.2 用户中心-信息修改
# 以下代码为设置图片访问路由规则
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
