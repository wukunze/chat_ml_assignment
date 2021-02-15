from django.urls import path
from . import views

# function path()  parameter :    route  , view ,  kwargs,  name
# the 'name' value as called by the {% url %} template tag

app_name = 'ubs' # url namespace
urlpatterns = [
    # ex: /ubs/
    path('', views.index, name='index'),

    # ex: /ubs/index2
    path('index2', views.index2, name='index2'),


    # ex: /ubs/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /ubs/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /ubs/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]



