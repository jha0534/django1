'''
Created on 2019. 2. 9.

@author: user
'''
from .views import *
from django.urls import path
app_name = 'blog'

urlpatterns = [
    #뷰 클래스 등록 시 뷰 클래스.as_view()로 등록
    path('', Index.as_view(), name = 'index'),
    
    #DetailView 클래스는 객체를 추출하기 위해 'pk' 매개변수를 사용
    #127.0.0.1:8000/blog/글번호/
    path('<int:pk>/', Detail.as_view(), name = 'detail'),
   
    path('posting/', Posting.as_view(), name = 'posting'),
    
    
    ]
