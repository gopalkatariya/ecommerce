from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer


@api_view(['GET'])
def read_category(request):
    search_query = request.query_params.get('s')
    categorys = Category.objects.all()
    if search_query:
        categorys = categorys.filter(name__contains=search_query)
    category_serializer = CategorySerializer(categorys, many=True)
    return Response(category_serializer.data)


@api_view(['POST'])
def create_category(request):
    print(request.data)
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_category(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=category, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return Response("Category successfully deleted")