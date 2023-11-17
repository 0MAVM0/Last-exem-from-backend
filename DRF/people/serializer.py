import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import People


# class PeopleModel:
#     def init(self, title, content):
#         self.title = title
#         self.content = content



class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = "__all__"



# def encode():
#     model = PeopleModel("King", "Conten: King")
#     model_sr = PeopleSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)


# def decode():
#     stream = io.BytesIO(b'{"title": "Leonel Messi", "content":"Content: Leonel Andres Messi Cuccittini"}')
#     data = JSONParser().parse(stream)
#     serializer = PeopleSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)