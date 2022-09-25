from re import T
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

# 會員

class Members(models.Model):
    image_type = (
        ('monster-1.png', '咘咘'),
        ('monster-2.png', '喬治'),
        ('monster-3.png', '布萊恩'),
        ('monster-4.png', '里歐'),
        ('monster-5.png', '鮑伯'),
        ('monster-6.png', '艾倫'),
    )
    gender_type = (
        ('1', '男性'),
        ('2', '女性'),
    )
    name = models.CharField(max_length=20, verbose_name="暱稱")
    gender = models.CharField(max_length=1, choices=gender_type, verbose_name="性別", default='1')
    email = models.EmailField(max_length=60, unique=True, verbose_name="電子信箱")
    password = models.CharField(max_length=20, verbose_name="密碼")
    image = models.CharField(max_length=20, choices=image_type, verbose_name="頭像")
    created_date = models.DateField(default=timezone.now,verbose_name='建立日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')
    class Meta:
        verbose_name = "會員"   # 單數
        verbose_name_plural = verbose_name   #複數
        ordering = ['-id']
    def __str__(self):
        return self.name


# 話題

class Topic(models.Model):
    name = models.CharField(max_length=20, verbose_name="話題", blank=True)
    post_number = models.IntegerField(verbose_name="發文數", default=0)
    created_date = models.DateField(default=timezone.now,verbose_name='建立日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')
    class Meta:
        verbose_name = "話題"   # 單數
        verbose_name_plural = verbose_name   #複數
        # ordering = ['-id']
    def __str__(self):
        return self.name

# 貼文

class Post(models.Model):
    author = models.ForeignKey(Members,on_delete = models.CASCADE, null=True, blank=True)
    #  Topic 可以透過 'post' 反向查詢 Post
    topic_fk = models.ForeignKey(Topic,on_delete = models.CASCADE, null=True, blank=True)
    topic = models.CharField(max_length=20, verbose_name="話題", blank=True)
    title = models.CharField(max_length=20, verbose_name="標題")
    content = RichTextUploadingField(max_length=200, verbose_name='編輯器內文')
    created_date = models.DateField(default=timezone.now,verbose_name='建立日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')
    class Meta:
        verbose_name = "貼文"   # 單數
        verbose_name_plural = verbose_name   #複數
        ordering = ['-created_date']
    def __str__(self):
        return self.title

