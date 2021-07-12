# from django.shortcuts import render
# from rest_framework import response

# # Create your views here.
# from .serializers import SeatsReservedSerializer, ReservationSerializer
# from rest_framework import viewsets, mixins, permissions, status
# from rest_framework.response import Response
# from .models import SeatsReserved
# from drf_yasg.utils import swagger_auto_schema


# class SeatReservedViewset(viewsets.ViewSet):

#     serializer_class = SeatsReservedSerializer

#     def get_seats_reserved(self, request, show_id):
              
#         if not show_id:
#             return Response({"Message": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

#         try:
            
#             queryset = SeatsReserved.objects.filter(show_time_id = show_id)
#             serialized = SeatsReservedSerializer(queryset, many=True)
        
#         except:
#             return Response({"Message": "serializer error"}, status=status.HTTP_409_CONFLICT)

#         return Response(data=serialized.data, status=status.HTTP_200_OK)

#     def patch_seats_reserved(self, request, **kwargs):
              
#         try:
#             seats_reserved_ids = request.data['seats_reserved_ids']
#         except:
#             return Response({'Message': 'bad request'}, status=status.HTTP_400_BAD_REQUEST)
        
#         try:
#             queryset = SeatsReserved.objects.filter(pk__in = seats_reserved_ids)
#             queryset.payment_processing = True

#         except:
#             return Response({"Message": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        
#         serialized = SeatsReservedSerializer(queryset, many=True)

#         return Response(data=serialized.data, status=status.HTTP_200_OK)

#     # def patch_seats_booked(self, request, **kwargs):

#     #     try:
#     #         seat_booking_id = request.data['seat_booking_id']
        
#     #     except:
#     #         return Response({'Message': 'bad request'}, status=status.HTTP_400_BAD_REQUEST)

#     #     try:
#     #         queryset = SeatsReserved.objects
    
#     # def patch_seats_booked(self, request, **kwargs):

#     #     try:

        
#         # except:
#         #     return Response({'Message': 'id does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
# class ReservationViewSet(viewsets.ViewSet):

#     @swagger_auto_schema(request_body=ReservationSerializer, responses={200: ReservationSerializer})
#     def post_reservation(self, request, **kwargs):
    
#         serialized = ReservationSerializer(data=request.data)

#         if serialized.is_valid():
#             serialized.save()
#             return Response(data=serialized.data, status=status.HTTP_200_OK)

#         return Response(data=serialized.error_messages, status=status.HTTP_400_BAD_REQUEST)        
            
        