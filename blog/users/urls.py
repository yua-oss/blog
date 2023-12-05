# 2.1 界面展示
from django.urls import path
from users.views import RegisterView
# 2.3 照片验证码
from users.views import ImageCodeView
# 2.4.2短信验证码
from users.views import SmsCodeView

# 进行users 子应用的视图路由
urlpatterns = [
    # 2.1 界面展示
    # 参数1：路由
    # 参数2：视图函数
    # 参数3：路由名，方便通过reverse来获取路由
    path('register/', RegisterView.as_view(), name='register'),
    # 2.3 照片验证码的路由
    # 参数1：路由
    # 参数2：视图函数
    # 参数3：路由名，方便通过reverse来获取路由
    path('imagecode/', ImageCodeView.as_view(), name='imagecode'),

    # 短信发送
    path('smscode/', SmsCodeView.as_view(), name='smscode'),
]
