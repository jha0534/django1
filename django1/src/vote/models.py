from django.db import models

#질문
#질문제목 생성일
class Question(models.Model):
    name = models.CharField(max_length = 100)
    #DateField : 날짜(년월일)를 저장하는 공간
    #DateTimeField : 날짜 + 시간을 저장하는 공간
    date = models.DateTimeField('생성일') # 1
    def __str__(self):
        return self.name
    class Meta : #모델클래스에 정의된 변수, 데이블 이름 등을 처리할 때 사용하는 클래스
        #ordering : 해상 모델 클래스에 정의된 변수 중에서 정렬에 사용할 변수 이름을 저장하는 변수
        ordering = ['-date']
        
#답변
#어떤 질문에 연결되어있는지에 답변내용 투표수
class Choice(models.Model):
    #ForeignKey(연결할 다른 모델 클래스) : 
    #ForeignKey 객체를 만든 모델클래스의 객체들이 연결한 모델 클래스의 객체와 1:n 관계로 연결할 수 있는 설정
    #ForeignKey 의 객체를 저장한 변수는 연결한 모델 클래스의 객체를 저장하는 변수가 됨
    #Choice 객체 q.name -> 해당하는 choice 객체와 연결된 Question 객체의 name 변수 값을  추출
    #on_delete : 연결된 모델클래스의 객체가 삭제될때 어떻게 처리할지 지정하는 변수
    #on_delete = model.PROTECT : 연결된 모델클래스의 객체가 삭제되지 않도록 막아주는기능
    #models.CASCADE : 연결된 모델클래스의 객체가 삭제되면 같이 삭제됨
    #models.SET_NULL : 연결된 모델 클래스의 객체가 삭제되면 아무것도 연결되지 않은 상태로 유지
    #models.SET(연결할 객체) : 연결된 객체가 삭제되면 매개변수로 넣은 객체와 연결
    #models.SET_DEFAULT : 연결된 객체가 삭제도면 기본 설정된 객체와 연결
    q = models.ForeignKey(Question, on_delete= models.CASCADE) # n
    name = models.CharField('답변항목',max_length = 50)
    #IntegerField : 정수값을 저장하는 공간
    #default : 모델 클래스의 객체 생성시 저장 공간에 기본값 설정
    #default는 모든 field에서 사용할 수 있음
    vote = models.IntegerField('투표수',default = 0)
    def __str__(self):
        return self.q.name + " / " + self.name
    