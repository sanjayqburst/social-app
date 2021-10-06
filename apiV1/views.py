from rest_framework.response import Response
from rest_framework.views import APIView
from apiV1.serializers import CommentSerializer, ContentSerializer

from dashboard.models import Comment, Content


# Create your views here.
class CommentView(APIView):
    """
    Method for creating commnet view api
    """

    def get(self, request):
        """
        Method for handling get request in comment view api

        Returns:
            Serilizer.data response: return serialized data
        """
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Method for handling post request in comment view api

        Returns:
            Serilizer.data response: return serialized data
        """
        data = request.data
        serializers = CommentSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)


class ContentView(APIView):
    """
    Method for creating commnet view api
    """

    def get(self, request):
        """
        Method for handling get request in content view api

        Returns:
            Serilizer.data response: return serialized data
        """
        content = Content.objects.all()
        serializer = ContentSerializer(content, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Method for handling post request in content view api

        Returns:
            Serilizer.data response: return serialized data
        """
        data = request.data
        serializers = ContentSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
