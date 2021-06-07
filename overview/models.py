from django.db import models
from login.models import UserInfo

class FileInfo(models.Model):
    type = (
        ('.pdf','pdf'),
        ('.docx','word'),
    )
    state = (
        ('private','未公开'),
        ('public','已公开'),
    )
    file_id = models.IntegerField(default=1,unique=True)
    name = models.CharField(max_length=32)
    #uploader = models.ForeignKey(UserInfo, to_field=UserInfo.username, on_delete=models.CASCADE)
    uploader = models.CharField(max_length=32)
    #owner = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    publish_state = models.CharField(max_length=10,choices=state,default='未公开')
    prices = models.IntegerField(default=100)
    topic = models.TextField()
    type = models.CharField(max_length=10,choices=type,default='.docx')
    src = models.CharField(max_length=100)
    file =  models.FileField(upload_to='files/%Y/%m/%d',default=None)

    def __str__(self) :
        return self.name

    


