from django.urls import path
from .views import TarefaList, TarefaDetail,TarefaCreate,  TarefaUpdate, TarefaDelete

urlpatterns = [
    path('listar_tarefa/', TarefaList.as_view(), name='listar_tarefa'),
    path('detalhar_tarefa/<int:pk>/', TarefaDetail.as_view(), name='detalhar_tarefa'),
    path('criar_tarefa/', TarefaCreate.as_view(), name='criar_tarefa'),
    path('atualizar_tarefa/<int:pk>/', TarefaUpdate.as_view(), name='atualizar_tarefa'),
    path('deletar_tarefa/<int:pk>/', TarefaDelete.as_view(), name='deletar_tarefa'),

]