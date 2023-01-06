from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from products.models import Product


class ProductAPITestCase(APITestCase):

    fixtures = [
        "products/fixtures/testing_products.json"
    ]

    def test_products_list(self):
        #reverse делает из name путь url
        url = reverse("products_list_create")
        response = self.client.get(url, format="json")
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response_json, [])

    def test_products_retrieve(self):
        url = reverse("products_RUD", args=[1])
        response = self.client.get(url, format="json")
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response_json, "[]")
        self.assertEqual(response_json["pr_name"], "testname")
        self.assertEqual(float(response_json["pr_cost"]), 1000)
        self.assertEqual(response_json["pr_amount"], 4)
        self.assertEqual(response_json["pr_description"], "Test description")
        self.assertEqual(response_json["pr_date"], "2023-01-03T00:00:00Z")

    def test_products_create(self):
        url = reverse("products_list_create")
        data = {
            "pr_name": "testname 3",
            "pr_cost": 3000.00,
            "pr_amount": 3,
            "pr_description": "Test description 3",
            "pr_date": "2023-01-04"
        }
        response = self.client.post(url, data=data)
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(response_json, "[]")
        self.assertEqual(response_json["pr_name"], "testname 3")
        self.assertEqual(float(response_json["pr_cost"]), 3000)
        self.assertEqual(response_json["pr_amount"], 3)
        self.assertEqual(response_json["pr_description"], "Test description 3")

    def test_products_retrieve_update(self):
        url = reverse("products_RUD", args=[1])
        new_data = {
            "pr_name": "New Name",
            "pr_cost": 2450.00,
            "pr_amount": 9,
            "pr_description": "New description",
            # "pr_date": "2023-01-06"
        }
        response = self.client.put(url, data=new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse("products_RUD", args=[1])
        response = self.client.get(url, format="json")
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response_json, "[]")
        self.assertEqual(response_json["pr_name"], "New Name")
        self.assertEqual(float(response_json["pr_cost"]), 2450)
        self.assertEqual(response_json["pr_amount"], 9)
        self.assertEqual(response_json["pr_description"], "New description")
        # self.assertEqual(response_json["pr_date"], "2023-01-06")

    def test_products_delete(self):
        url = reverse("products_RUD", args=[1])
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=1)
