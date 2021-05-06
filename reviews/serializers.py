from .models import Product, Category, Comment, Company, ProductSite, ProductSize, Image
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_flex_fields import FlexFieldsModelSerializer
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# Default payload includes the user_id. You can add any information you want, you just have to modify the claim.

# For add claims to payload we need to create a subclass for TokenObtainPairView as well as a subclass for 
# TokenObtainPairSerializer.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # add custom claims
        token['username'] = user.username
        return token

class CompanySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Company
        fields = ['pk', 'name','url']


class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['pk','name']
        expandable_fields = {
            'products': ('reviews.ProductSerializer', {'many': True})
        }


class ProductSizeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['pk','name']


class ImageSerializer(FlexFieldsModelSerializer):

    # The sizes argument on VersatileImageFieldSerializer simply unpacks the list of 2-tuples 
    # using the value in the first position as the attribute of the image and the second position
    # as a ‘Rendition Key’ which dictates how the original image should be modified.

    image = VersatileImageFieldSerializer(
        sizes= 'product_headshot'
    )

    class Meta:
        model = Image
        fields = ['pk', 'name', 'image']



class ProductSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Product
        fields = ['pk', 'name', 'content', 'created', 'updated']
        expandable_fields = {
            'category': ('reviews.CategorySerializer', {'many': True}),
            'sites': ('reviews.ProductSiteSerializer', {'many': True}),
            'comments': ('reviews.CommentSerializer', {'many': True}),
            'image': ('reviews.ImageSerializer', {'many': True}),
        }


class ProductSiteSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSite
        fields = ['pk', 'name', 'price', 'url', 'created', 'updated']
        expandable_fields = {
            'product' : 'reviews.CategorySerializer',
            'productsize' : 'reviews.ProductSizeSerializer',
            'company': 'reviews.CompanySerializer',
        }

class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'title', 'content', 'created', 'updated']
        expandable_fields = {
            'product' : 'reviews.CategorySerializer',
            'user': 'reviews.UserSerializer',
        }