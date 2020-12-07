from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Exam(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    question = models.CharField(max_length=3000)
    option1 = models.CharField(max_length=3000,blank=True)
    optionimg1 = models.ImageField(upload_to='photo/',blank=True,null=True)
    option2 = models.CharField(max_length=3000,blank=True)
    optionimg2 = models.ImageField(upload_to='photo/',blank=True,null=True)
    option3 = models.CharField(max_length=3000,blank=True)
    optionimg3 = models.ImageField(upload_to='photo/',blank=True,null=True)
    option4 = models.CharField(max_length=3000,blank=True)
    optionimg4 = models.ImageField(upload_to='photo/',blank=True,null=True)
    correct = models.CharField(max_length=3000,blank=True)
    correctimg = models.ImageField(upload_to='photo/',blank=True,null=True)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('exam:exam_list')



class questionkey(models.Model):
    question = models.ForeignKey(Exam,on_delete=models.CASCADE,null=True,blank=True)

class ExamAns(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    question = models.ForeignKey(Exam,on_delete=models.CASCADE,null=True,blank=True)
    store = models.CharField(max_length=3000, blank=True, null=True)