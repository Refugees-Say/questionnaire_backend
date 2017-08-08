from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from refugee_say.users.views import UserViewSet
from refugee_say.radio_question.views import RadioQuestionViewSet
from refugee_say.ranking_question.views import RankingQuestionViewSet
from refugee_say.selection_question.views import SelectionQuestionViewSet

from refugee_say.choice.views import ChoiceViewSet, TypeViewSet
from refugee_say.questionnaire.views import QuestionnaireViewSet, QuestionOrderViewSet

from refugee_say.response.views import ResponseViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'radios', RadioQuestionViewSet)
router.register(r'rankings', RankingQuestionViewSet)
router.register(r'selections', SelectionQuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'choice_types', TypeViewSet)
router.register(r'questionnaires', QuestionnaireViewSet)
router.register(r'question_orders', QuestionOrderViewSet)
router.register(r'responses', ResponseViewSet)

urlpatterns = [
                  url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
                  url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

                  # Django Admin, use {% url 'admin:index' %}
                  url(settings.ADMIN_URL, admin.site.urls),

                  # User management
                  # url(r'^users/', include('refugee_say.users.urls', namespace='users')),
                  # url(r'^accounts/', include('allauth.urls')),

                  # Your stuff: custom urls includes go here
                  url(r'^api/v1/token/$', obtain_auth_token),

                  url(r'^api/v1/', include('authentication.urls')),
                  url(r'^api/v1/', include(router.urls)),
                  url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
                          url(r'^__debug__/', include(debug_toolbar.urls)),
                      ] + urlpatterns
