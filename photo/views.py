# Create your views here.
from django.shortcuts import render
from Utils.tools import save_file
from myFirstDjangoProject.settings import FileSave_DIR
from photo.models import Photo
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    if request.session.get('success_message') == '1':       #   目前先使用 session 支持 HttpResponseRedirect 带过来的参数
        request.session['success_message'] = '0'
        return render(request,"index.html",{'success_message':'图片上传成功!'})
    return render(request, "index.html")

def upload(request):
    return render(request,"appointment.html")           # 暂时以 appointment.html 当作图片上传页面

def result(request):
    if request.method == "POST":
        # 得到图片
        photo = request.FILES.get('photo')
        pname = photo.name
        uid = -1
        purl = FileSave_DIR
        presult = 0.00
        pinfo = "no info"
        if Photo.objects.filter(photoName=pname):
            return render(request, 'appointment.html', {
                'error_message': '图片上传失败!,重名了'
            })
        if photo:
            photoModel = Photo.objects.create(photoName=pname,userId=uid,photoUrl=purl,photoResult=presult,photoInfo=pinfo)
            save_file(photo,purl)
            request.session['success_message'] = '1'
            return HttpResponseRedirect(reverse('app_name_photo:index'))
    return render(request,'appointment.html',{
        'error_message': '图片上传失败!'
    })
