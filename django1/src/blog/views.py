from django.shortcuts import render

# 제네릭 뷰 : 장고에서 제공하는 여러가지 뷰 기능을 구현한 클래스
# ListView : 특정 모델클래스의 객체 목록을 다루는 기능이 구현된 뷰
# DetailView : 특정 모델 클래스의 객체 1개를 다루는 기능이 구현된 뷰
# FormView : 특정 폼 클래스를 다루는 기능이 구현된 뷰

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from blog.forms import PostForm
from blog.models import Post, PostFile, PostImage
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse

#index : 글 목록이 뜨는 메인 페이지
class Index(ListView):
    #해당 뷰가 사용할 html 파일의 경로
    template_name = 'blog/index.html'
    #리스트로 뽑을 모델 클래스
    model = Post
    #템플릿에게 객체리스트로 넘겨줄 때 사용할 키 값
    context_object_name = 'list'
    #한페이지에 최대 몇개의 객체가 보여질지 설정
    paginate_by = 5
    
#detail : 글 상세보기 페이지
class Detail(DetailView):
    template_name = 'blog/detail.html'
    model = Post
    context_object_name = 'obj'
    
from django.contrib.auth.mixins import LoginRequiredMixin
#posting : 글 쓰기 페이지
class Posting(LoginRequiredMixin, FormView):
    template_name = 'blog/posting.html'
    #연동할 폼 클래스 저장
    form_class = PostForm
    context_object_name = 'f'
    
    #is_valid() 함수가 True를 반환한v뒤 처리를 form_valid() 함수를 오버라이딩 해서 작성
    def form_valid(self, form):
        
        #매개변수 form : is_valid()함수를 통과한 PostForm 객체
        #PostForm객체를 바탕으로 Post객체 저장
        #글쓴이 (author) 변수가 비어있으므로, 데이터베이스에 저장하지 않음

        p = form.save(commit = False) #p : Post 객체
        #request.user : 요청한 클라이언트의 로그인 정보(User 모델 클래스 객체)
        p.author = self.request.user 
        p.save() #Post 객체가 데이터 베이스에 저장됨
        
        #클라이언트가 보낸첨부파일, 이미지 파일을 바탕으로 PostFile, PostImage 객체 생성 및 저장
        
        #request.FILES : 클라이언트가 서버로 보낸 파일정보를 관리하는 변수
        
        #PostFile 객체를 생성
        
        for f in self.request.FILES.getlist('files'):
            #f 파일정보
            pf = PostFile() #새로운 PostFile 모델 클래스의 객체 생성
            pf.file = f
            pf.post = p
            pf.save() #데이터 베이스에 새로운 PostFile 객체가 저장됨
            
        
        #PostImage객체를 생성
        for i in self.request.FILES.getlist('images'):
            #i : 이미지 정보
            pi = PostImage()
            pi.post = p
            pi.image = i
            pi.save()
        
        #완성된 글 페이지로 URL 이동
        return HttpResponseRedirect(reverse('blog:detail', args = (p.id,)))
    
    
    

