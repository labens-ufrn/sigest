from django.urls import path
from .views import FuncaoList,FuncaoDetail,FuncaoCreate,FuncaoUpdate,FuncaoDelete

urlpatterns = [
    path('listar_funcao/', FuncaoList.as_view(), name='listar_funcao'),
    path('detalhar_funcao/<int:pk>/', FuncaoDetail.as_view(), name='detalhar_funcao'),
    path('criar_funcao/', FuncaoCreate.as_view(), name='criar_funcao'),
    path('atualizar_funcao/<int:pk>/', FuncaoUpdate.as_view(), name='atualizar_funcao'),
    path('deletar_funcao/<int:pk>/',
         FuncaoDelete.as_view(), name='deletar_funcao'),

]