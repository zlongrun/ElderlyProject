from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')

class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    realname = forms.CharField(label="真实姓名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')

class InfoEditForm(forms.Form):
    gender = (
        ('male','男'),
        ('female','女'),
    )
    userright = (
        ('common','普通用户'),
        ('vip','vip用户'),
    )
    userflag = (
        ('0','已注销'),
        ('1','正常'),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    realname = forms.CharField(label="真实姓名",max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #id = forms.AutoField()
    email = forms.EmailField(label="邮箱", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    region = forms.CharField(label='所在地区（省一级市）',max_length=32,widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='地址',max_length=128,widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip = forms.CharField(label='邮政编码',max_length=32,widget=forms.TextInput(attrs={'class': 'form-control'}))
    fax = forms.CharField(label='传真',max_length=32,widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='座机号码',max_length=32,widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile = forms.CharField(label='手机号码',max_length=32,widget=forms.TextInput(attrs={'class': 'form-control'}))
    ID_card = forms.CharField(label='身份证号',max_length=128,widget=forms.TextInput(attrs={'class': 'form-control'}))
    about = forms.CharField(label='介绍',max_length=500,widget=forms.TextInput(attrs={'class': 'form-control'}))