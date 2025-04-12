from customers.models import Customer
from django.http import JsonResponse
from customers.serializers import customerSerializer
def customers(request): 
   data = Customer.objects.all()
   serializer=customerSerializer(data, many=True)
   return JsonResponse(serializer.data)

