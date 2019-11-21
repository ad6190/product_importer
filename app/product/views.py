from product.serializers import ProductSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import viewsets

from product.models import Product


class ProductViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product_list.html'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        return Response({'products': queryset})




