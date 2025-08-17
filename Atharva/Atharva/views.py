from django.shortcuts import render
from .sevises import MarvelFilmOperations
import pymysql

def index(request):
    return render(request,'index.html')


def home(request):
    return render(request,'home.html')

def login(request):
    if request.method=='POST':
        uid=request.POST.get('username')
        psw=request.POST.get('password')
        if uid=='atharva chavhan' and psw=='atharva@123':
            #request.session['username']=id
           # request.session['password']=psw
            
            page='home.html'

        else:
            page='loginfail.html'
    return render(request,page)

def printallmarvelmoviesinsequence(request):
    obj=MarvelFilmOperations()
    data=obj.allmarvelmoviesinsequence()
    return render(request,'allmarvelmoviesinsequence.html',{'filmdata':data})

def createsuperhero(request):
    return render(request,'createsuperhero.html')

def addsuperhero(request):
    if request.method=='POST':
        try:  
            hero_name=request.POST.get('hero_name')
            real_name=request.POST.get('real_name')
            title=request.POST.get('title')
            origin_story=request.POST.get('origin_story')
            species=request.POST.get('species')
            superpowers=request.POST.get('superpowers')
            weakness=request.POST.get('weakness')
            gadgets=request.POST.get('gadgets')
            team=request.POST.get('team')
            description=request.POST.get('description')
            # print(f'{hero_name}{real_name}{title}{origin_story}{species}{superpowers}{weakness}{gadgets}{team}{description}')

            obj=MarvelFilmOperations()
            mess=obj.addsuperhero(hero_name,real_name,title,origin_story,species,superpowers,weakness,gadgets,team,description)
            print(mess)
        except:
            print("error ocure ")
    return render(request,'superheroadded.html')

def searchsuperhero(request):
    return render(request,'searchsuperhero.html')

def displaysuperhero(request):
    if request.method=="POST":
        
            hero_name=request.POST.get('hero_name')
            #print(hero_name)
            obj = MarvelFilmOperations()  
            superhero= obj.displaysuperhero(hero_name)  
            if not superhero:  # Check if superhero data is empty
                return render(request, 'not_found.html', {"message": "Superhero not found!"})
            print(superhero)
            return render (request,'displaysuperhero.html',{"superhero":superhero})

def fanstory(request):
    return render(request,'fanstory.html')

def addfanstory(request):
    return render(request,'addfanstory.html')

def submitfanstory(request):
    if request.method=="POST":
        try:
            title=request.POST.get('title')
            author=request.POST.get('author')
            content=request.POST.get('content')
            
            print(f"{title}{author}{content}{title}")
            obj=MarvelFilmOperations()
            data=obj.submitfanstory(title,author,content)
            return render(request,'storyadded.html')
        except:
            return render (request,'storynotadded.html')

def showfanstory(request):
         con=pymysql.connect(host='mysql-python-rahul-python.c.aivencloud.com',port=20349,user='avnadmin',password='AVNS_0IC9WqSB0H-_cdAII8e',database='marvel_project')
         curs=con.cursor()
         curs.execute("SELECT id, title, author, content, created_at FROM fan_stories ORDER BY created_at DESC")
         stories=curs.fetchall()
         con.commit()
         con.close()
         return render(request,'displayfanstory.html',{"stories":stories})

def serchmoviename(request):
    return render(request,'serchmoviename.html')

def downlodmovietourl(request):
    if request.method=='POST':
        try:
            name=request.POST.get('name')
            print(name)
            obj=MarvelFilmOperations()
            data=obj.downlodmovietourl(name)
            if data:
                return render(request,'downloadmovie.html',{"data":data})
            else:
                return render(request,"movienotfound.html")
        except:
           return render(request,"movienotfound.html")
    
def upcomeingmarvelmovies(request):
    try:
        obj=MarvelFilmOperations()
        data=obj.upcomeingmarvelmovies()
        return render(request,'upcomeingmarvelmovies.html',{"data":data})
    except  :
        print("not any upcoming movies")

   