from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ProductSerializer, ImageSerializer
from .models import Product, Image
from rest_framework.decorators import action
from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_flex_fields import is_expanded
import django_filters.filterset

class ImageViewSet(FlexFieldsModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ProductViewSet(FlexFieldsMixin,ReadOnlyModelViewSet):

    serializer_class = ProductSerializer

    # permit what can be expandend
    permit_list_expands = ['category', 'sites', 'comments', 'sites.company','sites.productsize']

    # dynamic filtering
    filterset_fields = ('category',)

    # select_related() “follows” foreign-key relationships, selecting additional related-object data when it 
    # executes its query. we use select_related when the object that you’re going to be selecting is a 
    # single object. (OneToOneField, ForeignKey)
   
    # prefetch_related() does a separate lookup for each relationship, and does the “joining” in Python . 
    # You use prefetch_related when you’re going to get a “set” of things. (ManyToManyField, Reverse ForeignKey)
    
    # is_expaned() examines request object to return boolean of whether passed field is expanded.

    def get_queryset(self):
        queryset = Product.objects.all()

        if is_expanded(self.request, 'category'):
            queryset = queryset.prefetch_related('category')

        if is_expanded(self.request, 'comments'):
            queryset = queryset.prefetch_related('comments')

        if is_expanded(self.request, 'sites'):
            queryset = queryset.prefetch_related('sites')
        
        if is_expanded(self.request, 'company'):
            queryset = queryset.prefetch_related('sites__company')
        
        if is_expanded(self.request, 'productsize'):
            queryset = queryset.prefetch_related('sites__productsize')

        return queryset