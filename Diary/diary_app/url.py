from django.urls import path
from . import views

urlpatterns = [
    path('viewDiary',views.viewDiary,name='viewDiary'),
    path('deleteDiary/<int:id>',views.deleteDiary,name='deleteDiary'),
    path('addDiary',views.createDiary,name='createDiary'),
    path('updateDiary/<int:id>',views.updateDiary,name='updateDiary'),
    path('viewDiary/<int:id>',views.viewDiary,name='viewDiaryDetail'),
    path('',views.home_page,name='home'),
]