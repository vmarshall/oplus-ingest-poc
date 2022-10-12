import json
import os

import requests
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from django.urls import path
from django.views.generic import TemplateView
from haversine import haversine_vector, Unit
from requests import Response
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import api_view

from hospital.serializers import FacilitySerializer
from hospital.models import Facility
from rest_framework.response import Response


@api_view(['GET'])
def refresh(request):

    # Fetch data from Soda API
    url = "https://data.cityofnewyork.us/resource/ymhw-9cz9.json"
    response = requests.get(url)
    data = json.loads(response.text)

    # Create a new directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Write the data to a file
    with open('data/hospitals.json', 'w') as outfile:
        json.dump(data, outfile)
    for facility in data:
        new_facility = Facility.objects.create(
            facility_name=facility['facility_name'],
            latitude=facility['location_1']['latitude'],
            longitude=facility['location_1']['longitude'],
        )
        new_facility.save()


    return Response(status=status.HTTP_200_OK)
    # Print the number of records fetched
    # print("Number of records fetched: " + str(len(data)))
    # return Response(status=status.HTTP_200_OK)

def find_closest_hospitals(lat, lng, facilities):
    # Create a list of tuples of latitude and longitude
    coordinates = [(facility.latitude, facility.longitude) for facility in facilities]

    # Create a tuple of latitude and longitude
    user_coordinates = (lat, lng)

    # Find the closest hospitals
    closest_hospitals = haversine_vector(user_coordinates, coordinates, Unit.MILES)
    print(closest_hospitals)

    # Sort the hospitals by distance
    sorted_hospitals = sorted(zip(closest_hospitals, facilities), key=lambda x: x[0])

    # Return the closest hospitals
    return sorted_hospitals[:5]
#
@api_view(['GET'])
def facilities(request):
    """
    List all code facilities, or create a new facility.
    """
    if request.method == 'GET':

        facilities = Facility.objects.all()
        serializer = FacilitySerializer(facilities, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FacilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def facility_detail(request, pk):
    """
    Retrieve, update or delete a code facility.
    """
    try:
        facility = Facility.objects.get(pk=pk)
    except Facility.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FacilitySerializer(facility)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FacilitySerializer(facility, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        facility.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FacilityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Facility.objects.all().order_by('-created_at')
    serializer_class = FacilitySerializer
    permission_classes = [permissions.IsAuthenticated]





@api_view(['GET'])
def get_closest_hospitals(request):
    lat = request.query_params.get('lat')
    lng = request.query_params.get('lng')
    n = request.query_params.get('n')
    facilities = Facility.objects.all()
    closest_facilities = find_closest_hospitals(lat, lng, facilities)
    serializer = FacilitySerializer(facilities, many=True)
    return Response(serializer.data)