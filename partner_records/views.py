from django.shortcuts import render

# Create your views here.
import json
import os

import requests
from requests import Response
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import api_view


from rest_framework.response import Response

from partner_records.models import PartnerRecord
from partner_records.serializers import PartnerRecordSerializer

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

@api_view(['GET'])
def generate_pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    partner_record = PartnerRecord.objects.first()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(400, 600, "Oplus Health Record")
    p.drawString(100, 320, "Partner: " + partner_record.partner_name)
    p.drawString(100, 340, "Patient: " + str(partner_record.patient))
    p.drawString(100, 300, "Notes: " + str(partner_record.doctor_notes.summary))

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='oplus_health_record.pdf')

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
    for partner_record in data:
        new_partner_record = PartnerRecord.objects.create(
            partner_record_name=partner_record['partner_record_name'],
            latitude=partner_record['location_1']['latitude'],
            longitude=partner_record['location_1']['longitude'],
        )
        new_partner_record.save()


    return Response(status=status.HTTP_200_OK)
    # Print the number of records fetched
    # print("Number of records fetched: " + str(len(data)))
    # return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def partner_records_list(request):
    partner_records = PartnerRecord.objects.all()
    serializer = PartnerRecordSerializer(partner_records, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def partner_record_detail(request, pk):
    """
    Retrieve, update or delete a code partner_record.
    """
    try:
        partner_record = PartnerRecord.objects.get(pk=pk)
    except PartnerRecord.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PartnerRecordSerializer(partner_record)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PartnerRecordSerializer(partner_record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        partner_record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PartnerRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PartnerRecord.objects.all().order_by('-created_at')
    serializer_class = PartnerRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

