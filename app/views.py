from django.shortcuts import redirect, render
from .models import data
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        
        q1=request.POST['q1']
        q2=request.POST['q2']
        q3=request.POST['q3']
        q4=request.POST['q4']
        q5=request.POST['q5']

        if  q1!='' and q2!='' and q3!='' and q4!='' and q5!='':
            detail=data.objects.create(q1=q1, q2=q2, q3=q3 ,q4=q4 , q5=q5)
            detail.save()
            messages.info(request,"Thank you "+ q1,extra_tags='done')
       
        else:
           messages.info(request, "please fill vaild details",extra_tags='error')
           
        '''if detail!=e
            messages.info(request,"INVALID DETAILS")'''

    return render(request,'index.html')

def detail(request):
    detail=data.objects.all()
    return render(request,"detail.html",{'detail':detail})

def delete(request,id):
    detail=data.objects.get(id=id)
    detail.delete()
    return redirect('detail')