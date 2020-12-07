from django.shortcuts import render,get_object_or_404
from django.urls import reverse
# Http Imports
from django.http import HttpResponse,HttpResponseRedirect
# Form imports

# Model Imports
from .models import Exam,ExamAns,questionkey
# Class based Views imports
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from django.views.generic.edit import FormMixin
# Create your views here.

def IndexView(request):
    return render(request,'index.html')

class ExamListView(ListView):
    model = Exam
    context_object_name = 'exam'



def ExamCreateView(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        correct = request.POST.get('correct')
        img1 = request.FILES['img1']
        img2 = request.FILES['img2']
        img3 = request.FILES['img3']
        img4 = request.FILES['img4']
        img5 = request.FILES['img5']
        exam_img = Exam(user=request.user,question=question,option1=option1,option2=option2,option3=option3,option4=option4,correct=correct,optionimg1=img1,optionimg2=img2,optionimg3=img3,optionimg4=img4,correctimg=img5)
        exam_img.save()
        return HttpResponseRedirect(reverse('exam:exam_list'))
    return render(request,'exam/exam_form.html')



class ExamDetailView(DetailView):
    model = Exam
    context_object_name = 'exam'

    def post(self, request, pk,*args, **kwargs):
        store = request.POST['answer']
        ques = request.POST.get('question')

        exam = get_object_or_404(Exam,pk=pk)
        try:
            examans = ExamAns.objects.filter(user=request.user,question__exact=exam,store__isnull=False).values_list('id',flat=True)[0]
#       print(examans)
            examans_change = get_object_or_404(ExamAns,pk=examans)
#        print(examans_change)
            examans_change.store = store
            examans_change.save()
            if examans == 0:
                examans = ExamAns(user=request.user, question=exam, store=store)
                examans.save()
        except:
            examans = ExamAns(user=request.user,question=exam,store=store)
            examans.save()



        context = self.get_context_data()
        return self.render_to_response(context)


class ExamPage(TemplateView):
    template_name = 'exam/exam_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exam'] = Exam.objects.all()
        return context

class ExamTarget(TemplateView):
    template_name = 'exam/exam_target.html'


