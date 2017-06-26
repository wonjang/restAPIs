from django.conf.urls import url
from mathreq import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^mathreq/$', views.MathReqList.as_view()),
    url(r'^mathreq/factorial/$', views.MathReqFactorial.as_view()),
    url(r'^mathreq/combination/$', views.MathReqCombination.as_view()),
    url(r'^mathreq/(?P<pk>[0-9]+)/$', views.MathReqDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)