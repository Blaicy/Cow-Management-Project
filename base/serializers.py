from .models import (Cow, Breed, Breed_Table, Milking_Record, Feeding_Record, Feed, Feed_Purchases,Funfacts,
                      Milk_Sales,Immunisation_Records, Veterinary_Care, Birth_Records,Manure_Sales,MonthlyReport)

from rest_framework import serializers
from datetime import datetime


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'

class CowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cow
        fields = '__all__'

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'

class Breed_TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breed_Table
        fields = [
            'breed',
            'cow'
        ]

class Manure_SalesSerializer(serializers.ModelSerializer):
    manure_sales = serializers.SerializerMethodField()
    class Meta:
        unique_together = ['month']
        model = Manure_Sales
        fields = ['quantity','cost','manure_sales']

    def get_manure_sales(self,obj):
        manure_sales = obj.quantity*obj.cost
        return manure_sales

class FunfactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funfacts
        fields = '__all__'

class Milk_SalesSerializer(serializers.ModelSerializer):
    milk_sales = serializers.SerializerMethodField()
    monthly_sales = serializers.SerializerMethodField()
    class Meta:
        unique_together = ['month']
        model = Milk_Sales
        fields = ['litres','cost','milk_sales','monthly_sales']

    def get_milk_sales(self,obj):
        milk_sales = obj.litres*obj.cost
        return milk_sales
    
    def get_monthly_sales(self,obj):
        monthly_sales = obj.litres*obj.cost*30
        return monthly_sales

    # def get_milk_sales(self,obj):
    #     milk_sales = 0
    #     try:
    #         milksales = Milk_Sales.objects.all()
    #         for milksale in milksales:
    #             milk_sales = milksale.litres*milksale.cost
    #         return milk_sales
    #     except:
    #         return milk_sales


class Milking_RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milking_Record
        exclude = ['date']


class Feeding_RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeding_Record
        exclude = ['date']


class Feed_PurchasesSerializer(serializers.ModelSerializer):
    feed_purchases = serializers.SerializerMethodField()
    class Meta:
        model = Feed_Purchases
        fields = ['quantity','feed_type','cost','feed_purchases']

    def get_feed_purchases(self,obj):
        feed_purchases = obj.quantity*obj.cost
        return feed_purchases

class Immunisation_RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Immunisation_Records
        exclude = ['date']


class Veterinary_CareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinary_Care
        fields = '__all__'


class Birth_RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Birth_Records
        exclude = ['date']


# class Profit_LossSerializer(serializers.ModelSerializer):
#   milk_sales = serializers.SerializerMethodField()
#   feeding_cost = serializers.SerializerMethodField()
#   veterinary_care = serializers.SerializerMethodField()
#   total_MilkSales = serializers.SerializerMethodField()
#   class Meta:
#     model = Milk_Sales
#     fields = ['milk_sales',
#               'feeding_cost',
#               'veterinary_care',
#               'total_MilkSales'
#               ]
    
#     def get_milk_sales(self,obj):
#         milk_sales = 0
#         try:
#             milksales = Milk_Sales.objects.all()
#             for milksale in milksales:
#                 milk_sales += milksale.litres*milksale.cost
#             return milk_sales
#         except:
#             return milk_sales

#     def get_feeding_cost(self,obj):
#         feeding_cost = 0
#         try:
#             feedingcosts = Feed_Purchases.objects.all()
#             for feedingcost in feedingcosts:
#                 feeding_cost +=feedingcost.quantity*feedingcost.cost
#             return feeding_cost
#         except:
#             return feeding_cost
    
#     def get_veterinary_care(self,obj):
#         veterinary_care = 0
#         try:
#             cares = Veterinary_Care.objects.all()
#             for care in cares:
#                 veterinary_care +=care.quantity*care.cost
#             return veterinary_care
#         except:
#             return veterinary_care
  
class MonthlyReportSerializer(serializers.ModelSerializer):
    milk_sales = serializers.SerializerMethodField()
    manure_sales = serializers.SerializerMethodField()
    feed_purchase = serializers.SerializerMethodField()
    net_profit = serializers.SerializerMethodField()

    class Meta:
        model=MonthlyReport
        field=['month','feed_purchases','veterinary_cost','milk_sales','manure_sales','net_profit']

    def get_milk_sales(self,obj):
        milk_sale=Milk_Sales()
        return milk_sale.get_monthly_sales(obj.month)

    def get_manure_sales(self,obj):
        manure_sale=Manure_Sales()
        return manure_sale.get_monthly_sales(obj.month)
    
    def get_feed_purchases(self,obj):
        feed_purchases=Feed_Purchases()
        return feed_purchases.get_monthly_sales(obj.month)
    
    def get_net_profit(self,obj):
        milk_sales=self.get_milk_sales(obj)
        manure_sales=self.get_manure_sales(obj)
        return(milk_sales+manure_sales)-(obj.feed_purchases+obj.veterinary_cost)
      