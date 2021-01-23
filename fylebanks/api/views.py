from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from api.models import Branch
from api.serializers import BranchSerializer


class BranchesView(views.APIView):

    def get(self, request):
        query = request.query_params.get('q')
        limit = request.query_params.get('limit')
        offset = request.query_params.get('offset')

        if not (query and limit and offset):
            return Response({'error': 'query or limit or offset not provided'}, status=status.HTTP_400_BAD_REQUEST)

        limit = int(limit)
        offset = int(offset)
        
        queryset = Branch.objects.filter(Q(ifsc__icontains=query) |
                                         Q(branch__icontains=query) |
                                         Q(address__icontains=query) |
                                         Q(city__icontains=query) |
                                         Q(district__icontains=query) |
                                         Q(state__icontains=query)).order_by('ifsc')[offset:offset+limit]
        serializer = BranchSerializer(queryset, many=True)
        return Response({"branches":serializer.data}, status=status.HTTP_200_OK)


class BranchesAutocompleteView(views.APIView):
    
    def get(self, request):
        query = request.query_params.get('q')
        limit = request.query_params.get('limit')
        offset = request.query_params.get('offset')

        if not (query and limit and offset):
            return Response({'error': 'query or limit or offset not provided'}, status=status.HTTP_400_BAD_REQUEST)

        limit = int(limit)
        offset = int(offset)
        
        queryset = Branch.objects.filter(branch__icontains=query).order_by('ifsc')[offset:offset+limit]
        serializer = BranchSerializer(queryset, many=True)
        return Response({"branches":serializer.data}, status=status.HTTP_200_OK)
