from django.shortcuts import render,redirect
from .models import (Cow_Profile, Breed, Breed_Table, Milking_Record, Feeding_Record, Feed, Milk_Sales, Feed_Purchases,Reproduction,
                      Veterinary_Care,Birth_Records,Funfacts,Manure_Sales, MonthlyReport)
from .serializers import (Cow_ProfileSerializer, BreedSerializer, Breed_TableSerializer, Milking_RecordSerializer, Feeding_RecordSerializer,
    Feed_PurchasesSerializer, Milk_SalesSerializer, FeedSerializer,Veterinary_CareSerializer, 
    Birth_RecordsSerializer, MonthlyReportSerializer, FunfactsSerializer, Manure_SalesSerializer,ReproductionSerializer)
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse

class ListCreateFunfacts(generics.ListCreateAPIView):
  queryset = Funfacts.objects.all()
  serializer_class = FunfactsSerializer

class DestroyAPIViewFunfacts(generics.DestroyAPIView):
    queryset = Funfacts.objects.all()
    serializer_class = FunfactsSerializer

class ListCreateManure_Sales(generics.ListCreateAPIView):
  queryset = Manure_Sales.objects.all()
  serializer_class = Manure_SalesSerializer

class ListCreateMonthlyReport(generics.ListCreateAPIView):
  queryset =  MonthlyReport.objects.all()
  serializer_class =  MonthlyReportSerializer

def birthRecords(request):
  if request.method == "GET":
    breeds = Breed.objects.all()
    cows = Cow_Profile.objects.all()
    return render(request, 'birthRecords.html',{'cows':cows, 'breeds': breeds})
  if request.method == "POST":
    data ={'calf': request.POST['calf'],
                         'mother': request.POST['mother'],
                         'tag Number': request.POST['tag_Number'],
                          'weight': request.POST['weight'],
                          'gender': request.POST['gender'],
                          'date': request.POST['date']
                         }
    calf = Cow_Profile(name=request.POST['calf'],
               tag_Number=request.POST['tag_Number'],
               weight=request.POST['weight'],
               gender=request.POST['gender'],
               age=1
               )
    calf.save()
    calfhere = Cow_Profile.objects.get(id=calf.id)
    mother = Cow_Profile.objects.get(id=request.POST['mother'])
    birthrecord = Birth_Records(cow=mother,date=request.POST['date'],calf=calfhere)
    breedRecord = Breed_Table(breed=request.POST['Breed'],cow=calfhere)
    breedRecord.save()
    birthrecord.save()
    return redirect('/api/birthRecords/')
    
    
class ListCreateBirth_Records(generics.ListCreateAPIView):
    queryset = Birth_Records.objects.all()
    serializer_class = Birth_RecordsSerializer

class ListCreateVeterinary_Care(generics.ListCreateAPIView):
    queryset = Veterinary_Care.objects.all()
    serializer_class = Veterinary_CareSerializer


class ListCreateFeed_Purchases(generics.ListCreateAPIView):
    queryset = Feed_Purchases.objects.all()
    serializer_class = Feed_PurchasesSerializer


class ListCreateMilk_Sales(generics.ListCreateAPIView):
    queryset = Milk_Sales.objects.all()
    serializer_class = Milk_SalesSerializer

class DestroyAPIViewMilk_Sales(generics.DestroyAPIView):
    queryset = Milk_Sales.objects.all()
    serializer_class = Milk_SalesSerializer

class ListCreateFeeding_Record(generics.ListCreateAPIView):
    queryset = Feeding_Record.objects.all()
    serializer_class = Feeding_RecordSerializer


class ListCreateMilking_Record(generics.ListCreateAPIView):
    queryset = Milking_Record.objects.all()
    serializer_class = Milking_RecordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data['cow'].gender == 'male':
            return Response('bull cannot be milked!', status=status.HTTP_409_CONFLICT)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ReproductionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reproduction.objects.all()
    serializer_class = ReproductionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data['cow'].gender == 'male':
            return Response('bull cannot reproduce!', status=status.HTTP_409_CONFLICT)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ListCreateBreed(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class ListCreateBreedTable(generics.ListCreateAPIView):
    queryset = Breed_Table.objects.all()
    serializer_class = Breed_TableSerializer


class ListCreateCow_Profile(generics.ListCreateAPIView):
    queryset = Cow_Profile.objects.all()
    serializer_class = Cow_ProfileSerializer


class ListCreateFeed(generics.ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
