from django.urls import path

#aynı dizin içerisindeki dosyaları tarayarak wievs ile bağlantı kuruluyor.
from.import views

#http://127.0.0.1:8000/products =>index
#http://127.0.0.1:8000/details =>details
#http://127.0.0.1:8000/list =>list


#examples uygulamasındaki path('products/',include('myapp.urls')) sonrası
#http://127.0.0.1:8000/products =>index
#http://127.0.0.1:8000/products/details =>details
#http://127.0.0.1:8000/products/list =>list
urlpatterns = [
    #views dosyasından index metodu getirildi.
    path('',views.index,name="index"),
    path('index',views.index,name="index"),
    path('details',views.details,name='details'),
    #path('list',views.list,name='list'),
    path('<int:category_id>',views.getProductsByCategoryID),
    path('<str:category>',views.getProductsByCategory,name='products_by_category')
 
    
]
