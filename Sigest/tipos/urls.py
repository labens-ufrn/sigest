from django.urls import path
from .views import TipoList, TipoDetail,TipoCreate,  TipoUpdate, TipoDelete

urlpatterns = [
    path('listar_tipo/', TipoList.as_view(), name='listar_tipo'),
    path('detalhar_tipo/<int:pk>/', TipoDetail.as_view(), name='detalhar_tipo'),
    path('criar_tipo/', TipoCreate.as_view(), name='criar_tipo'),
    path('atualizar_tipo/<int:pk>/', TipoUpdate.as_view(), name='atualizar_tipo'),
    path('deletar_tipo/<int:pk>/', TipoDelete.as_view(), name='deletar_tipo'),

]