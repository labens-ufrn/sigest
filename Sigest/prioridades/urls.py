from django.urls import path
from .views import PrioridadeList, PrioridadeDetail,PrioridadeCreate,  PrioridadeUpdate, PrioridadeDelete

urlpatterns = [
    path('listar_prioridade/', PrioridadeList.as_view(), name='listar_prioridade'),
    path('detalhar_prioridade/ <int:pk>/', PrioridadeDetail.as_view(), name='detalhar_prioridade'),
    path('criar_prioridade/', PrioridadeCreate.as_view(), name='criar_tipo'),
    path('atualizar_prioridade/<int:pk>/', PrioridadeUpdate.as_view(), name='atualizar_prioridade'),
    path('deletar_prioridade/<int:pk>/', PrioridadeDelete.as_view(), name='deletar_prioridade'),

]