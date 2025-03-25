from rest_framework import serializers
from main_app.models import Category, Project, ProjectImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProjectImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)

    class Meta:
        model = ProjectImage
        fields = ['id', 'project', 'image', 'is_main', 'created_at']


class ProjectSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    images = ProjectImageSerializer(many=True, read_only=True)
    main_image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'client', 'date', 'featured',
                  'category', 'category_name', 'images', 'main_image', 'created_at']

    def get_main_image(self, obj):
        main_image = obj.images.filter(is_main=True).first()
        if not main_image:
            main_image = obj.images.first()

        if main_image:
            return {
                'id': main_image.id,
                'url': main_image.image.url
            }
        return None



class ProjectDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description','client' ,
                  'date', 'featured', 'category', 'images',
                  'created_at', 'updated_at']