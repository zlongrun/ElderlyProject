from django.db import models

class UserInfo(models.Model):
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
    number = models.IntegerField(default=1)
    username = models.CharField(max_length=128, unique=True)
    realname = models.CharField(max_length=32)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32,choices=gender,default='男')
    right = models.CharField(max_length=32,choices=userright,default='普通用户') 
    region = models.CharField(max_length=32, blank= True)
    address = models.CharField(max_length=128, blank= True)
    zip = models.CharField(max_length=32,blank= True)
    fax = models.CharField(max_length=32,blank= True)
    phone = models.CharField(max_length=32,blank= True)
    mobile = models.CharField(max_length=32,blank= True)
    ID_card = models.CharField(max_length=128,blank= True)
    c_time = models.DateTimeField(auto_now_add=True)
    flag = models.CharField(max_length=32,choices=userflag,default='正常')
    about = models.TextField(blank=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'













