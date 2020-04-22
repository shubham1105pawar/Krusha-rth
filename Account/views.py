from django.shortcuts import render


def Register(request):
     
    return render(request,'Account/Register.html')

def Login(request):
     
    return render(request,'KrishiGyan/home.html',{"data":'sfdfd'})

