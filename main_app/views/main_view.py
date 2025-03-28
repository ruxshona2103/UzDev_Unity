from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, action
from django_filters.rest_framework import DjangoFilterBackend
from main_app.models import Category, Project,ProjectImage
from main_app.serializers import (
    CategorySerializer,
    ProjectSerializer,
    ProjectDetailSerializer,
    ProjectImageSerializer,
)
from main_app.permissions import IsAdminUserOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]

    @action(detail=True, methods=['get'])
    def projects(self, request, pk=None):
        category = self.get_object()
        projects = Project.objects.filter(category=category)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by("-created_at")

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'featured']
    search_fields = ['title', 'description', 'client']

    permission_classes = [IsAdminUserOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectSerializer

    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured_projects = Project.objects.filter(featured=True)
        serializer = ProjectSerializer(featured_projects, many=True)
        return Response(serializer.data)


class ProjectImageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing project images.
    """
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()



