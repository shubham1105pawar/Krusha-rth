from django.shortcuts import render,redirect

from .models import Crops, Diseases,Pesticides,PesticideDisease,Rating,Question,Answers

from django.contrib.auth.models import User,auth

from django.views.decorators.csrf import csrf_exempt

def home(request):
    crops = Crops.objects.all();
    
    return render(request,'KrishiGyan/home.html',{'Crops':crops})


def Disease(request,crop='wheat'):
    
    Disease =  Diseases.objects.filter(Crop=crop);
     
    return render(request,'KrishiGyan/Disease.html',{'Diseases':Disease,'crop':crop})



def Pesticide(request,disease='',crop=''):
    
    Disease =  Diseases.objects.filter( Disease_Name = disease);
    Pesticide =  PesticideDisease.objects.filter(Disease_name  = disease);
    Pesticid=[] 
    z=[]
    for p in Pesticide:
        c=[]
        Pesticid.append(p.Pesticide_name)
        x = Rating.objects.filter(Disease=disease,Pesticide=p.Pesticide_name,Up_vote=1)    
        c.append(x.count())              
        x = Rating.objects.filter(Disease=disease,Pesticide=p.Pesticide_name,Down_vote=1)    
        c.append(x.count())             
        z.append(c) 
    y = zip(Pesticid,z)                              
    
    return render(request,'KrishiGyan/Pesticide.html',{'Pesticides':y,'Disease':Disease,'crop':crop})


def Aboutus(request):
     
    
    return render(request,'KrishiGyan/About.html')


def Login(request):
    crops = Crops.objects.all();
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = auth.authenticate(request, username=username, password=password)
       if user is not None:
           
           
           auth.login(request, user)
           return render(request,'KrishiGyan/home.html',{'Crops':crops,'msg':'Your successfully Loged-in'}) 
       else:
            
           return render(request,'KrishiGyan/home.html',{'Crops':crops,'msg':'Please Retry '}) 

def Logout(request):
    crops = Crops.objects.all();
    auth.logout(request)
    return render(request,'KrishiGyan/home.html',{'Crops':crops,'msg':'Successfully loged off'}) 


def Register(request):
    crops = Crops.objects.all();
    if request.method == 'POST':
        First_name = request.POST['first_name']
        Last_name  = request.POST['last_name']
        Username   = request.POST['username']
        Email      = request.POST['email']
        Password   = request.POST['password']
        CPassword  = request.POST['confirm_password']
        
        if Password==CPassword:
            if User.objects.filter(email=Email).exists():
     
                return render(request,'KrishiGyan/home.html',{'Crops':crops,'msg':'Email Already Exist'})
            
            elif User.objects.filter(username=Username).exists():
          
                return render(request,'KrishiGyan/home.html',{'Crops':crops,'msg':'username Already Exist'}) 
            
            else :
                
                user = User.objects.create_user(username=Username,password=Password,email=Email,first_name=First_name,last_name=Last_name)
                
                user.save();
               
                return render(request,'KrishiGyan/home.html',{'Crops':crops,'msg':'Welcome '+ First_name})
        else:
             
              
             return render(request,'KrishiGyan/home.html',{'Crops':crops,'Msg':'Please Re-enter Password'})
        
    else:
        
        return  redirect('/')
