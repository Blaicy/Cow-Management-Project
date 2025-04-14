from django.db import models
from django.db.models import Sum, F, ExpressionWrapper,DecimalField
from datetime import timedelta,date

class Cow_Profile(models.Model):
    name = models.CharField(max_length=255)
    tag_Number = models.CharField(max_length=255, unique=True)
    age = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    OPTION_ONE = 'male'
    OPTION_TWO = 'female'
    OPTION_CHOICES = [(OPTION_ONE, 'bull'),
                      (OPTION_TWO, 'heifer')]
    gender = models.CharField(
        max_length=255, choices=OPTION_CHOICES, default=OPTION_TWO)

    def __str__(self):
        return self.tag_Number + "-" + self.name

class Breed(models.Model):
    breed_name = models.CharField(max_length=255)

    def __str__(self):
        return self.breed_name

class Breed_Table(models.Model):
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    cow = models.ForeignKey(Cow_Profile, on_delete=models.CASCADE)

class Milking_Record(models.Model):
    cow = models.ForeignKey(Cow_Profile, on_delete=models.CASCADE)
    litres = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    OPTION_ONE = 'morning'
    OPTION_TWO = 'noon'
    OPTION_THREE = 'evening'
    OPTION_CHOICES = [(OPTION_ONE, 'morning'),
                      (OPTION_TWO, 'noon'),
                      (OPTION_THREE, 'evening')
                      ]
    session = models.CharField(
        max_length=255, choices=OPTION_CHOICES, default=OPTION_ONE)

class Milk_Sales(models.Model):
    litres = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    price_per_litre = models.DecimalField(max_digits=7, decimal_places=2)

class Feed(models.Model):
    feed_type = models.CharField(max_length=255)
    feed_quantity = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.feed_type

class Feeding_Record(models.Model):
    cow = models.ForeignKey(Cow_Profile, on_delete=models.CASCADE)
    feed_type = models.ForeignKey(Feed, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    OPTION_ONE = 'morning'
    OPTION_TWO = 'noon'
    OPTION_THREE = 'evening'
    OPTION_CHOICES = [(OPTION_ONE, 'morning'),
                      (OPTION_TWO, 'noon'),
                      (OPTION_THREE, 'evening')
                      ]
    session = models.CharField(
        max_length=255, choices=OPTION_CHOICES, default=OPTION_ONE)

class Feed_Purchases(models.Model):
    feed_type = models.ForeignKey(Feed, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    price_per_kg = models.DecimalField(max_digits=7, decimal_places=2)

class Veterinary_Care(models.Model):
    cow = models.ForeignKey(Cow_Profile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    veterinary_cost = models.DecimalField(max_digits=7, decimal_places=2)

class Birth_Records(models.Model):
    cow = models.ForeignKey(
        Cow_Profile, on_delete=models.CASCADE, related_name='mother')
    date = models.DateField(auto_now_add=True)
    calf = models.ForeignKey(Cow_Profile, on_delete=models.CASCADE)

class Funfacts(models.Model):
    fact = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Manure_Sales(models.Model):
    quantity = models.DecimalField(max_digits=7, decimal_places=2)
    price_per_kg = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(default=date.today)

class Reproduction(models.Model):
    cow = models.ForeignKey(Cow_Profile, on_delete=models.CASCADE)
    mating_records = models.DateField()
    gestation_period = models.IntegerField(default=0, help_text="Gestation period in days")

class MonthlyReport(models.Model):
    month = models.DateField()

    @property
    def start_end_dates(self):
        start = self.month.replace(day=1)
        end = (start + timedelta(days=32)).replace(day=1)
        return start, end
    
    @property
    def milk_sales_total(self):
        start, end = self.start_end_dates
        return Milk_Sales.objects.filter(date__gte=start, date__lt=end).aggregate(
            total=Sum(ExpressionWrapper(F('litres') * F('price_per_litre'),output_field=DecimalField()))
            )['total'] or 0
        
    @property
    def manure_sales_total(self):
        start, end = self.start_end_dates
        return Manure_Sales.objects.filter(date__gte=start, date__lt=end).aggregate(
            total=Sum(ExpressionWrapper(F('quantity') * F('price_per_kg'),output_field=DecimalField()))
            )['total'] or 0
    
    @property
    def feed_purchases_total(self):
        start, end = self.start_end_dates
        return Feed_Purchases.objects.filter(date__gte=start, date__lt=end).aggregate(
            total=Sum(ExpressionWrapper(F('quantity') * F('price_per_kg'),output_field=DecimalField()))
            )['total'] or 0
    
    @property
    def veterinary_care_total(self):
        start, end = self.start_end_dates
        return Veterinary_Care.objects.filter(date__gte=start, date__lt=end).aggregate(
            total=Sum('veterinary_cost')
            )['total'] or 0
    
    @property
    def total_income(self):
        return self.milk_sales_total + self.manure_sales_total
    
    @property
    def total_expense(self):
        return self.feed_purchases_total + self.veterinary_care_total
    
    @property
    def net_profit(self):
        return self.total_income - self.total_expense