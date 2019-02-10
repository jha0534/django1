"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#bookmark/views.py 의 index, booklist함수 임포트
from bookmark.views import index, booklist, getbook
#from bookmark.views import * : 해당파일에 들어있는 모든 변수,함수,클래스 임포트

#url.py : 웹클라이언트의 요청을 분석해 특정한 뷰를 호출하는 역할
#urlpatterns : URL과 뷰함수를 등록 및 관리하는 변수
#리스트 형태로 저장. URL 등록 시 path함수를 통해 urlpatterns의 요소로 추가
#path(URL주소(문자열), 호출할 뷰함수/클래스 이름)

#기본 주소 : 127.0.0.1:8000
urlpatterns = [
    #웹 클라이언트가 127.0.0.1:8000/admin 으로 요청한 경우
    #관리자 사이트 뷰가 실행되도록 등록
    path('a1/', admin.site.urls),
    #웹 클라이언트가 127.0.0.1:8000/ 으로 요청한 경우 index 뷰함수 호출
    path('', index),
    path('booklist/', booklist),
    #127.0.0.1:8000/숫자값/ 으로 요청한 경우
    #getbook 뷰함수 호출. bookid 매개변수에 숫자값을 대입
    #URL에서 매개변수로 사용할 값을 분리하는 방법 : <값의타입:매개변수이름>
    path('<int:bookid>/', getbook),
    #투표어플릭케이션에 사용할 하위 URLConf 등록
    #웹 클라이언트가 127.0.0.1:8000/vote/로 시작하는 모든 요청을
    #vote 폴더에 있는 URL.py에 등록된 urlpatterns로 처리하도록 등록
    path('vote/', include('vote.urls')),
    #127.0.0.1:8000/cl/로 시작하는 모든 요청을 customlogin/urls.py에 넘겨줌
    path('cl/', include('customlogin.urls')),
    #127.0.0.1:8000/blog로 시작하는 모든 요청을 blog/urls.py로 처리
    path('blog/', include('blog.urls')),
    #social_django 어플리케이션의 하위 URLConf 등록
    path('auth/', include('social_django.urls', namespace = 'social')),
    ]
#setting.py에서 설정된 변수를 가져오기 위해 임포트
from django.conf import settings
#MEDIA_URL와 MEDIA_ROOT를 연결하기 위한 함ㅅ
from django.conf.urls.static import static

#파일 요청 URL과 실체 저장된 파일 경로를 매칭
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)













