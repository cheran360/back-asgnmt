from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class CreateRecordTestCase(APITestCase):
    def test_createrecord(self):
        data = {"image":'',
                "name":"testcase", 
                "species":"testcasesp", 
                "weight":4,
                "length":56,
                "latitude":78.4,
                "longitude":56.6}
        response = self.client.post(reverse("createRecord"),data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getrecords(self):
        response = self.client.get(reverse("getAllRecords"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)