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
    path("sem2chemistrypyqs/", views.sem2chemistrypyqs, name='sem2chemistrypyqs'),
    path("sem2evspyqs/", views.sem2evspyqs, name='sem2evspyqs'),
    path("sem3OOPSpyqs/", views.sem3OOPSpyqs, name='sem3OOPSpyqs'),
    path("sem3dspyqs/", views.sem3dspyqs, name='sem3dspyqs'),
    path("sem3digitallogicpyqs/", views.sem3digitallogicpyqs, name='sem3digitallogicpyqs'),
    path("sem4javapyqs/", views.sem4javapyqs, name='sem4javapyqs'),
    path("sem4micropyqs/", views.sem4micropyqs, name='sem4micropyqs'),
    path("sem4Automatapyqs/", views.sem4Automatapyqs, name='sem4Automatapyqs'),
    path("sem5mlpyqs/", views.sem5mlpyqs, name='sem5mlpyqs'),
    path("sem5databasepyqs/", views.sem5databasepyqs, name='sem5databasepyqs'),
    path("sem5ospyqs/", views.sem5ospyqs, name='sem5ospyqs'),
    path("sem6compilerpyqs/", views.sem6compilerpyqs, name='sem6compilerpyqs'),
    path("sem6sepyqs/", views.sem6sepyqs, name='sem6sepyqs'),
    path("sem6networksecuritypyqs/", views.sem6networksecuritypyqs, name='sem6networksecuritypyqs'),
    path("sem7Softpyqs/", views.sem7Softpyqs, name='sem7Softpyqs'),
    path("sem7bipyqs/", views.sem7bipyqs, name='sem7bipyqs'),
    path("sem7cgpyqs/", views.sem7cgpyqs, name='sem7cgpyqs'),
    path("sem8ccpyqs/", views.sem8ccpyqs, name='sem8ccpyqs'),
    path("sem8mbpyqs/", views.sem8mbpyqs, name='sem8mbpyqs'),
    path("sem8dmpyqs/", views.sem8dmpyqs, name='sem8dmpyqs'),
    path("sem1physicspyqs/", views.sem1physicspyqs, name='sem1physicspyqs'),
    path("sem1chemistrypyqs/", views.sem1chemistrypyqs, name='sem1chemistrypyqs'),
    path("sem1mathpyqs/", views.sem1mathpyqs, name='sem1mathpyqs'),
    path("sem1englishpyqs/", views.sem1englishpyqs, name='sem1englishpyqs'),
    path("sem2physicspyqs/", views.sem2physicspyqs, name='sem2physicspyqs'),
    path("sem2chemistrypyqs/", views.sem2chemistrypyqs, name='sem2chemistrypyqs'),
    path("sem2mathpyqs/", views.sem2mathpyqs, name='sem2mathpyqs'),
    path("sem2csbasicspyqs/", views.sem2csbasicspyqs, name='sem2csbasicspyqs'),
    path("sem3mechanicspyqs/", views.sem3mechanicspyqs, name='sem3mechanicspyqs'),
    path("sem3organicchempyqs/", views.sem3organicchempyqs, name='sem3organicchempyqs'),
    path("sem3discretemathpyqs/", views.sem3discretemathpyqs, name='sem3-discretemathpyqs'),
    path("sem3introtocomputingpyqs/", views.sem3introtocomputingpyqs, name='semintrotocomputingpyqs'),
    path("sem4electromagnetismpyqs/", views.sem4electromagnetismpyqs, name='sem4electromagnetismpyqs'),
    path("sem4physicalchempyqs/", views.sem4physicalchempyqs, name='sem4physicalchempyqs'),
    path("sem4linearalgebra-pyqs/", views.sem4linearalgebrapyqs, name='sem4linearalgebrapyqs'),
    path("sem4datastructurespyqs/", views.sem4datastructurespyqs, name='sem4datastructurespyqs'),
    path("sem5quantummechanicspyqs/", views.sem5quantummechanicspyqs, name='sem5quantummechanicspyqs'),
    path("sem5inorganicchempyqs/", views.sem5inorganicchempyqs, name='sem5inorganicchempyqs'),
    path("sem5dbmspyqs/", views.sem5dbmspyqs, name='sem5dbmspyqs'),
    path("sem5ospyqs/", views.sem5ospyqs, name='sem5-os-pyqs'),
    path("sem6relativitypyqs/", views.sem6relativitypyqs, name='sem6relativitypyqs'),
    path("sem6thermodynamicspyqs/", views.sem6thermodynamicspyqs, name='sem6-thermodynamics-pyqs'),
    path("sem6compilerdesignpyqs/", views.sem6compilerdesignpyqs, name='sem6compilerdesignpyqs'),
    path("sem6softwareengineeringpyqs/", views.sem6softwareengineeringpyqs, name='sem6softwareengineering-pyqs'),
    path("sem7particlephysicspyqs/", views.sem7particlephysicspyqs, name='sem7particlephysicspyqs'),
    path("sem7biochemistrypyqs/", views.sem7biochemistrypyqs, name='sem7biochemistrypyqs'),
    path("sem7advanceddspyqs/", views.sem7advanceddspyqs, name='sem7-advanceddspyqs'),
    path("sem7aipyqs/", views.sem7aipyqs, name='sem7aipyqs'),
    path("sem8astrophysicspyqs/", views.sem8astrophysicspyqs, name='sem8astrophysicspyqs'),
    path("sem8appliedchemistrypyqs/", views.sem8appliedchemistrypyqs, name='sem8appliedchemistrypyqs'),
    path("sem8mlpyqs/", views.sem8mlpyqs, name='sem8mlpyqs'),
    path("sem8cloudcomputingpyqs/", views.sem8cloudcomputingpyqs, name='sem8cloudcomputingpyqs'),

    
    









    path("subjects-btech/", views.subjects_btech, name='subjects_btech'),
    path("subjects-bca/", views.subjects_bca, name='subjects_bca'),
    path("subjects-bcom/", views.subjects_bcom, name='subjects_bcom'),
    path("subjects-bba/", views.subjects_bba, name='subjects_bba'),
    path("subjects-mba/", views.subjects_mba, name='subjects_mba'),

    path("notes/", views.notes, name='notes'),

    path('resources/<str:course>/<str:subject>/', views.resources_page, name='resources_page'),
]
