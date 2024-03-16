from django.shortcuts import render

def home(request):
    return render(request,'homepage.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'CONTACT.html')
def login(request):
    if request.method=="post":
        un=request.post['USERNAME']
        pw=request.post['PASWORD']
        print("USERNAME=",un)
        print("PASSWORD=",pw)
    return render(request,'login.html')
def reg(request):
    return render(request,'registration form.html')
