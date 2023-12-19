# 2.1 界面展示
from django.urls import path
from users.views import RegisterView
# 2.3 照片验证码
from users.views import ImageCodeView
# 2.4.2短信验证码
from users.views import SmsCodeView
# 3.1手机号登录
from users.views import LoginView
# 3.3退出登录
from users.views import LogoutView
# 4.1 忘记密码
from users.views import ForgetPasswordView
# 5.1用户中心
from users.views import UserCenterView

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

    # 3.1 登录路由
    path('login/', LoginView.as_view(), name='login'),

    # 3.3 退出登录
    path('logout/', LogoutView.as_view(), name='logout'),

    # 4.1 忘记密码
    path('forgetpassword/', ForgetPasswordView.as_view(), name='forgetpassword'),

    # 5.1用户中心
    path('center/', UserCenterView.as_view(), name='center'),
]
