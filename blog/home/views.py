# 2.6展示首页
from django.views import View
from django.shortcuts import render


# 2.6展示首页
class IndexView(View):
    """首页广告"""

    def get(self, request):
        """提供首页广告界面"""
        return render(request, 'index.html')
