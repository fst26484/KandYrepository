from django.db import models
from django.contrib.auth.models import User

class White(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='white_owner',verbose_name='投稿者')
    update = models.CharField(max_length=100,verbose_name='投稿日')
    content = models.CharField(max_length=100,verbose_name='タイトル')
    image = models.TextField(verbose_name='内容')

    def __str__(self):
        return '<update:id=' + str(self.id) + ',' + \
            self.content + ',' + str(self.update) + '>'

class Question(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question_owner')
    text = models.TextField(verbose_name='内容')

    def __str__(self):
        return '<question:id=' + str(self.id) + ',' + self.text + '>' 


