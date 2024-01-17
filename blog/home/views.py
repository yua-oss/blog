# 2.6展示首页
from django.views import View
from django.shortcuts import render

# 7.1首页分类数据展示
from home.models import ArticleCategory
from django.http import HttpResponseNotFound

# 7.2首页文章数据展示
from home.models import Article
from django.http import HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage


# 2.6展示首页
class IndexView(View):
    """首页广告"""

    def get(self, request):
        # 7.1 首页分类数据展示
        # """提供首页广告界面"""
        # # ?cat_id=xxx&page_num=xxx&page_size=xxx
        # cat_id = request.GET.get('cat_id', 1)
        #
        # # 判断分类id
        # try:
        #     category = ArticleCategory.objects.get(id=cat_id)
        # except ArticleCategory.DoesNotExist:
        #     return HttpResponseNotFound('没有此分类')
        #
        # # 获取博客分类信息
        # categories = ArticleCategory.objects.all()
        #
        # context = {
        #     'categories': categories,
        #     'category': category
        # }
        # return render(request, 'index.html', context=context)
        """提供首页广告界面"""
        # ?cat_id=xxx&page_num=xxx&page_size=xxx
        cat_id = request.GET.get('cat_id', 1)
        page_num = request.GET.get('page_num', 1)
        page_size = request.GET.get('page_size', 10)
        # 判断分类id
        try:
            category = ArticleCategory.objects.get(id=cat_id)
        except ArticleCategory.DoesNotExist:
            return HttpResponseNotFound('没有此分类')

        # 获取博客分类信息
        categories = ArticleCategory.objects.all()

        # 分页数据
        articles = Article.objects.filter(
            category=category
        )

        # 创建分页器：每页N条记录
        paginator = Paginator(articles, page_size)
        # 获取每页商品数据
        try:
            page_articles = paginator.page(page_num)
        except EmptyPage:
            # 如果没有分页数据，默认给用户404
            return HttpResponseNotFound('empty page')
        # 获取列表页总页数
        total_page = paginator.num_pages

        context = {
            'categories': categories,
            'category': category,
            'articles': page_articles,
            'page_size': page_size,
            'total_page': total_page,
            'page_num': page_num,
        }

        return render(request, 'index.html', context=context)


# 8.5发表评论
from home.models import Comment, Article
from django.urls import reverse
from django.shortcuts import redirect


# 8.1 详情视图
class DetailView(View):
    # 8.1详情视图
    def get(self, request):
        # detail/?id=xxx&page_num=xxx&page_size=xxx
        # 获取文档id
        id = request.GET.get('id')

        # 获取博客分类信息
        categories = ArticleCategory.objects.all()

        try:
            article = Article.objects.get(id=id)
        except Article.DoesNotExist:
            # 8.2 404界面
            return render(request, '404.html')
        # 8.3 推荐文章
        else:
            article.total_views += 1
            article.save()
        # 获取热点数据
        hot_articles = Article.objects.order_by('-total_views')[:9]
        # 8.3 推荐文章
        # 8.6 评论显示
        page_size = request.GET.get('page_size', 10)
        page_num = request.GET.get('page_num', 1)
        comments = Comment.objects.filter(article=article).order_by('-created')
        total_count = comments.count()
        from django.core.paginator import Paginator, EmptyPage
        paginator = Paginator(comments, page_size)
        try:
            page_comments = paginator.page(page_num)
        except EmptyPage:
            return HttpResponseNotFound('empty page')
        # 总页数
        total_page = paginator.num_pages
        context = {
            'categories': categories,
            'category': article.category,
            'article': article,
            'hot_articles': hot_articles,  # 8.3推荐文章
            # <editor-fold desc="8.6 评论展示">
            'total_count': total_count,
            'comments': page_comments,
            'page_size': page_size,
            'total_page': total_page,
            'page_num': page_num,
            # </editor-fold>
        }
        return render(request, 'detail.html', context=context)

    # 8.5 发表评论
    def post(self, request):
        user = request.user
        if user and user.is_authenticated:
            # 接收数据
            id = request.POST.get('id')
            content = request.POST.get('content')

            # 判断文章是否存在
            try:
                article = Article.objects.get(id=id)
            except Article.DoesNotExist:
                return HttpResponseNotFound('没有此文章')

            # 保存到数据
            Comment.objects.create(
                content=content,
                article=article,
                user=user
            )
            # 修改文章评论数量
            article.comments_count += 1
            article.save()
            # 拼接跳转路由
            path = reverse('home:detail') + '?id={}'.format(article.id)
            return redirect(path)
        else:
            # 没有登录则跳转到登录页面
            return redirect(reverse('users:login'))
