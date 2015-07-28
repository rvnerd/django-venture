from django.conf.urls import url

from . import views

urlpatterns = [
    # course_list view simple-url:
    # url(r'^$', views.course_list, name='course_list'),
    # course_list view generic-url:
    url(r'^$', views.CourseListView.as_view(), name='index'),

    # this must be first because of the cascade order of the url
    # patter assignment
    #
    # step_detail view simple-url:
    url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$', views.step_detail,
        name='step_detail'),

    # course_detail view simple-url:
    url(r'(?P<course_pk>\d+)/$', views.course_detail, name='course_detail'),

]
