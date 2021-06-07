# -*- coding: utf-8 -*-
from login import forms
from django.shortcuts import render, redirect
#from django.shortcuts import render_to_response
#from django.template import RequestContext
from overview.models import FileInfo
from login.models import UserInfo
from upload.form import FileForm

def upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            filename = form.cleaned_data['filename']
            filetype = form.cleaned_data['filetype']
            prices = form.cleaned_data['prices']
            uploader = request.session.get('user_name')
            topic = form.cleaned_data['topic']
            file = form.cleaned_data['filesrc']
            if filetype == 'pdf' or filetype =='.pdf':
                src = 'static/pdf/' + filename + '.pdf'
            elif filetype == 'word' or filetype =='.docx':
                src = 'static/docx/' + filename + '.docx'
            else:
                return redirect('/index/')
            file_id = FileInfo.objects.count() + 1
            new_file = FileInfo.objects.create(file_id = file_id)
            # new_file.file_id = file_id
            new_file.name = filename
            new_file.uploader = uploader
            new_file.owner = UserInfo.objects.filter(username=uploader)
            new_file.prices = prices
            new_file.topic = topic
            new_file.type = filetype
            new_file.src = src
            new_file.file = file
            
            new_file.save()
            #return HttpResponseRedirect(reverse('upload.views.upload'))
        else:
            #print(form.clean_data)
            print(form.errors)
        return redirect('/index/')
    else:
        username = request.session.get('user_name','None')
        form = FileForm(initial={
            'uploader':username
        }
        )
        return render(request,'upload/upload.html',{'upload_form':form})
    #    'upload/upload.html',
    #    {'uploadfile': UploadFile, 'form': form},
    #    context_instance=RequestContext(request)
    #)
