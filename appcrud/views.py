from django.shortcuts import render, get_object_or_404, redirect
from .forms import AppcrudForm
from .models import Appcrud
from django.utils import timezone

# Create your views here.
def home(request):
    appcruds=Appcrud.objects
    return render(request, 'home.html', {'appcruds':appcruds})

def post(request):
    if request.method == "POST":
        form = AppcrudForm(request.POST) 
        if form.is_valid(): 
            appcrud = form.save(commit=False)
            appcrud.update_date=timezone.now()
            appcrud.save()
            return redirect('home')
    else:
        form = AppcrudForm() 
        return render(request, 'post.html',{'form' : form})

def detail(request, appcrud_id):
    appcrud_detail=get_object_or_404(Appcrud, pk=appcrud_id)
    return render(request, 'detail.html', {'appcrud': appcrud_detail})

def edit(request, pk):
    appcrud= get_object_or_404(Appcrud, pk=pk) 
    if request.method == "POST":
        form = AppcrudForm(request.POST, instance =appcrud)
        if form.is_valid():
            appcrud = form.save(commit=False)
            appcrud.update_date=timezone.now()
            appcrud.save()
            return redirect('home')
    else:
            form = AppcrudForm(instance =appcrud)
            return render(request, 'edit.html',{'form' : form})

def delete(request, pk):
    appcrud =Appcrud.objects.get(id=pk)
    appcrud.delete()
    return redirect('home')