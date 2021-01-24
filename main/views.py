from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Book

def homepage(request):
    todo_list = ToDo.objects.all()
    return render(request, "index.html", {"todo_list": todo_list})

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
    return render(request, "books.html", {"book_list": books_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(homepage)

def add_books(request):
    form = request.POST
    title = form["title"]
    subtitle = form["subtitle"]
    description = form["description"]
    price = form["price"]
    genre = form["genre"]
    author = form["author"]
    year = form["year"]
    book = Book(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    book.save()

    return redirect(books)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(homepage)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    if todo.is_favorite:
        todo.is_favorite = False
    else:
        todo.is_favorite = True
    todo.save()
    return redirect(homepage)