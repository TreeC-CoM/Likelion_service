from django.shortcuts import render, get_object_or_404, redirect
from .models import Visitor
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    visitor = Visitor.objects

    visitor_list = Visitor.objects.all()
    pag = Paginator(visitor_list, 2)
    page = request.GET.get('page')
    posts = pag.get_page(page)

    return render(request, 'home.html', {'visitor': visitor, 'posts': posts})

def details(request, visitor_id):
    #pk를 괜히 primary_key로 쓰지 말자. 오류 난다.
    details = get_object_or_404(Visitor, pk = visitor_id)
    return render(request, "details.html", {'details': details})

def new(request):
    return render(request, 'new.html')

def create(request):
    visitor = Visitor()
    visitor.title = request.GET['title']
    visitor.description = request.GET['description']
    #visitor.pub_date = timezone.datetime.now()
    visitor.save()
    return redirect('/')
    #visitor.id 가 문제가 생긴 건지 실행이 안 된다...뭐가 문제일까
    return redirect('/visitor/'+str(visitor.id))
    #create -> save -> redirect
