# 2.6展示首页
from django.urls import path
from home.views import IndexView, DetailView

# 2.6展示首页
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # 8.1 详情视图的路由
    path('detail/', DetailView.as_view(), name='detail'),
]
