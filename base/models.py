from django.db import models



class Cow(models.Model):
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
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)


class Milking_Record(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
    liters = models.FloatField()
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
    litres = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)
    cost = models.FloatField(default=0)


class Feed(models.Model):
    feed_type = models.CharField(max_length=255)
    feed_quantity = models.FloatField()

    def __str__(self):
        return self.feed_type


class Feeding_Record(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
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
    cost = models.FloatField(default=0)


class Immunisation_Records(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    medicine = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    next_date = models.DateField(null=True, blank=True)


class Veterinary_Care(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    veterinary_cost = models.FloatField(default=0)


class Birth_Records(models.Model):
    cow = models.ForeignKey(
        Cow, on_delete=models.CASCADE, related_name='mother')
    date = models.DateField(auto_now_add=True)
    calf = models.ForeignKey(Cow, on_delete=models.CASCADE)


class Funfacts(models.Model):
    fact = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Manure_Sales(models.Model):
    quantity = models.FloatField(default=0)
    cost = models.FloatField(default=0)

class MonthlyReport(models.Model):
    veterinary_cost = models.FloatField(default=0)
    month = models.DateField()
