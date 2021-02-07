from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RequirementsSerializer
from .models import Requirements
from rest_framework import viewsets, filters
import requests



# Create your views here.
class RequirementsViewSet(viewsets.ModelViewSet):
    #search_fields = ['name']
    #filter_backends = (filters.SearchFilter)
    serializer_class = RequirementsSerializer
    queryset = Requirements.objects.all()


def index(request):
    return render(request, 'index.html')


# def viewset(request):
#     result = request.GET['name']
#     print(result)
#     data = requests.get('http://127.0.0.1:8000/viewsets/requirements', params=request.GET)
#     #print(data.json())
#     return render(request, 'viewset.html', {'result':data})


#The following codes were created for learning purposes and poses same functionalities as the above codes.

# class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
#     serializer_class = RequirementsSerializer
#     queryset = Requirements.objects.all()

#     lookup_field = 'id'
#     #authentication_classes = [SessionAuthentication, BasicAuthentication]
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, id=None):
#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)

#     def post(self, request):
#         return self.create(request)

#     def put(self, request, id=None):
#         return self.update(request, id)

#     def delete(self, request, id):
#         return self.delete(request, id)

# class RequirementsAPIView(APIView):
    
#     def get(self, request):
#         requirements = Requirements.objects.all()
#         serializer = RequirementsSerializer(requirements, many=True)
#         return response(serializer.data)

#     def post(self, request):
#         serializer = RequirementsSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class RequirementsDetails(APIView):
    
#     def get_object(self, id):
#         try:
#             return Requirements.objects.get(id=id)
#         except Requirements.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, id):
#         requirements = self.get_object(id)
#         serializer = RequirementsSerializer(requirements)
#         return Response(serializer.data)

#     def put(self, request, id):
#         requirements = self.get_object(id)
#         serializer = RequirementsSerializer(requirements, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         requirements = self.get_object(id)
#         requirements.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def req_list(request):

#     if request.method == 'GET':
#         requirements = Requirements.objects.all()
#         serializer = RequirementsSerializer(requirements, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = RequirementsSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def req_detail(request, pk):
#     try:
#         requirements = Requirements.objects.get(pk=pk)
#     except Requirements.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = RequirementsSerializer(requirements)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = RequirementsSerializer(requirements, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         requirements.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)