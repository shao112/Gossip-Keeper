from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse

from .forms import LoginForm, SignupForm, PostForm

from .models import Members, Post, Topic

from django.contrib import messages

from django.core.paginator import Paginator

from Scrape.scrapers import PTT
from Scrape.googlenews_10 import google_news

from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.utils import timezone

@csrf_exempt
def DBlist(request, dateFilter):
    # ptt = PTT()
    # top_six = ptt.scrape()

    now = datetime.datetime.now()
    datalist = []
    print(dateFilter)
    if(dateFilter == "day"):
        # getdata = Topic.objects.all()[:6]
        getdata = Topic.objects.filter(update_date=now)[:6]
        for one_data in getdata:
            data = one_data.to_dict()
            print("-------------------")
            print(data)
            datalist.append(data)
            print(datalist)
        # datalist = top_six
        # print(datalist)
    elif(dateFilter == "month"):
        getdata = Topic.objects.filter(created_date__month=now.month)[:6]
        for one_data in getdata:
            data = one_data.to_dict()
            print("-------------------")
            print(data)
            datalist.append(data)
    elif(dateFilter == "year"):
        getdata = Topic.objects.filter(created_date__year=now.year)[:6]
        for one_data in getdata:
            data = one_data.to_dict()
            print("-------------------")
            print(data)
            datalist.append(data)
    
    return JsonResponse(datalist, safe=False)

# 首頁
def index(request):
    Login_form = LoginForm()
    Signup_form = SignupForm()
    ptt = PTT()

    # 回傳 6 個關鍵字為陣列，要不要把 top_six 拿掉，之後改成傳 topic 就好
    top_six = ptt.scrape()
    # 回傳 6 個關鍵字的 link 為陣列
    googlenews = google_news(top_six)
    link = googlenews.google()
    # print("連結")
    # print(link)

    # 看這六個關鍵字有沒有在資料庫裡，有的話就加 times，沒有就存資料庫
    for i, val in enumerate(top_six):
        topic = Topic.objects.filter(name=val)
        print(i)
        print(val)
        if not topic:
            print("新的關鍵字，儲存至資料庫！")
            Topic.objects.create(name=val)
        else:
            print("已有此關鍵字，出現次數加一！")
            topic = Topic.objects.get(name=val)
            times = topic.times + 1
            topic = Topic.objects.filter(name=val).update(times=times)
            topic = Topic.objects.filter(name=val).update(update_date=datetime.datetime.now())
        # 把這六個關鍵字的 link 存入資料庫
        # t = Topic.objects.filter(name=val)
        Topic.objects.filter(name=val).update(link=link[i])
        print("已儲存 link!")


    if request.POST.get('submit') == '登入' and request.method == "POST":
        print("進到登入")
        return login(request)
    if request.POST.get('submit') == '註冊' and request.method == "POST":
        print("進到註冊")
        return singup(request)
    
    # now = datetime.datetime.now()
    # print("---- now.day -----")
    # print(now.day)
    # month_topic = Topic.objects.filter(created_date__month=now.month)[:6]
    # year_topic = Topic.objects.filter(created_date__year=now.year)[:6]
    # print("month topic")
    # print(month_topic)
    # print("year topic")
    # print(year_topic)

    # 讀取 session
    members = request.session.get('members','')
    
    context = {
        'Login_form': Login_form,
        'Signup_form': Signup_form,
        'members': members,
        # 'ptt': top_six,
        # 'topic': topic,
        # 'link':link
    }

    return render(request, "index/index.html", context)

# 登入
def login(request):

    if request.method == 'POST':
        # 登入表單輸入的帳號與密碼
        username = request.POST.get('email', '')
        password = request.POST.get('password', '')
        print(username,password)
        # 過濾資料庫裡面有沒有此筆資料
        members = Members.objects.filter(email=username).filter(password=password)
        print(members)
        print(members.first)
        if not members:
            print("失敗啦")
            messages.info(request, '錯誤的密碼或信箱')
            # messages.add_message(request, messages.WARNING,"錯誤的密碼或信箱")
            return HttpResponseRedirect("/")
        else:
            # 抓出資料庫裡帳號相同的資料
            members = Members.objects.get(email=username)
            # 利用 session 保存模型物件
            request.session['members'] = members
            print("成功啦 - ",request.session['members'])
            # request.session['members'] = id #新增session，並對應user值為id
            # id = request.session.get('user','') #讀取瀏覽器session
            context = {
                'members': members
                # 'members': id 
            }
            print(members)
            print(members.name)
            # return members
            return render(request, "index/index.html", context)

# 登出
def logout(request):
    del request.session['members']
    return HttpResponseRedirect('/')

