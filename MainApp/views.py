from django.shortcuts import render, HttpResponse, Http404
from MainApp.models import Item

name = "Наталья"
surname = "Лазуренко"
email = "developer@nlazurenko.ru"
phone = "8-900-678-90-78"




def home(request):
    # text = f"""<h1> "Изучаем django"</h1> <strong>  Автор <i> {surname} Н.С. </i></strong>"""
    # return HttpResponse(text)
    return render(request,"index.html")


def about(request):
    # info = f"""  Имя: <b>{name}</b> <br>
    #         Фамилия:<b> {surname} </b><br>
    #         телефон: <b>8-923-600-01-02</b> <br>
    #         email: <b>developer@nlazurenko.ru</b>"""
    # return HttpResponse(info)
    context = {
        "name": "Наталья",
        "surname": "Лазуренко",
        "phone": "8-900-678-90-78",
        "email":  "developer@nlazurenko.ru"
    }
    return render(request,"about.html",context)
items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 4, "name": "Картофель фри" ,"quantity":0},
   {"id": 5, "name": "Кепка" ,"quantity":124},
]
def item_page(request,id):
    for item in items:
        if item["id"] == id:
            # item_str = f"товар {item['name']} количество{item['quantity']}"
            # return HttpResponse(item_str)
            return render(request,"item_page.html",item)
    #return HttpResponse(f"Товар с id = {id} не найден")
    raise Http404(f"Товар с id = {id} не найден")
def items_list(request):
    # items_result = "<ol>"
    # for item in items:
    #     items_result += "<li>" + f"<a href = '/item/{item['id']}'>" + item['name'] + "</li>"
    # items_result += "</ol>"
    #
    # return HttpResponse(items_result)
    items = Item.object.all()
    context = {
        "items": items
    }
    return render(request,"items.html",context)



# ctrl + alt + l
