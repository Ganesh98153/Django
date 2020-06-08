from django.contrib import admin
from django.urls import path,include



#This is for decoration of admin site in django project name SchoolManagementSystem


admin.site.site_header = "School Management System Admin"

admin.site.site_title = "School Management System Admin Portal"

admin.site.index_title = "Welcome to School Management System"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
