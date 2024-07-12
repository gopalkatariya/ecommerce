from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Category, SubCategory
from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer

# Category
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

# SubCategory
@api_view(['GET'])
def read_subcategory(request):
    search_query = request.query_params.get('s')
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


# Product
@api_view(['GET'])
def read_product(request):
    search_query = request.query_params.get('s')
    categorys = Product.objects.all()
    print(categorys)
    if search_query:
        categorys = categorys.filter(name__contains=search_query)
    category_serializer = ProductSerializer(categorys, many=True)
    return Response(category_serializer.data)


@api_view(['POST'])
def create_product(request):
    print(request.data)
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_product(request, pk):
    category = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=category, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_product(request, pk):
    category = Product.objects.get(id=pk)
    category.delete()
    return Response("Product successfully deleted")