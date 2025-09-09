from django.urls import path
from .import views

urlpatterns =[
    path('add',views.add,name='add'),
    path('insert/',views.insert,name='insert'),
    path('show/',views.show,name='show'),
    path('edit/<int:rollnumber>/',views.edit,name='edit'),
    path('update/<int:rollnumber>/',views.update,name='update'),
    path('delete/<int:rollnumber>/',views.delete,name='delete')
]