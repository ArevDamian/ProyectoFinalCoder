from django.urls import path
from MyBus import views

urlpatterns = [
    path('', views.Principal, name='Principal'),
    path('colectivo/', views.colectivos, name='Colectivos'),
    path('colectivocreat/', views.Colectivocreat.as_view(), name='Crearc'),
    path('colectivolist/', views.Colectivolist.as_view(), name='Listac'),
    path('colectivoedit/<pk>', views.Colectivoedit.as_view(), name='Editarc'),
    path('colectivodetail/<pk>', views.Colectivodetail.as_view(), name='Detallec'),
    path('colectivodelete/<pk>', views.Colectivodelete.as_view(), name='Eliminarc'),
    path('recorrido/', views.recorridos, name='Recorrido'),
    path('recorridocreat/', views.Recorridoscreat.as_view(), name='Crearr'),
    path('recorridolist/', views.Recorridolist.as_view(), name='Listar'),
    path('recorridoedit/<pk>', views.Recorridoedit.as_view(), name='Editarr'),
    path('recorridodetail/<pk>', views.Recorridodetail.as_view(), name='Detaller'),
    path('recorriodelete/<pk>', views.Recorridodelete.as_view(), name='Eliminarr'),
    path('tarifas/', views.tarifas, name='Tarifas'),
    path('tarifascreat/', views.Tarifascreat.as_view(), name='Creart'),
    path('tarifaslist/', views.Tarifaslist.as_view(), name='Listat'),
    path('tarifaedit/<pk>', views.Tarifasedit.as_view(), name='Editart'),
    path('tarifasdetail/<pk>', views.Tarifasdetail.as_view(), name='Detallet'),
    path('tarifasdelete/<pk>', views.Tarifasdelete.as_view(), name='Eliminart'),
    path('colectivoapi/', views.colectivoApi),
    path('recorridoapi/', views.recorridoApi),
    path('tarifaapi/', views.tarifaApi),
    path('busqueda/', views.busqueda, name='Buscar'),
    path('buscar/', views.buscar),
    path('busquedarecorrido/', views.busquedarecorrido, name='Buscarr'),
    path('buscarrecorrido/', views.buscarrecorrido),
    path('busquedatarifa/', views.busquedatarifa, name='Buscart'),
    path('buscartarifa/', views.buscartarifa)
    ]   