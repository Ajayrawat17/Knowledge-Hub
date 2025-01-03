from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin',admin.site.urls),
    path("about/", views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('', views.login_view, name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("faculty/", views.faculty, name='faculty'),
    path("pyq/", views.pyq, name='pyq'),
    path("course_outline/", views.course_outline, name='course_outline'),
    path("practice/index/", views.index, name='index'),
    path("course_outline/index/", views.index, name='index'),
    path("faculty/index/", views.index, name='index'),
    path("book/", views.book, name='book'),
    path("courses/", views.courses, name='courses'),
    path("assignments/", views.assignment, name='assignment'),
    path("btech/", views.btech, name='btech'),
    path("bba/", views.bba, name='bba'),
    path("bca/", views.bca, name='bca'),
    path("mca/", views.mca, name='mca'),
    path("bsc/", views.bsc, name='bsc'),
    path("mcom/", views.mcom, name='mcom'),
    path("mba/", views.mba, name='mba'),
    path("bcom/", views.bcom, name='bcom'),
    path("btech_assignment/", views.btech_assignment, name='btech_assignment'),
    path("bba_assignment/", views.bba_assignment, name='bba_assignment'),
    path("bca_assignment/", views.bca_assignment, name='bca_assignment'),
    path("bcom_assignment/", views.bcom_assignment, name='bcom_assignment'),
    path("mcom_assignment/", views.mcom_assignment, name='mcom_assignment'),

    path("sem1mathpyqs/", views.sem1mathpyqs, name='sem1mathpyqs'),
    path("sem1physicspyqs/", views.sem1physicspyqs, name='sem1physicspyqs'),
    path("sem1ecepyqs/", views.sem1ecepyqs, name='sem1ecepyqs'),
    path("sem2mathpyqs/", views.sem2mathpyqs, name='sem2mathpyqs'),  

    path("subjects-btech/", views.subjects_btech, name='subjects_btech'),
    path("subjects-bca/", views.subjects_bca, name='subjects_bca'),
    path("subjects-bcom/", views.subjects_bcom, name='subjects_bcom'),
    path("subjects-bba/", views.subjects_bba, name='subjects_bba'),
    path("subjects-mba/", views.subjects_mba, name='subjects_mba'),

    path("notes/", views.notes, name='notes'),

    path('resources/<str:course>/<str:subject>/', views.resources_page, name='resources_page'),
]
