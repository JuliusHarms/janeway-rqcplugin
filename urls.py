"""
© Julius Harms, Freie Universität Berlin 2025
"""

from plugins.rqc_adapter import views
from django.urls import re_path
#TODO unused? look over
urlpatterns = [
    re_path(r'^manager/$', views.manager, name='rqc_adapter_manager'),
    re_path(r'^manager/handle_journal_settings_update$', views.handle_journal_settings_update, name='rqc_adapter_handle_journal_settings_update'),
    re_path(r'^article/(?P<article_id>\d+)/$', views.rqc_grade_article_reviews, name='rqc_adapter_rqc_grade_article_reviews'),
    re_path(r'^articles/(?P<article_id>\d+)/submit$', views.submit_article_for_grading, name='rqc_adapter_submit_article_for_grading'),
    re_path(r'^participate_in_rqc/$', views.reviewer_opting_form, name="rqc_adapter_reviewer_opting_form"),
    re_path(r'^set_reviewer_opting_status/$', views.set_reviewer_opting_status, name='rqc_adapter_set_reviewer_opting_status'),
]
