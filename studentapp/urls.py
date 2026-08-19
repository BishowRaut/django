from django .urls import path
from.import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:student_id>/', views.update_student, name='update_student'),
    
    # ADD THIS LINE: Matches the name used in your template's {% url %} tag
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]