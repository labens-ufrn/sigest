from django.urls import path
from .views import SituacaoList, SituacaoDetail,SituacaoCreate,  SituacaoUpdate, SituacaoDelete

urlpatterns = [
    path('listar_situacao/', SituacaoList.as_view(), name='listar_situacao'),
    path('detalhar_situacao/<int:pk>/', SituacaoDetail.as_view(), name='detalhar_situacao'),
    path('criar_situacao/', SituacaoCreate.as_view(), name='criar_situacao'),
    path('atualizar_situacao/<int:pk>/', SituacaoUpdate.as_view(), name='atualizar_situacao'),
    path('deletar_situacao/<int:pk>/', SituacaoDelete.as_view(), name='deletar_situacao'),

]