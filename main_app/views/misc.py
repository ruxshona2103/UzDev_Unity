from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action

from main_app.models import NavItem, Page, ContactSubmission
from main_app.serializers import NavItemSerializer, PageSerializer, ContactSubmissionSerializer
from main_app.permissions import IsAdminUserOrReadOnly


class NavItemViewSet(viewsets.ModelViewSet):
    queryset = NavItem.objects.all()
    serializer_class = NavItemSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminUserOrReadOnly]

    @action(detail=True, methods=['get'])
    def published(self, request):
        published_pages = Page.objects.filter(is_published=True)
        serializer = PageSerializer(published_pages, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def contact_submission(request):
    serializer = ContactSubmissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message" : "Your message has been sent successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ConctactSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ContactSubmission.objects.all().order_by("-created_at")
    serializer_class = ContactSubmissionSerializer

    @action(detail=True, methods=['post'])
    def mark_as_read(self, request, pk=None):
        submission = self.get_object()
        submission.is_read = True
        submission.save()
        return Response({'status': 'marked as read'})