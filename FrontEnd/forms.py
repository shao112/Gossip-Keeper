from django import forms
from .models import Members,Post

# 登入表單
class LoginForm(forms.ModelForm):

    class Meta:
        model = Members
        
        fields = ('email', 'password')

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'email': '帳號',
            'password': '密碼',
        }

# 註冊表單
gender_type = (
    ('1', '男性'),
    ('2', '女性'),
)
image_type = (
    ('monster-1.png', 'Monster1'),
    ('monster-2.png', 'Monster2'),
    ('monster-3.png', 'Monster3'),
    ('monster-4.png', 'Monster4'),
    ('monster-5.png', 'Monster5'),
    ('monster-6.png', 'Monster6'),
)
class SignupForm(forms.ModelForm):
    
    # gender = ModelChoiceField(Members.objects.all(), empty_label=None)

    class Meta:
        model = Members
        fields = ('name', 'gender','email','password','image')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(choices=gender_type,
            attrs={
                'class': 'form-check',
            }),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'pattern': '([A-Za-z0-9.])+@([A-Za-z0-9])+.[a-z.]{2,}'
                }),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'id': 'password',
                    'onblur': 'checkpas1()',
                    'title': '請輸入八個英、數字，不可輸入符號及空格',
                    'pattern': '([a-zA-Z0-9])\w{8,}'
                }),
            'image': forms.Select(choices=image_type,
                attrs={
                    'class': 'form-control'
                    # 'class': 'select2-hidden-accessible',
                    # 'id': 'id_select2_example',
                    # 'style': 'width: 120px; height:60px;'
                }),
        }
        #預設會是顯示英文欄位，可用labels改成對應中文欄位
        labels = {
            'name': '暱稱',
            'gender': '性別',
            'email': 'Email',
            'password': '密碼',
            'image': '頭像'
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        print(self.fields['image'].choices[1][0])
    #     self.fields['gender'].empty_label = None
    #     print(self.fields['gender'].choices[0])
        # print(self.fields['gender'].label)
        # del self.fields['gender'].choices[0]
        # self.fields['gender'].choices[0] = None
        # print(self.fields['gender'].choices)

# 發文表單
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        
        fields = ('topic', 'title', 'content')

        widgets = {
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'name':'title',
                }),
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'rows':'4',
                    'name': 'content',
                })
        }

        labels = {
            'topic': '話題',
            'title': '標題',
            'content': '內容',
        }

        # def __init__(self, *args, **kwargs):
        #     topic = kwargs.pop('topic','')
        #     super(PostForm, self).__init__(*args, **kwargs)
        #     self.fields['topic']=forms.ModelChoiceField(queryset=topic.objects. filter(topic=topic))
