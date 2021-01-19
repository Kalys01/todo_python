from django.shortcuts import render, HttpResponse
from .models import ToDo, Book

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This‌ ‌is‌ ‌page‌ ‌test3.")


def add(request):
    return render(request, "add.html")


def update(request):
    return render(request, "update.html")


def delete(request):
    return render(request, "delete.html")
    
def books(request):
    books_list = Book.objects.all()
    return render(request, "books.html", {"books_list": books_list})