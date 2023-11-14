from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import People

class PeopleModel:
    def init(self, title, content):
        self.title = title
        self.content = content


class PeopleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()


def encode():
    model = PeopleModel("King", "Conten: King")
    model_sr = PeopleSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)