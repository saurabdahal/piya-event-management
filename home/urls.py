from django.contrib import admin
from django.urls import path
from home import views
# In your urls.py
from django.conf import settings
from django.conf.urls.static import static
from .views import register
    


urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("gallery", views.gallery, name='gallery'),
    path("contact", views.contact, name='contact'),
    path("login", views.login_user, name='login'),
    path("register", views.register, name='register'),
    path("profile", views.profile, name='profile'),
    path("seed", views.seed_data, name='seed'),

    path("events", views.list_event, name='list_events'),
    path("events/add", views.add_event, name='add_event'),
    path("events/my", views.list_my_events, name='list_my_events'),
    path("events/my/events/<int:e_id>", views.view_my_event, name='view_my_event'),
    path("events/book", views.book_events, name='book_events'),
    path("events/book/edit/<int:id>", views.edit_events, name='edit_events'),
    path("events/book/delete/<int:id>", views.delete_event, name='delete_events'),
    path("events/detail/<int:e_id>", views.view_event_detail, name='events_detail'),
    path("events/my/ticket/<int:e_id>", views.view_event_ticket, name='ticket'),
    path("events/my/cart/<int:e_id>", views.event_ticket_cart, name='cart'),
    path("events/my/checkout/<int:e_id>", views.purchase_event_ticket, name='checkout'),

    path("logout", views.logout_user, name='logout'),
    ] 


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)