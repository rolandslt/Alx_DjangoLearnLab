from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, filters, generics
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType



class IsAuthorOrReadOnly(permissions.BasePermission):
    """Custom permission to only allow authors of an object to edit it."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Step 3 logic: Get posts from users the current user follows
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if created:
            # Create Notification for the author
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post,
                target_content_type=ContentType.objects.get_for_model(post),
                target_object_id=post.id
            )
            return Response({"message": "Post liked."}, status=status.HTTP_201_CREATED)
        return Response({"error": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post)
        if like.exists():
            like.delete()
            return Response({"message": "Post unliked."}, status=status.HTTP_200_OK)
        return Response({"error": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)