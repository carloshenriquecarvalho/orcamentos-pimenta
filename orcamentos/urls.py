from django.urls import path
from orcamentos.views import home, control_panel

# configurando urls
urlpatterns = [
    path('', home),
    path('painel', control_panel)
]

