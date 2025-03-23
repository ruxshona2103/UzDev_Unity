from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main_app.views import (CategoryViewSet, ProjectViewSet,
                            NavItemViewSet, PageViewSet,
                            ConctactSubmissionViewSet,contact_submission)

router = DefaultRouter()
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'projects',ProjectViewSet)
router.register(r'navigation', NavItemViewSet)
router.register(r'pages', PageViewSet)
router.register(r'admin/contact-submissions', ConctactSubmissionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('contact/',contact_submission, name='contact-submission'),
]
