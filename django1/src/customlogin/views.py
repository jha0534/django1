from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import SigninForm, SignupForm
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse

# 회원가입 처리 뷰
def signup(request):
    #GET, POST 구분
    if request.method =="GET":
        #SignupForm 객체 생성 후 HTML 파일 전달
        f = SignupForm()
        return render(request, 'cl/signup.html', {'f': f})
    #POST
    elif request.method =="POST":
        #사용자 입력 데이터 기반의 SignupForm 객체 생성
        f = SignupForm(request.POST)
        #유효한 값이 들어있는지 확인 (아이디 중복, 비밀번호 형식이 올바른지, 이메일 형식이 올바른지)
        if f.is_valid():
            #비밀번호 확인과 비밀번호에 들어있는 값이 같은지 확인
            if f.cleaned_data['password'] == f.cleaned_data['password_check']:
                #회원생성
                #create_user(아읻, 이메일, 패스워드) : 데이터 베이스에 django가 제공하는 회원 모델클래스의 객체를 생성하는 함수,
                #아이디, 이메일은 원본, 패스워드는 암호화된 상태로 저장됨
                #생성된 새로운 회원을 반환함
                new_user = User.objects.create_user(username = f.cleaned_data['username'],
                                                    email = f.cleaned_data['email'], 
                                                    password = f.cleaned_data['password'])
                
                #회원정보 추가(성 - last_name, 이름 - first_name)
                new_user.last_name = f.cleaned_data['last_name']
                new_user.first_name = f.cleaned_data['first_name']
                new_user.save() #수정사항 (성, 이름 변수에 값 변경)을 데이터 베이스에 반영
                print('새 유저', new_user)
                #다른 URL 전송
                return HttpResponseRedirect(reverse('vote:index'))
            #비밀번호 다른경우
            else:
                #HTML에러코드 전달
                return render(request, 'cl/signup.html', {'f':f, 
                                                          'error': '비밀번호가 같지 않습니다.'})
        #유효한 값이 아닌경우
        else:
            #HTML파일에 에러코드 전달
            #에러코드가 is_valid() 함수를 통과하지 못하면 User 모델 클래스에 설정된 에러정보가 자동으로 넘겨짐
            return render(request, 'cl/signup.html', {'f':f })
        
from django.contrib.auth import login, authenticate, logout
#logout(request)

#authenticate(아이디, 비밀번호)
#비밀번호를 암호화 한 뒤, 아이디와 암호화된 비밀번호 모두 일치하는 User 객체를 추출
#단, 아이디나 비밀번호가 틀린경우 None 값을 반환

#login(request, User 객체)
#해당 요청을 한 클라이언드가  User객체의 정보를 바탕으로 로그인 처리
#로그인이 완료된 후, request.user 변수로 해당요청을 한 클라이언트의 User 객체 추출가능
#비로그인 상태일때는 사용할 수 없음

#로그인 처리 과정
#1) authenticate 함수로 로그인할 User 객체 찾기 
#2) 받은 결과가 None 값이 아닌경우, login 함수를 통해 클라이언트를 로그인함

# 로그인 처리 뷰
def signin(request):
    #GET, POST 구분
    if request.method == "GET":
        #SigningForm 객체 생성 후 HTML 파일 전송
        return render(request, 'cl/signin.html', {'f':SigninForm()})
        
    #POST
    elif request.method == "POST":
        #SigningForm 객체를 사용자 입력기반으로 생성
        f = SigninForm(request.POST)
        
        #사용자가 입력한 데이터를 추출(아이디, 패스워드)
        id = request.POST.get('username')
        pw = request.POST.get('password')
        
        #아이디랑 패스워드가 일치하는 User 모델클래스 객체 추출
        #u : 회원이 있는경우 User객체, 없는경위 None값이 저장됨
        u = authenticate(username = id, password = pw)
        
        #회원이 있는 경우
        if u:
            #로그인처리
            login(request, u)
            #nexturl : 이동할  URL 주소가 있는 경우 메인페이지로 가지 않고 저장된 URL로 리다이렉트
            nexturl = request.POST.get('nexturl')
            if nexturl :
                return HttpResponseRedirect(nexturl)
            else:
                return HttpResponseRedirect(reverse('vote:index'))
        #회원이 없는 경우    
        else:
            return render(request, 'cl/signin.html', {'f': f, 'error':'아이디나 비밀번호가 틀렸습니다.'})


# 로그아웃 처리 뷰
def signout(request):
    #요청한 클라이언트가 로그아웃
    logout(request)
    #다른 URL 전송
    return HttpResponseRedirect(reverse('cl:signin'))