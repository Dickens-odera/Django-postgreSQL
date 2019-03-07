#translates the posts to json formart
from rest_framework import serializers
from .models import Posts

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"
        read_only_fields = ['id']

    #validate the title to only allow a unique tittle
    def validate_title(self, value):
        title_to_validate = Posts.objects.filter(title__iexact = value)
        #exclude the priary key pk/id
        if self.instance:
            title_to_validate = title_to_validate.exclude(id = self.instance.id)
        if title_to_validate.exists():
            raise serializers.ValidationError('The title already exists')
        return value
        