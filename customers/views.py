from customers.models import Customer
from django.http import JsonResponse
from customers.serializers import customerSerializer

def customers(request):
   data = Customer.objects.all()
   serializer = customerSerializer(data, many=True)
   # Modifier la structure des données ici
   response_data = {"customers": serializer.data}
   return JsonResponse(response_data)

def customer(request, id):
   data = Customer.objects.get(pk=id)
   serializer = customerSerializer(data)
   # Modifier la structure des données ici
   response_data = {"customer": serializer.data}
   return JsonResponse(response_data)