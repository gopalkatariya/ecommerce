from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import SubCategory
from .serializers import SubCategorySerializer


@api_view(['GET'])
def read_subcategory(request):
    search_query = request.query_params.get('s')
    categorys = SubCategory.objects.select_related('category_id')
    categorys = SubCategory.objects.all()
    print(categorys)
    if search_query:
        categorys = categorys.filter(name__contains=search_query)
    category_serializer = SubCategorySerializer(categorys, many=True)
    return Response(category_serializer.data)


@api_view(['POST'])
def create_subcategory(request):
    print(request.data)
    serializer = SubCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_subcategory(request, pk):
    category = SubCategory.objects.get(id=pk)
    serializer = SubCategorySerializer(instance=category, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_subcategory(request, pk):
    category = SubCategory.objects.get(id=pk)
    category.delete()
    return Response("SubCategory successfully deleted")