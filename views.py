#from django.template.loader import get_template
#from django.template import Template, Context

from django.http import HttpResponse
from django.shortcuts import render_to_response
from ge.models import Author,Book

def search_form(request):
    
    return render_to_response('search_form.html')

def summary(request):

    authors = Author.objects.all()
    books = Book.objects.all()
    return render_to_response('summary.html',locals())

def add_form(request):

    return render_to_response('add_form.html')

def add_result(request):

    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    d = request.GET['d']
    
    e = request.GET['e']
    f = request.GET['f']
    g = request.GET['g']
    h = request.GET['h']
    i = request.GET['i']
    j = request.GET['j']
    p = Author(AuthorID=a,Name=b,Age=c,Country=d)
    p.save()
    q = Book(ISBN=e,Title=f,AuthorID_id=g,Publisher=h,Publishdate=i,Price=j)
    q.save()
    return render_to_response('add_result.html')

def search_result(request):
    
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        authorid = Author.objects.filter(Name=q)
        book = Book.objects.filter(AuthorID=authorid)
        return render_to_response('search_result.html', locals())
    
    else:   
        return render_to_response('search_form.html', {'error': True})

def information(request):
    
    if 'book_title' in request.GET and request.GET['book_title']:
        book_title = request.GET['book_title']       
        book = Book.objects.get(Title=book_title)
        author_id =  book.AuthorID
        author = Author.objects.get(AuthorID=author_id)
        return render_to_response('information.html', {'book':book, 'author':author})

def delete(request):
    
    if'booktitle' in request.GET and request.GET['booktitle']:
        booktitle = request.GET['booktitle']
        Book.objects.get(Title=booktitle).delete()
        return render_to_response('delete.html') 
    

