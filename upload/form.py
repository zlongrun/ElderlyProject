from django import forms

class FileForm(forms.Form):
    type = (
        ('.pdf','pdf'),
        ('.docx','word'),
    )
    filename = forms.CharField(label='文件名',max_length=32,widget=forms.TextInput(attrs={'class': 'form-control'}))
    filetype = forms.ChoiceField(label="文件类型", choices=type)
    filesrc = forms.FileField(label='请选择文件', help_text='max. 42 megabytes')
    prices = forms.IntegerField(label='购买所需积分', widget=forms.TextInput(attrs={'class': 'form-control'}))
    topic = forms.CharField(label='文件主题',max_length=500,widget=forms.TextInput(attrs={'class': 'form-control'}))