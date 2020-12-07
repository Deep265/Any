from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'exam'

urlpatterns = [
    path('list/',views.ExamListView.as_view(),name='exam_list'),
    path('detail/<int:pk>/',views.ExamDetailView.as_view(),name='exam_detail'),
    path('new/',views.ExamCreateView,name='add_question'),
    path('',views.ExamPage.as_view(),name='exam_page'),
    path('detail/',views.ExamTarget.as_view(),name='exam_target'),
    path('index/',views.IndexView,name='index'),
]

