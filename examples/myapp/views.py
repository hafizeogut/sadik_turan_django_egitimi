from django.http.response import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.shortcuts import render,redirect

from django.urls import reverse
# Create your views here.

#Ansayfa yönlendireek bşr donksiyon yazılıyor.
#request:rica,talep istenilen sayfa

#adres:http://127.0.0.1:8000/ #ana url
#URL=uNİFORM RESOURCE LOCATOR= tek tip kaynak bulucu

data={
    "telefon":["samsung s20","samsung s21"],
    "bilgisayar":["laptop 1","laptop 2"],
    "elektronik":[],
}
def index (request):
    category_list=list(data.keys())
    return render(request,'myapp/index.html',{
        "categories":category_list
    })


def details(request):
    return HttpResponse("details")

# def list(request):
#     return HttpResponse("list")


def getProductsByCategoryID(request,category_id):
    #url yönlendirmesi ile telefon kategorisine yönlendiriliyor.
    #
    
    category_list=list(data.keys())#["telefon","bilgisayar",elektronik]
    
    if category_id>len(category_list):
        return HttpResponseNotFound("Yanlış kategori seçimi")
    
    category_name=category_list[category_id-1]
    
    #reverse fonksiyonu ile name göre bir yönlendirme yapılıyor.
    redirect_path=reverse("products_by_category",args=[category_name])
    
    return redirect(''+redirect_path)



def getProductsByCategory(request,category):
    # category_text=None
    # if category=='bilgisayar':
    #     category_text="bilgisayar kategorisndeki ürünler"
    # elif category=='telefon':
    #     category_text="telefon kategorisndeki ürünler"
    # else:
    #     category_text="Yanlış seçim yaptınız"
    # return HttpResponse(category_text) 
    
    try:
        products=data[category] 
        return render(request,'myapp/products.html',{
            "category":category,
            "products":products
        })
    except:
        return HttpResponseNotFound(f"<h1> Yanlış kategori secimi </h1>")
        
 