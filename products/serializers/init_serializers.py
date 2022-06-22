
'''
This file contains serializers
        - Product Categories, Countries, Sub_Categories, Brand 
        - Products, Product_images, ProductReview
'''

# import section 
from rest_framework import serializers

from products.database.slider import Slider
from products.database.init_p import Categories, Countreies, Sub_Categories,  Brand
from products.database.products import Products, Product_images
from products.database.reviews import ProductReview

''' 
Category
subcategory
brand
countries
 '''

#  CategorySerializers 
class CategoriesSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False, use_url=True, required=False)
    class Meta:
        model = Categories
        fields="__all__"
        depth = 1

#  SubCategorySerializers 
class SubCategoriesSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False, use_url=True, required=False)
    categories = CategoriesSerializers(many=True, read_only=True)
    class Meta:
        model = Sub_Categories
        fields="__all__"

# BrandSerrializer
class BrandSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Brand
        fields = '__all__'

# CountrySerializer 
class CountriesSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Countreies
        fields = '__all__'





'''
Products Review serializer
'''
class ProductReviewSerailizers(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ['id','profile','product','star_count','review']


'''
Slider Serializers
'''
class SliderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'