from .models import (Cow_Profile, Breed, Breed_Table, Milking_Record, Feeding_Record, Feed, Feed_Purchases,Funfacts,Reproduction,
                      Milk_Sales, Veterinary_Care, Birth_Records,Manure_Sales,MonthlyReport, About_Us)

from rest_framework import serializers
from datetime import timedelta,date
from django.shortcuts import get_object_or_404,redirect
from django.db.models import Sum, F, ExpressionWrapper,DecimalField

class About_UsSerializer(serializers.ModelSerializer):
    fields = '__all__'

class ReproductionSerializer(serializers.ModelSerializer):
    mating_records = serializers.SerializerMethodField() 
    estimated_delivery = serializers.SerializerMethodField(read_only=True) 
    class Meta:
        model = Reproduction
        fields = ['cow',
                  'mating_records',
                  'estimated_delivery']

    def mating_records(self,obj):
        return obj.mating_records.create()
    def get_estimated_delivery(self,obj):
        if obj.mating_records:
            return obj.mating_records + timedelta(days=283)
        return None

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'

class Cow_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cow_Profile
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
    monthly_manure_sales = serializers.SerializerMethodField()
    class Meta:
        model = Manure_Sales
        fields = ['quantity','price_per_kg','manure_sales','monthly_manure_sales']

    def get_manure_sales(self,obj):
        manure_sales = obj.quantity*obj.price_per_kg
        return manure_sales
    def get_monthly_manure_sales(self,obj):
        year = obj.date.year
        month = obj.date.month
        start_date = date(year, month, 1)
        if month == 12:
            end_date = date(year + 1,1,1)
        else:
            end_date = date(year, month + 1,1)
        sales = Manure_Sales.objects.filter(date__gte=start_date, date__lt=end_date)
        total = sales.aggregate(total_sales=Sum(ExpressionWrapper(F('quantity') * F('price_per_kg'),
                                                                  output_field=DecimalField())))
        return (total['total_sales'] or 0,year-month)


class FunfactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funfacts
        fields = '__all__'

class Milk_SalesSerializer(serializers.ModelSerializer):
    milk_sales = serializers.SerializerMethodField()
    monthly_milk_sales = serializers.SerializerMethodField()
    class Meta:
        model = Milk_Sales
        fields = ['litres','price_per_litre','milk_sales','monthly_milk_sales']

    def get_milk_sales(self,obj):
        milk_sales = obj.litres*obj.price_per_litre
        return milk_sales
    
    def get_monthly_milk_sales(self,obj):
        year = obj.date.year
        month = obj.date.month
        start_date = date(year, month, 1)
        if month == 12:
            end_date = date(year + 1,1,1)
        else:
            end_date = date(year, month + 1,1)
        sales = Milk_Sales.objects.filter(date__gte=start_date, date__lt=end_date)
        total = sales.aggregate(total_sales=Sum(ExpressionWrapper(F('litres') * F('price_per_litre'),
                                                                  output_field=DecimalField())))
        
        return (total['total_sales'] or 0,year,month)
    

class Milking_RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milking_Record
        fields = '__all__'


class Feeding_RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeding_Record
        fields = '__all__'


class Feed_PurchasesSerializer(serializers.ModelSerializer):
    feed_purchases = serializers.SerializerMethodField()
    monthly_feed_purchases = serializers.SerializerMethodField()
    class Meta:
        model = Feed_Purchases
        fields = ['quantity','feed_type','price_per_kg','feed_purchases','monthly_feed_purchases']

    def get_feed_purchases(self,obj):
        feed_purchases = obj.quantity*obj.price_per_kg
        return feed_purchases
    
    def get_monthly_feed_purchases(self,obj):
        year = obj.date.year
        month = obj.date.month
        start_date = date(year, month, 1)
        if month == 12:
            end_date = date(year + 1,1,1)
        else:
            end_date = date(year, month + 1,1)
        purchases = Feed_Purchases.objects.filter(date__gte=start_date, date__lt=end_date)
        total = purchases.aggregate(total_sales=Sum(ExpressionWrapper(F('quantity') * F('price_per_kg'),
                                                                  output_field=DecimalField())))
        return (total['total_sales'] or 0,year,month)

class Veterinary_CareSerializer(serializers.ModelSerializer):
    monthly_veterinary_cost = serializers.SerializerMethodField()
    class Meta:
        model = Veterinary_Care
        fields = ['cow','veterinary_cost','monthly_veterinary_cost']

    def get_monthly_veterinary_cost(self,obj):
        year = obj.date.year
        month = obj.date.month
        start_date = date(year, month, 1)
        if month == 12:
            end_date = date(year + 1,1,1)
        else:
            end_date = date(year, month + 1,1)
        total = Veterinary_Care.objects.filter(date__gte=start_date, date__lt=end_date).aggregate(
                total_cost=Sum('veterinary_cost'))
        
        return (total['total_cost'] or 0,year,month)

class Birth_RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Birth_Records
        fields = '__all__'
  
class MonthlyReportSerializer(serializers.ModelSerializer):
    milk_sales_total = serializers.SerializerMethodField()
    manure_sales_total = serializers.SerializerMethodField()
    feed_purchases_total = serializers.SerializerMethodField()
    veterinary_care_total = serializers.SerializerMethodField()
    total_income = serializers.SerializerMethodField()
    total_expense = serializers.SerializerMethodField()
    net_profit = serializers.SerializerMethodField()

    class Meta:
        model = MonthlyReport
        fields = ['month','feed_purchases_total','veterinary_care_total','milk_sales_total','manure_sales_total',
                  'total_income','total_expense','net_profit']

    def get_milk_sales_total(self,obj):
        return obj.milk_sales_total
    def get_manure_sales_total(self,obj):
        return obj.manure_sales_total
    def get_feed_purchases_total(self,obj):
        return obj.feed_purchases_total
    def get_veterinary_care_total(self,obj):
        return obj.veterinary_care_total
    def get_total_income(self,obj):
        return obj.total_income
    def get_total_expense(self,obj):
        return obj.total_expense
    def get_net_profit(self,obj):
        return obj.net_profit