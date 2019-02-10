from django.db import models
#글쓴이를 외래키로 지정하기 위해 임포트
from django.contrib.auth.models import User

#카테고리
#카테고리 이름
class PostType(models.Model):
    name = models.CharField('카테고리', max_length = 20)
    def __str__(self):
        return self.name

#글 정보
#제목, 글쓴이-외래키, 글내용, 작성일, 카테고리-외래키
class Post(models.Model):
    category = models.ForeignKey(PostType, on_delete = models.CASCADE)
    headline = models.CharField('제목', max_length = 200)
    author = models.ForeignKey(User, on_delete = models.PROTECT)
    
    #TextField : 글자수 제한이 없는 문자열 저장공간
    
    #default외에 XXXXField에서 사용할 수 있는 공통 매개변수
    #null(기본값 False) : True값을 저장한 경우, 데이터베이스에 객체 저장시 해당 변수값이 비어있어도 생성되도록 허용
    #blank(기본값 False) : True값을 저장한 경우, 폼객체를 통한 사용자 입력공간 (<input>) 제공 시 빈칸을 허용
    
    content = models.TextField('내용', null = True, blank = True)
    
    #auto_now_add(DateTimeField, DateField 만 사용가능)
    #객체 생성시, 서버기준의 날짜 / 시간이 자동으로 저장되도록 설정하는 매개변수
    pub_date = models.DateTimeField('작성일', auto_now_add = True)
    
    def __str__(self):
        return self.headline
    
    class Meta:
        #pub_date 변수에 저장된 값을 내림차순으로 정렬
        #-> 최신글 순으로 정렬
        ordering = ['-pub_date']
        

#글에 포함된 이미지 정보
#글-외래키, 이미지파일
#ImageField : 이미지 파일을 저장하는 공간
#ImageField를 사용하려면 Pillow 모듈이 설치되있어야 함
#Pillow 모듈 : 파이썬에서 이미지 처리할때 사용하는 대표적인 모듈
#pip install Pillow
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    #upload_to : 실제 파일이 저장되어 있는 경로를 지정하는 매개변수
    
    #서버기분의 날자 데이터를 포함시킬 수 있음
    #%Y : 객체가 저장될 때 서버기준의 년도
    #%m : 서버기준의 달
    #%d : 서버기준의 일
    
    #이미지 저장 시, images/년/월/일 폴더에 이미지파일이 저장
    image = models.ImageField('이미지파일', upload_to = 'images/%Y/%m/%d')

#글에 포함된 첨부파일 정보
#글-외래키, 파일
class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    
    #FileField : 파일 데이터를 저장하는 공간
    file = models.FileField('첨부파일', upload_to = 'files/%Y/%m/%d')
    
    