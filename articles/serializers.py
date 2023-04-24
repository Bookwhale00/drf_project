from rest_framework import serializers
from articles.models import Article


class ArticleSerializer (serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Article
        fields = "__all__"


class ArticleCreateSerializer (serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "image", "content")


class ArticleListSerializer (serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Article
        fields = ("pk", "title", "image", "updated_at", "user")
