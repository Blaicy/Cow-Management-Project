from django.urls import path
from .views import (ListCreateCow_Profile, ListCreateBreed,
                    ListCreateBreedTable, ListCreateMilking_Record, ListCreateFeeding_Record,ListCreateFunfacts,
                    ListCreateFeed_Purchases, ListCreateFeed, ListCreateMilk_Sales, ListCreateVeterinary_Care, 
                    ListCreateBirth_Records,birthRecords,ListCreateMonthlyReport,
                    ListCreateManure_Sales,ReproductionListCreateAPIView,DestroyAPIViewFunfacts,DestroyAPIViewMilk_Sales)

urlpatterns = [
    path('Cow_Profile', ListCreateCow_Profile.as_view()),
    path('Breed/', ListCreateBreed.as_view()),
    path('BreedTable/', ListCreateBreedTable.as_view()),
    path('Milking_Record/', ListCreateMilking_Record.as_view()),
    path('Feeding_Record/', ListCreateFeeding_Record.as_view()),
    path('Feeds/', ListCreateFeed.as_view()),
    path('Feed_Purchases/', ListCreateFeed_Purchases.as_view()),
    path('Milk_Sales/', ListCreateMilk_Sales.as_view()),
    path('Veterinary_Care/', ListCreateVeterinary_Care.as_view()),
    path('Birth_Records/', ListCreateBirth_Records.as_view()),
    path('Birthrecord/',birthRecords, name='birthRecords'),
    path('MonthlyReport/',ListCreateMonthlyReport.as_view()),
    path('Funfacts/',ListCreateFunfacts.as_view()),
    path('Manure_Sales/',ListCreateManure_Sales.as_view()),
    path('<int:pk>/Funfacts/delete/',DestroyAPIViewFunfacts.as_view()),
    path('<int:pk>/Milk_Sales/delete/',DestroyAPIViewMilk_Sales.as_view()),
    path('Reproduction/', ReproductionListCreateAPIView.as_view()),
    
]
