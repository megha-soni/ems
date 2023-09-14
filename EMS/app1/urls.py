from django.urls import path
from . import views

urlpatterns = [

    # ---------------user urls------------------
    path('',views.homepage,name='home'),
    path('uregister/',views.ureges,name='ureges'),
    path('uinsert/',views.uinsert,name='uinsert'),
    path('userlogpage',views.uloginp,name='userlogpage'),
    path('ulogin/',views.userlogin,name="userlog"),


    # ----------------admin urls---------------
    path("aregister/",views.areges,name="areges"),
    path("ainsert/",views.ainsert,name="ainsert"),
    path('alogpage/',views.aloginp,name='alogpage'),
    path('alogin/',views.adminlogin,name='adminlog'),

    #----------------enquiry--------------------
    path("enquiry/",views.enquiry,name="enquiry"),
    path("einsert/",views.einsert,name="einsert"),

    #---------------crud---------------
    path("display/",views.display,name="display"),
    path('editpage/<int:id>/',views.EditPage,name='editpage'),
    path("update/<int:id>/",views.update,name="update"),
    path("delete/<int:id>/",views.delete,name="delete"),
]