@csrf_exempt           
def upvote(request,disease='',pesticide='',crop=''):
    
    
    Disease =  Diseases.objects.filter( Disease_Name = disease);
    Pesticide =  PesticideDisease.objects.filter(Disease_name  = disease);
    Pesticid=[] 
    
    for p in Pesticide:
        Pesticid.append(p.Pesticide_name)
        
                               
    if request.user.is_authenticated :
        
        if request.method == 'POST':
            ob = Rating.objects.filter(Email=request.user.email,Disease=disease,Pesticide=pesticide)
            if request.POST.get("upvote"):
                   
                   if ob.exists():
                       ob.update(Up_vote=1,Down_vote=0)
                       
                       
                   else:
                       user = Rating(Email=request.user.email,Disease=disease,Pesticide=pesticide,Up_vote=1,Down_vote=0)
                
                       user.save()
             
            else:
                 if ob.exists():
                       ob.update(Up_vote=0,Down_vote=1)
                 else:
                      user = Rating(Email=request.user.email,Disease=disease,Pesticide=pesticide,Up_vote=0,Down_vote=1)
                
                      user.save()
        z=[]
        for p in Pesticide:
            c=[]
            x = Rating.objects.filter(Disease=disease,Pesticide=p.Pesticide_name,Up_vote=1)    
            c.append(x.count())              
            x = Rating.objects.filter(Disease=disease,Pesticide=p.Pesticide_name,Down_vote=1)    
            c.append(x.count())             
            z.append(c) 
        y = zip(Pesticid,z)    
        return render(request,'KrishiGyan/Pesticide.html',{'Pesticides':y,'Disease':Disease,'msg':'Your response is recorded','crop':crop})
    
    else:
        z=[]
        for p in Pesticide:
            c=[]
            x = Rating.objects.filter(Disease=disease,Pesticide=p.Pesticide_name,Up_vote=1)    
            c.append(x.count())              
            x = Rating.objects.filter(Disease=disease,Pesticide=p.Pesticide_name,Down_vote=1)    
            c.append(x.count())             
            z.append(c)  
        y = zip(Pesticid,z)    
        return render(request,'KrishiGyan/Pesticide.html',{'Pesticides':y,'Disease':Disease,'msg':'Please login to vote ','crop':crop})
    
def Questions(request,EMAIL=''):
    
    if EMAIL != 'xyz':
        ques = Question.objects.filter(Email=EMAIL)
    else:
        
        ques = Question.objects.all()
        
    return render(request,'KrishiGyan/Question.html',{'Questions':ques})

def AddQuestion(request):
       crops = Crops.objects.all();
       if request.method == "POST" and request.user.is_authenticated:
           CropName = request.POST['crop']
           Questions  = request.POST['Question']
           Image   = request.FILES.get('img',"default.png")
           
           print(Image) 
           user = Question(Email=request.user.email,CropName=CropName,Questions=Questions,image=Image)
           user.save()
           ques = Question.objects.all()
           
           return render(request,'KrishiGyan/Question.html',{'Questions':ques})

       else:
           
           return render(request,'KrishiGyan/home.html',{'Crops':crops,'msg':'Please Log-in'}) 

def Addanswer(request):
       
       if request.method == "POST" and request.user.is_authenticated:
           fid = int(request.POST['crop'])
           obj = Question.objects.get(pk=fid)
           answer  = request.POST['Answer']
           
           user = Answers(Email=request.user.email,UserName=request.user.username,Answer=answer,Qid=obj)
           user.save()
    
           ans = Answers.objects.filter(Qid=fid)
           ques = Question.objects.filter(pk=fid)
           return render(request,'KrishiGyan/Answers.html',{'Answers':ans,'Question':ques})

def answers(request,qid=''):
    if qid.isnumeric():
        ans = Answers.objects.filter(Qid=qid)
        ques = Question.objects.filter(pk=qid)
        return render(request,'KrishiGyan/Answers.html',{'Answers':ans,'Question':ques})
    else:
        ans = Answers.objects.filter(Email=qid)
        return render(request,'KrishiGyan/Answers.html',{'Answers':ans})

def ans_del(request,Aid=''):
     
    try:
        user = Answers.objects.get(pk=Aid)
    except Answers.DoesNotExist:
        user = None
    if user: 
        user.delete()    
    ans=Answers.objects.all()
    return render(request,'KrishiGyan/Answers.html',{'Answers':ans})

def ques_del(request,Qid=''):
     
    try:
        user = Question.objects.get(pk=Qid)
    except Question.DoesNotExist:
        user = None
    if user: 
        user.delete()    
    ans=Question.objects.all()
    return render(request,'KrishiGyan/Question.html',{'Questions':ans})
