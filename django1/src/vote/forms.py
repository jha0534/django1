'''
Created on 2019. 1. 26.

@author: user
'''
# form : HTML <form> 태그에 들어가는  <input> 태그들을 관리하는 클래스/기
#        모델클래스에 저장된 변수들에 맞춰 자동설정도 할 수 있고, 커스텀 입력공간(비밀번호 확인)도 생성할 수 있음

# class 클래스명 (ModelForm 또는 Form):
# ModelForm : 모델클래스 기반으로 입력양식을 자동 생성할 때 상속받는 클래스
# Form : 커스텀 입력양식을 생성할 때 생성할 때 상속받는 클래스
# ModelForm을 상속받았을 때도 커스텀 입력양식을 생성할 수 있음

# 폼 크래스의 객체를 함수를 통해 HTML문서의 코드로 변환할 수 있음 (<p>, <table>, <li>)
# ex) 폼클래스객체.as_p() -> 해당 폼 객체에 저장된 입력 공간들을 <input>태그로 변환하고,
# 개별적으로 <p> 태그로 묶은 문자열을 반환
# ex2) 회원가입 폼 클래스 객체.as_p() 0>
# <p> <label>아이디</label> <input type = "" name = ""> </p>
# <p> <label>비밀번호</label> <input type ="" name = ""> </p> """ 문자열 반환

# 1) ModelForm/Form 클래스 임포트
# 2) 사용할 모델클래스 임포트
# 3) ModelForm/Form 클래스를 상속받은 폼 클래스 정의

# 만들어진 폼 클래스는 view에서 객체 생성을 통해 활용함
# 변경
# 어플리케이션 생성 -> setting.py 등록 -> 모델 정의 -> 데이터베이스 반영 -> 폼 클래스 정의
# -> 뷰정의 -> 템플릿 정의 -> URLConf 등록

from django.forms.models import ModelForm
from .models import Question, Choice

# Question 모델 클래스와 연동된 모델 폼 클래스 정의 (Question 객체 추가/ 수정 때 사용)

class QuestionForm(ModelForm):
    class Meta:  #Meta 클래스 : 연동하고자 하는 모델 클래스에 대한 정보를 정의하는 클래스
        # model : 연동하고자 하는 모델 클래스를 저장하는 변수
        model = Question
        # fields : 모델클래스에 정의된 변수중 어떤 변수를 클라이언트가 작성할수 있도록 입력양식으로 제공할 것인지 지정하는변수
        # (iterable - list, tuple)
        # field, exclude 변수 중 한개만 사용해야함
        fields = ['name'] # name변수만 입력할수 있는 form 생성
        # exclude : 모델클래스에 정의된 변수 중 입력양식으로 만들지 않을 것을 지정하는 변수 (list)
        #exclude = ['date'] #date 변수를 제외한 모든 변수를 입력할수 있는 form 생성

# Choice 모델클래스와 연동딘 모델 폼클래스 정의 (Choice 객체 추가 / 수정 때 사용)
class ChoiceForm(ModelForm):
    #Choice 모델 클래스 연동 및 q변수와 name변수를 클라이언트가 입력할 수 있도록 설정
    
    class Meta:
        model = Choice
        fields = ['q', 'name']
