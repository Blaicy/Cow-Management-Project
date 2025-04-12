from django.urls import path
from .views import (ListCreateCow, ListCreateBreed,
                    ListCreateBreedTable, ListCreateMilking_Record, ListCreateFeeding_Record,ListCreateFunfacts,
                    ListCreateFeed_Purchases, ListCreateFeed, ListCreateMilk_Sales, ListCreateVeterinary_Care, 
                    ListCreateBirth_Records,birthRecords,ListCreateMonthlyReport,
                    ListCreateManure_Sales,ReproductionListCreateAPIView,DestroyAPIViewFunfacts,DestroyAPIViewMilk_Sales)

urlpatterns = [
    path('', ListCreateCow.as_view()),
    path('breed/', ListCreateBreed.as_view()),
    path('breedTable/', ListCreateBreedTable.as_view()),
    path('milkingRecord/', ListCreateMilking_Record.as_view()),
    path('feedingRecord/', ListCreateFeeding_Record.as_view()),
    path('feedsRecord/', ListCreateFeed.as_view()),
    path('feedPurchases/', ListCreateFeed_Purchases.as_view()),
    path('milkSales/', ListCreateMilk_Sales.as_view()),
    path('veterinary/', ListCreateVeterinary_Care.as_view()),
    path('birthRecords/', ListCreateBirth_Records.as_view()),
    path('record/',birthRecords, name='birthRecords'),
    path('report/',ListCreateMonthlyReport.as_view()),
    path('funFacts/',ListCreateFunfacts.as_view()),
    path('manureSales/',ListCreateManure_Sales.as_view()),
    path('<int:pk>/funFacts/delete/',DestroyAPIViewFunfacts.as_view()),
    path('<int:pk>/milkSales/delete/',DestroyAPIViewMilk_Sales.as_view()),
    path('reproduction/', ReproductionListCreateAPIView.as_view()),
    
]
