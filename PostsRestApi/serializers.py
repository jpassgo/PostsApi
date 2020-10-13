from rest_framework import serializers
from talk.models import post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'created', 'updated')