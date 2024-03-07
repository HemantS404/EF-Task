from django.urls import path

from .views import ListConnectionRequestApi, DeclineConnectionApi, AcceptConnectionApi, SendConnectionApi, GetConnectionSuggestion

urlpatterns = [
    path('SendConnection/', SendConnectionApi.as_view(), name="send_connection"),
    path('AcceptConnection/', AcceptConnectionApi.as_view(), name="accept_connection"),
    path('DeclineConnection/', DeclineConnectionApi.as_view(), name="decline_connection"),
    path('ListConnectionRequest/', ListConnectionRequestApi.as_view(), name="list_connection_request"),
    path('GetConnectionSuggestion/', GetConnectionSuggestion.as_view(), name="get_connection_suggestion"),
]