from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    # https://docs.djangoproject.com/en/1.8/ref/models/fields/#field-types
    author = models.ForeignKey('auth.User')     # 다른 모델에 대한 링크
    title = models.CharField(max_length=200)    # 글자 수가 제한된 텍스트를 정의할 때 사용
    text = models.TextField()                   # 글자 수에 제한이 없는 긴 텍스트를 위한 속성
    created_date = models.DateTimeField(        # 날짜와 시간 속성
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title