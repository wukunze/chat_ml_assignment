from django.urls import path
from .views import event
from .views import advertisement
from .views import registration
from .views import club
from .views import index
from .views.merchandise import DeleteItemView, UpdateItemView, ItemDetailsView, item_create, item_display, item_exchange, item_exchange_finish
from .views import exchange
from .views import order
from .views import lend_merchandise
from .views import message

urlpatterns = [
    path("", index.index, name="home"),
    path("sign_up/", registration.sign_up, name="sign_up"),

    # story 5 : A student can CRUD events
    # ex: /ubs_project/event_list/
    path('event_list/', event.IndexView.as_view(), name='event_list'),  # show all

    # ex: /ubs_project/event_detail/
    path('event_detail/<int:pk>/', event.DetailView.as_view(), name='event_detail'),  # show event by pk

    path('event_create/', event.event_create, name='event_create'),  # GET to show the html form
    path('event_create_handler/', event.event_create_handler, name='event_create_handler'),  # POST receive data

    path('event_update/<int:pk>/', event.event_update, name='event_update'),  # GET to show the html form
    path('event_update_handler/<int:pk>/', event.event_update_handler, name='event_update_handler'),
    # POST receive data

    path('event_delete/<int:pk>/', event.event_delete, name='event_delete'),

    # Story 6: A student can CRUD exchanges
    path('exchange_list/', exchange.IndexView.as_view(), name='exchange_list'),  # show all

    path('exchange_detail/<int:pk>/', exchange.DetailView.as_view(), name='exchange_detail'),  # show exchange by pk

    path('exchange_create/', exchange.exchange_create, name='exchange_create'),  # GET to show the html form
    path('exchange_create_handler/', exchange.exchange_create_handler, name='exchange_create_handler'),
    # POST receive data

    path('exchange_update/<int:pk>/', exchange.exchange_update, name='exchange_update'),  # GET to show the html form
    path('exchange_update_handler/<int:pk>/', exchange.exchange_update_handler, name='exchange_update_handler'),
    # POST receive data

    path('exchange_delete/<int:pk>/', exchange.exchange_delete, name='exchange_delete'),

    # Story 7: A student can CRUD advertisement
    path('advertisement_list/', advertisement.IndexView.as_view(), name='advertisement_list'),  # show all

    path('advertisement_detail/<int:pk>/', advertisement.DetailView.as_view(), name='advertisement_detail'),
    # show advertisement by pk

    path('advertisement_create/', advertisement.advertisement_create, name='advertisement_create'),
    # GET to show the html form
    path('advertisement_create_handler/', advertisement.advertisement_create_handler,
         name='advertisement_create_handler'),  # POST receive data

    path('advertisement_update/<int:pk>/', advertisement.advertisement_update, name='advertisement_update'),
    # GET to show the html form
    path('advertisement_update_handler/<int:pk>/', advertisement.advertisement_update_handler,
         name='advertisement_update_handler'),  # POST receive data

    path('advertisement_delete/<int:pk>/', advertisement.advertisement_delete, name='advertisement_delete'),

    # Story 10
    path('display', item_display, name="display item"),

    path('<int:pk>/', ItemDetailsView.as_view(), name="item details"),

    path('create/', item_create, name="create item"),

    path('delete/<int:pk>/', DeleteItemView.as_view(), name='delete item'),

    path('edit/<int:pk>/', UpdateItemView.as_view(), name='edit item'),

    path('exchange_item/<int:item_id>/', item_exchange, name="exchange_item"),
    path('exchange_finish/<int:buy_id>/<int:sell_id>/', item_exchange_finish, name="exchange_finish"),

    # Story 8: A student can CRUD clubs
    path('club_list/', club.club_list, name='club_list'),  # show all
    path('club_create/', club.club_create, name='club_create'),
    path('club_create_handler/', club.club_create_handler, name='club_create_handler'),
    path('club_search/', club.club_search, name='club_search'),
    path('club_join_handler/<int:pk>/', club.club_join_handler, name='club_join_handler'),
    path('club_update/<int:pk>/', club.club_update, name='club_update'),
    path('club_update_handler', club.club_update_handler, name='club_update_handler'),
    path('club_detail/<int:pk>/', club.club_detail, name='club_detail'),
    path('club_exit/<int:pk>/', club.club_exit, name='club_exit'),
    path('club_dismiss/<int:pk>/', club.club_dismiss, name='club_dismiss'),
    # Story 9: A student/owner of the club can manage (add/delete) members
    path('club_member_list/<int:pk>/', club.club_member_list, name='club_member_list'),
    # show all club member of your own club
    path('club_member_delete/<int:club_id>/<int:user_id>/', club.club_member_delete, name='club_member_delete'),
    path('club_member_add_handler/<int:pk>/', club.club_member_add_handler, name='club_member_add_handler'),
    path('club_member_add/<int:club_id>/<int:user_id>/', club.club_member_add, name='club_member_add'),

    path("cart", order.cart, name="cart"),
    path("cart/<int:cart_line_id>", order.update_cart_quantity, name="cart_update"),
    path("cart/delete/<int:cart_line_id>", order.delete_from_cart, name="cart_delete"),
    path("cart/order", order.order_cart, name="cart_order"),
    path("orders", order.orders, name="orders"),
    path("order/<int:order_id>", order.order, name="order"),

    # story 13: A Student can lend Merchandises
    path('mlend/<int:pk>/', lend_merchandise.lend_req, name='lend_req'),
    path('mlend_req_handler', lend_merchandise.lend_req_handler, name='lend_req_handler'),
    path('mlend_list/', lend_merchandise.lend_list, name='mlend_list'),
    path('mlend_detail/<int:pk>', lend_merchandise.lend_detail, name='lend_detail'),
    path('mlend_return_handler/<int:pk>', lend_merchandise.lend_return_handler, name='mlend_return_handler'),
    path('mlend_history/', lend_merchandise.lend_history, name='lend_history'),

    # story 16/17 : A student can Send and Receive messages
    path('msg_sent/', message.SentView.as_view(), name='msg_sent'),  # show all
    path('msg_recv/', message.RecvView.as_view(), name='msg_recv'),  # show all

    path('message_detail/<int:pk>/', message.DetailView.as_view(), name='message_detail'),  # show message by pk

    path('msg_create/', message.msg_create, name='msg_create'),  # GET to show the html form
    path('msg_create_handler/', message.msg_create_handler, name='msg_create_handler'),  # POST receive data

    path('msg_group/', message.msg_group, name='msg_group'),  # GET to show the html form  
    path('msg_group_handler/', message.msg_group_handler, name='msg_group_handler'),  # POST receive data

    path('msg_delete/<int:pk>/', message.msg_delete, name='msg_delete'),


]