# 註冊
def singup(request):
    form = SignupForm(request.POST)
    
    if form.is_valid():
        print(form)
        form.save()
        print("進到註冊後儲存!")
        # 手動更新頭像，先抓出剛剛註冊的用戶，再抓出選擇的頭像
        email = request.POST.get('email', '')
        image = request.POST.get('payments', '')
        print("------ 註冊 Debug -------")
        print(email)
        print(image)
        Members.objects.filter(email=email).update(image=image)
        return HttpResponseRedirect("/")
    # context = {
    #     'Signup_form': SignupForm
    # }
    print("進到註冊後沒有儲存")
    return HttpResponseRedirect("/")
    # return render(request, "index/index.html", context)

# 話題
def topic(request):
    # query set
    topic = Topic.objects.values('name').distinct()
    # print(topic.query)
    for t in topic:
        print(t['name'])
        # 篩選是該 Topic 的 Post，計算出數量
        post_num = Post.objects.filter(topic=t['name']).count()
        # 取得該 Topic 物件
        tme_post = Topic.objects.get(name=t['name'])
        print(tme_post)
        Topic.objects.filter(name=t['name']).update(post_number=post_num)
        print(post_num)
        print("------")
    # 重新抓 Topic
    topic = Topic.objects.all()
    # topic_hot = Topic.objects.all()[:3]、一般 topic [3:]
    
    # 顯示五筆資料
    paginator = Paginator(topic, 5)
    # 獲取url中的頁碼，比如第一頁，我們需要在url末尾中新增 ?page=1
    page = request.GET.get('page')
    # 獲取相應的頁碼的資料，比如page=1，第一頁，這裡獲取得到第一頁的資料內容
    topic = paginator.get_page(page)
    # 獲取一共分出來了多少頁，前端展示所有頁碼數的時候需要用到該數
    print("總共有",paginator.num_pages,"頁")
    print("多少資料",paginator.object_list)
    print(topic.paginator.page_range)
    context = {
        # 'topic_hot': topic_hot,
        'topic':topic,
        'post_num':post_num
    }
    return render(request, "topic/topic.html", context)

# 搜尋出來的話題
def search_topic(request):
    if request.method == "POST":
        searched = request.POST['searched']
        topic = Topic.objects.filter(name__contains = searched)

        context = {
            'searched': searched,
            'topic':topic
        }

        return render(request, "topic/search_topic.html", context)

    
    return render(request, "topic/search_topic.html")

# 所有文章
def all(request, topic):
    post = Post.objects.filter(topic=topic)
    print(post)
    # 顯示五筆資料
    paginator = Paginator(post, 5)
     # 獲取url中的頁碼，比如第一頁，我們需要在url末尾中新增 ?page=1
    page = request.GET.get('page')
    # 獲取相應的頁碼的資料，比如page=1，第一頁，這裡獲取得到第一頁的資料內容
    post = paginator.get_page(page)
     # 獲取一共分出來了多少頁，前端展示所有頁碼數的時候需要用到該數
    print("總共有",paginator.num_pages,"頁")
    print("多少資料",paginator.object_list)
    print(post.paginator.page_range)
    # post = Post.objects.filter(topic_fk__name=topic)
    context = {
        'post': post,
        'topic': topic
    }
    return render(request, "all/all.html",context)


# 文章詳細內文
def article(request, pk):
    # 讀取 session
    members = request.session.get('members','')

    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
        'members': members
    }
    return render(request, "article/article.html",context)

# 發文
def post(request, topic):

    form = PostForm()

    if request.method=='POST':
        print("收到 POST 請求!")
        form=PostForm(request.POST)
        if form.is_valid():
            # 讀取 session 抓取發文的使用者
            members = request.session.get('members','')
            form.instance.author = members

            form.save()
            # 手動更新話題，先抓出剛剛新增的貼文
            # content = request.POST.get('content', '')
            # print(content)
            print("----- Post Debug ----")
            title = request.POST.get('title', '')
            print(title)
            Post.objects.filter(title=title).update(topic=topic)
            print("發布成功!")
            return all(request, topic)
        print("form is unvalid")
        print(form.errors)
    
    context = {
        'form':form,
        'topic':topic
    }

    return render(request, "post/post.html", context)



# 個人頁面
def profile(request):
    # 讀取 session
    members = request.session.get('members','')

    print(members.email)

    this_guy_post_number = Post.objects.filter(author=members).count()
    print(this_guy_post_number)

    post_queryset = Post.objects.filter(author=members)
    print(post_queryset)

    context = {
        'members':members,
        'this_guy_post_number':this_guy_post_number,
        'post_queryset':post_queryset
    }

    return render(request, "profile/profile.html",context)


# 規範
def rule(request):
    return render(request, "rule/rule.html")
# 修改密碼
def change_password(request, pk):

    members = Members.objects.get(id=pk)

    if request.method == 'POST':
        password = request.POST.get('password', '')
        print("新的密碼")
        print(password)
        members = Members.objects.filter(id=pk).update(password=password)
        # 刪除 session，重新登入
        del request.session['members']
        return HttpResponseRedirect('/')

    context = {
        'members': members,
    }
    return render(request, "change_password/change_password.html",context)