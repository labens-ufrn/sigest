"""SigestAlfa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from funcoes import urls as funcoes_urls
from usuarios import urls as usuarios_urls
from tipos import urls as tipos_urls
from prioridades import urls as prioridades_urls
from situacoes import urls as situacoes_urls
from tarefas import urls as tarefas_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('funcoes/', include(funcoes_urls)),
    path('usuarios/',include(usuarios_urls)),
    path('tipos/',include(tipos_urls)),
    path('prioridades/',include(prioridades_urls)),
    path('situacoes/',include(situacoes_urls)),
    path('tarefas/', include(tarefas_urls)),


]
