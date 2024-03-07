from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .serializers import ConnectionSerializer, SuggestedUserSerializer
from .models import Connection

# Create your views here.
class SendConnectionApi(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ConnectionSerializer
    queryset = Connection.objects

    def post(self, request):
        serializer = self.serializer_class(data = {'from_user':request.user.id, 'to_user': request.data.get('to_user'), 'status' : 'pending'})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class AcceptConnectionApi(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ConnectionSerializer
    queryset = Connection.objects

    def post(self, request):
        if not request.data.get('from_user'):
            return Response("Required : from_user")
        try:
            instance = self.queryset.get(from_user = request.data.get('from_user'), to_user = request.user.id)
            instance.status = 'accepted'
            instance.save()
            return Response("Connection Accepted")
        except:
            return Response("No Connection Request")

class DeclineConnectionApi(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ConnectionSerializer
    queryset = Connection.objects

    def post(self, request):
        if not request.data.get('from_user'):
            return Response("Required : from_user")
        try:
            instance = self.queryset.get(from_user = request.data.get('from_user'), to_user = request.user.id)
            instance.status = 'declined'
            instance.save()
            return Response("Connection Declined")
        except:
            return Response("No Connection Request")

class ListConnectionRequestApi(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ConnectionSerializer
    queryset = Connection.objects

    def get(self, request):
        serializer = self.serializer_class(self.queryset.filter(to_user = request.user.id, status = 'pending'), many=True)
        return Response(serializer.data)
    
class GetConnectionSuggestion(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        userConnection = []
        userConnection += [connection.from_user for connection in Connection.objects.filter(to_user = user, status = 'accepted')]
        userConnection += [connection.to_user for connection in Connection.objects.filter(from_user = user, status = 'accepted')]
        connection_suggestion = set()
        for userConnection in userConnection:
            connection_suggestion.update([connection.from_user for connection in Connection.objects.filter(to_user = userConnection, status = 'accepted')])
            connection_suggestion.update([connection.to_user for connection in Connection.objects.filter(from_user = userConnection, status = 'accepted')])
        
        connection_suggestion.remove(user)
        serializer = SuggestedUserSerializer(connection_suggestion, many = True)
        return Response(serializer.data)