
from django.urls import path,include
from .import views

urlpatterns = [

    path('',views.home,name='home'),
    path('book/<int:myid>/',views.newform,name='get_book'),
    path('liveSession',views.live_session,name='live_session'),
    path('booking-class',views.booking_class,name='booking_class'),
    path('AboutUs',views.about_us,name='about_us'),
    path('ContactUs',views.contact_us,name='contact_us'),
    path('Services',views.services,name='services'),

    path('virtual_counselling',views.virtual_counselling,name='virtual_counselling'),
    path('speaking_partner',views.speaking_partner,name='speaking_partner'),


    path('Essay_correction',views.Essay_correction,name='Essay_correction'),
    path('mock_test', views.mock_test, name='mock_test'),
    path('videos_lession', views.videos_lession, name='videos_lession'),
    path('short_trick', views.short_trick, name='short_trick'),
    path('ebookCollection' ,views.ebookCollection,name='ebookCollection'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),

]