from django.shortcuts import render
from . forms import Student_login_form, Student_signup_form
from . models import Student_model
from django.http import HttpResponse, HttpResponseRedirect

def Student_signup_view(request):
    if request.method == "GET":
        form = Student_signup_form()
        return render(request,'signup.html',{'form':form})
    elif request.method == "POST":
        form = Student_signup_form(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('data submitted successfully')

def Student_login_view(request):
    if request.method == "GET":
        form = Student_login_form()
        return render(request,'login.html',{'form':form})
    elif request.method == "POST":
        form = Student_login_form(request.POST)
        if form.is_valid():
            obj = Student_model.objects.filter(name=form.cleaned_data['name'],password=form.cleaned_data['password'])
            if obj:
                return HttpResponse('login success')
            else:
                return HttpResponseRedirect('./login')

def display(request):
    obj = Student_model.objects.all()
    return render(request,'display.html',{'obj':obj})

def update(request,id):
    if request.method == 'GET':
        edit_obj = Student_model.objects.get(id=id)
        return render(request,'update.html',{'edit_obj':edit_obj})
    elif request.method == 'POST':
        edit_obj = Student_model.objects.get(id=id)
        edit_obj.name = request.POST['t1']
        edit_obj.department = request.POST['t2']
        edit_obj.picture = request.POST['t3']
        edit_obj.first_name = request.POST['t4']
        edit_obj.last_name = request.POST['t5']
        edit_obj.password = request.POST['t6']
        edit_obj.conform_password = request.POST['t7']
        edit_obj.save()
        return HttpResponseRedirect('./display')

def delete(request,id):
    delete_obj = Student_model.objects.get(id=id)
    delete_obj.delete()
    return HttpResponseRedirect('./display')
