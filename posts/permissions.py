from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class IsCorrectedAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.post.author == request.user


class IsCompetentCorrector(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_native_language = request.user.learning_language != obj.language
        is_higher_level = int(request.user.level) > int(obj.difficulty)
        is_not_post_author = request.user != obj.author

        return (is_native_language or is_higher_level) and is_not_post_author
