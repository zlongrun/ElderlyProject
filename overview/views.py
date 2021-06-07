import os
import io
from django.shortcuts import redirect, render
from pydocx import PyDocX
from ElderlyProject.settings import BASE_DIR
from . import models
from django.template.loader import render_to_string
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas

def overview(request,num):
    #file_id = request.session["file_id"]
    file = models.FileInfo.objects.get(file_id=num)
    request.session["file_id"] = file.file_id
    request.session["src"] = file.src
    request.session["name"] = file.name
    
    return render(request,'overview/overview.html',{'FileInfo':file})

def viewdoc(request):
    path = os.path.join(BASE_DIR, request.session["src"])
    # print(path)
    load_html = PyDocX.to_html(path)
    html_path = "overview/templates/filehtmls/"+request.session["name"]+".html"
    f = open(html_path, 'w', encoding="utf-8")
    f.write(load_html)
    f.close()
    return render(request,"filehtmls/"+request.session["name"]+".html")

def viewpdf(request):
    path = "static/pdf/"+request.session["name"]+".pdf"
    return FileResponse(open(path, 'rb'), content_type='application/pdf')

def publish(request):
    num = request.session["file_id"]
    file = models.FileInfo.objects.get(file_id=num)
    file.publish_state = "已公开"
    file.save()
    return render(request,'overview/overview.html',{'FileInfo':file})

def priavte(request):
    num = request.session["file_id"]
    file = models.FileInfo.objects.get(file_id=num)
    file.publish_state = "未公开"
    file.save()
    return render(request,'overview/overview.html',{'FileInfo':file})


