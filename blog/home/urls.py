# 2.6展示首页
from django.urls import path
from home.views import IndexView

# 2.6展示首页
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
