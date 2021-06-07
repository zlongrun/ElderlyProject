from django.shortcuts import render,redirect
from . import models
from .forms import UserForm, RegisterForm, InfoEditForm
from overview.models import FileInfo
import hashlib

from django.db.models import Q


def index(request):
    pass
    return render(request,'login/index.html')


def login(request):
    if request.session.get('is_login',None):
        return redirect('/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():  # 确保用户名和密码都不为空
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.UserInfo.objects.get(username=username)
                if user.password == password:
                    request.session['is_login'] = True
                    #request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'login/login.html', locals())
    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            realname = register_form.cleaned_data['realname']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.UserInfo.objects.filter(username=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.UserInfo.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户
                number = models.UserInfo.objects.count() + 1
                new_user = models.UserInfo.objects.create()
                new_user.number = number + 1
                new_user.username = username
                new_user.realname = realname
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")

def info_show(request):
    username = request.session['user_name']
    userinfo = models.UserInfo.objects.get(username=username)
    return render(request,'login/info_show.html',{'UserInfo':userinfo})

def info_edit(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    if request.method == "POST":
        infoedit_form = InfoEditForm(request.POST)
        username = request.session['user_name']
        userinfo = models.UserInfo.objects.get(username=username)
        if infoedit_form.is_valid():  # 获取数据
            userinfo.username = infoedit_form.cleaned_data['username']
            userinfo.realname = infoedit_form.cleaned_data['realname']
            userinfo.email = infoedit_form.cleaned_data['email'] 
            userinfo.sex = infoedit_form.cleaned_data['sex']
            userinfo.region = infoedit_form.cleaned_data['region']
            userinfo.address = infoedit_form.cleaned_data['address']
            userinfo.zip = infoedit_form.cleaned_data['zip']
            userinfo.fax = infoedit_form.cleaned_data['fax']
            userinfo.phone = infoedit_form.cleaned_data['phone']
            userinfo.mobile = infoedit_form.cleaned_data['mobile']
            userinfo.ID_card = infoedit_form.cleaned_data['ID_card']
            userinfo.about = infoedit_form.cleaned_data['about']
            userinfo.save()
            return redirect('/info_show/')
    else:
        username = request.session['user_name']
        userinfo = models.UserInfo.objects.get(username=username)
        userprofile = InfoEditForm(initial={
            'username':userinfo.username,
            'realname':userinfo.realname,
            'email':userinfo.email,
            'sex':userinfo.sex,
            'region':userinfo.region,
            'address':userinfo.address,
            'zip':userinfo.zip,
            'fax':userinfo.fax,
            'phone':userinfo.phone,
            'mobile':userinfo.mobile,
            'ID_card':userinfo.ID_card,
            'about':userinfo.about
        })
        return render(request,'login/info_edit.html',{'infoedit_form':userprofile})

def myfiles(request):
    username = request.session['user_name']
    queryset = FileInfo.objects.filter(uploader=username)
    #print(queryset)
    public_files = queryset.filter(Q(publish_state='public')|Q(publish_state='已公开'))
    private_files = queryset.filter(Q(publish_state='private')|Q(publish_state='未公开'))
    #print(private_files)
    #print(public_files)
    return render(request,'login/myfiles.html',{'public_files':public_files,'private_files':private_files})
    


