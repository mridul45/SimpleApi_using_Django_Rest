from rest_framework import serializers
from .models import *
import re
from django.template.defaultfilters import slugify


class TodoSerializer(serializers.ModelSerializer):

    slug = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ['user','todo_title','slug','todo_description','is_done','uid']


    def get_slug(self,obj):
        return slugify(obj.todo_title)


    def validate_todo_title(self,data):

        if data.get('todo_title'):
                todo_title = data['todo_title']

                regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

                if len(todo_title)<3:
                    raise serializers.ValidationError('Todo title must be more than 3 chars')

                if not regex.search(todo_title) == None:

                    raise serializers.ValidationError('Serialisers cannot contain special chracters')

        # def validate(self,validated_data):
            

        #     return validated_data

        return data
        

class TimingTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimingTodo
        exclude = ['created_at','updated_at']