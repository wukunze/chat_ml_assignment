from django.urls import path
from .views import event
from .views import advertisement
from .views import registration
from .views import club
from .views import index
from .views import exchange

urlpatterns = [
    path("", index.index, name="home"),
    path("sign_up/", registration.sign_up, name="sign_up"),

    # story 5 : A student can CRUD events
    # ex: /ubs_project/event_list/
    path('event_list/', event.IndexView.as_view(), name='event_list'), # show all

    # ex: /ubs_project/event_detail/
    path('event_detail/<int:pk>/', event.DetailView.as_view(), name='event_detail'), # show event by pk

    path('event_create/', event.event_create, name='event_create'),  # GET to show the html form
    path('event_create_handler/', event.event_create_handler, name='event_create_handler'),  # POST receive data

    path('event_update/<int:pk>/', event.event_update, name='event_update'), # GET to show the html form
    path('event_update_handler/<int:pk>/', event.event_update_handler, name='event_update_handler'), # POST receive data

    path('event_delete/<int:pk>/', event.event_delete, name='event_delete'),


    # Story 7: A student can CRUD advertisement
    path('advertisement_list/', advertisement.IndexView.as_view(), name='advertisement_list'), # show all

    path('advertisement_detail/<int:pk>/', advertisement.DetailView.as_view(), name='advertisement_detail'), # show advertisement by pk

    path('advertisement_create/', advertisement.advertisement_create, name='advertisement_create'),  # GET to show the html form
    path('advertisement_create_handler/', advertisement.advertisement_create_handler, name='advertisement_create_handler'),  # POST receive data

    path('advertisement_update/<int:pk>/', advertisement.advertisement_update, name='advertisement_update'), # GET to show the html form
    path('advertisement_update_handler/<int:pk>/', advertisement.advertisement_update_handler, name='advertisement_update_handler'), # POST receive data

    path('advertisement_delete/<int:pk>/', advertisement.advertisement_delete, name='advertisement_delete'),

    # Story 8: A student can CRUD clubs
    path('club_list/', club.club_list, name='club_list'), # show all
    path('club_create/', club.club_create, name='club_create'),
    path('club_create_handler/', club.club_create_handler, name='club_create_handler'),
    path('club_search/', club.club_search, name='club_search'),
    path('club_join_handler/<int:pk>/', club.club_join_handler, name='club_join_handler'),
    path('club_update/<int:pk>/', club.club_update, name='club_update'),
    path('club_update_handler', club.club_update_handler, name='club_update_handler'),
    path('club_detail/<int:pk>/', club.club_detail, name='club_detail'),
    path('club_exit/<int:pk>/', club.club_exit, name='club_exit'),
    path('club_dismiss/<int:pk>/', club.club_dismiss, name='club_dismiss'),

    # Story : A student can CRUD exchanges
    path('exchange_list/', exchange.IndexView.as_view(), name='exchange_list'), # show all

    path('exchange_detail/<int:pk>/', exchange.DetailView.as_view(), name='exchange_detail'), # show exchange by pk

    path('exchange_create/', exchange.exchange_create, name='exchange_create'),  # GET to show the html form
    path('exchange_create_handler/', exchange.exchange_create_handler, name='exchange_create_handler'),  # POST receive data

    path('exchange_update/<int:pk>/', exchange.exchange_update, name='exchange_update'), # GET to show the html form
    path('exchange_update_handler/<int:pk>/', exchange.exchange_update_handler, name='exchange_update_handler'), # POST receive data

    path('exchange_delete/<int:pk>/', exchange.exchange_delete, name='exchange_delete'),
]

