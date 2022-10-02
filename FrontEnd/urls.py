from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 首頁
    path('', views.index, name='index'),
    # 登入
    # path('index', views.login, name='login'),
    # 註冊
    # path('singup', views.singup, name='singup'),
    # 登出
    path('logout', views.logout, name='logout'),
    # 個人頁面
    path('profile', views.profile, name='profile'),
    # path('profile/pk', views.profile, name='profile'),
    
    # 話題
    path('topic', views.topic, name='topic'),
    # 所有文章
    path('topic/<topic>', views.all, name='all'),
    # 原本的所有文章 all 路經拿掉 變成 topic/<topic>
    path('article/<pk>', views.article, name='article'),
    # 發文
    path('post/<topic>', views.post, name='post'),

    # 規範
    path('rule', views.rule, name='rule'),
    # 修改密碼
    path('change_password/<pk>', views.change_password, name='change_password'),
]