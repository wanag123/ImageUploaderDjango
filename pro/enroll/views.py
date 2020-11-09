from django.shortcuts import render ,redirect
from .foms import ImageForm
from .models import Image

def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
        image = Image.objects.all()
    else:
        image = Image.objects.all()
        form = ImageForm() 
    return render(request, 'enroll/home.html' , {'img':image ,'form':form})

def delete_img(request,id):
    if request.method == 'POST':
        pi = Image.objects.get(pk=id)
        pi.delete()
        return redirect('/')