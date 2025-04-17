from django.shortcuts import render
from .llmres import analyze_text
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import QueryLog
from .serializers import QueryLogSerializer
from .actions import suggest_actions


class Analyze(APIView):
    def post(self,request):
        query=request.data.get("query")
        if query:
            analysis=analyze_text(query)
            tone=analysis.get("tone","unknown")
            intent=analysis.get("intent","unknown")
            suggestions=suggest_actions(intent)

            query_log=QueryLog.objects.create(
                query=query,
                    tone=tone,
                    intent=intent,
                    actions=suggestions 
            )
            query_log_serializer = QueryLogSerializer(query_log)
            return Response(query_log_serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Query is required."}, status=status.HTTP_400_BAD_REQUEST)



