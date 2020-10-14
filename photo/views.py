# Create your views here.
from django.shortcuts import render,redirect
from Utils.tools import save_file
from myFirstDjangoProject.settings import FileSave_DIR
from photo.models import Photo

def index(request):
    return render(request,"index.html")

def upload(request):
    return render(request,"appointment.html")           # 暂时以 appointment.html 当作图片上传页面

def result(request):
    if request.method == "POST":
        # 得到图片
        photo = request.FILES.get('photo')
        pname = request.POST.get('photoName')
        uid = -1
        purl = FileSave_DIR
        presult = 0.00
        pinfo = "no info"
        if photo:
            photoModel = Photo.objects.create(photoName=pname,userId=uid,photoUrl=purl,photoResult=presult,photoInfo=pinfo)
            save_file(photo,pname,purl)
    return redirect('/')                  # 暂时以 index.html 当作上传图片成果页面