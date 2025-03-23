from rest_framework import serializers
from main_app.models import  NavItem, ContactSubmission, Page

class NavItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavItem
        fields = "__all__"


class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = ['id', 'name', 'email', 'subject', 'message']



class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'

