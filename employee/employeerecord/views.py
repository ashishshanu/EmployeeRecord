from django.http.response import Http404
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from .models import EmployeeModel
from employeerecord import forms
from .forms import EmployeeForm

# Create your views here.

def create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/data')
    else:
        form =EmployeeForm()
        context = {
            'form':form
        }
        return render(request,'create.html',context)

###########################################################################################################
###########################################################################################################
 
def retrieve_listView(request):
    dataset = EmployeeModel.objects.all()
    return render(request,'retrive.html',{'dataset':dataset})
 
def retrieve_detailView(request,_id):
    try:
        data =EmployeeModel.objects.get(id =_id)
    except EmployeeModel.DoesNotExist:
        raise Http404('Data does not exist')
 
    return render(request,'detailview.html',{'data':data})

###########################################################################################################
###########################################################################################################

def Update(request,_id):
    try:
        old_data = get_object_or_404(EmployeeModel,id =_id)
    except Exception:
        raise Http404('Does Not Exist')
 
    if request.method =='POST':
        form =EmployeeForm(request.POST, instance =old_data)
 
        if form.is_valid():
            form.save()
            return redirect(f'/data/{_id}')
     
    else:
 
        form = EmployeeForm(instance = old_data)
        context ={
            'form':form
        }
        return render(request,'update.html',context)

###########################################################################################################
###########################################################################################################

def DeleteView(request,_id):
    try:
        data = get_object_or_404(EmployeeModel,id =_id)
    except Exception:
        raise Http404('Does Not Exist')
 
    if request.method == 'POST':
        data.delete()
        return redirect('/data')
    else:
        return render(request, 'delete.html')