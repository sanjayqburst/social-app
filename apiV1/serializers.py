from dashboard.models import Content, Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        if instance is not None:
            instance.save()
            return instance


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        if instance is not None:
            instance.save()
            return instance
