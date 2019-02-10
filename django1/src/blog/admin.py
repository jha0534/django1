from django.contrib import admin
from .models import Post, PostFile, PostImage, PostType

admin.site.register(Post)
admin.site.register(PostFile)
admin.site.register(PostImage)
admin.site.register(PostType)

#관리자 사이트에서 객체 새엉
#카테고리 2가지
#글 카테고리별 2개
#