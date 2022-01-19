from rest_framework import serializers
from BackEndAPI.models import Articles


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = (
            'id',
            'Title',
            'Image',
            'HeaderImage',
            'Introduction',
            'Description',
            'LastMod',
            'Language',
            'KeyWords',
            'State',
            'NumVisit',
            'IdTheme',
            'IdUser',
            'IdHost'
        )
