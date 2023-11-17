from rest_framework import generics

from .serializer import PeopleSerializer
from .models import People


class PeopleAPIList(generics.ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class PeopleAPIUpdate(generics.UpdateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class PeopleAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


# class PeopleAPIView(APIView):
#     def get(self, request):
#         w = People.objects.all()
#         return Response({'posts': PeopleSerializer(w, many=True).data})

#     def post(self, request):
#         serializer = PeopleSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'post': serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})

#         try:
#             isinstance = People.objects.get(pk=pk)
#         except:
#             return Response({'error':'Object does not exist'})

#         serializer = PeopleSerializer(data=request.data, instance=isinstance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method DELETE not allowed'})

#         People.objects.filter(pk=pk).delete()

#         return Response({'error': 'Delete post' + str(pk)})


# class PeopleAPIView(generics.ListAPIView):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer
