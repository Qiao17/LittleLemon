from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest (TestCase):
    def setUp(self):
        Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        Menu.objects.create(Title="HotDog", Price=90, Inventory=80)
        
    def test_getall(self):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        