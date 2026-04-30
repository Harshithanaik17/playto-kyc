from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from .state_machine import change_state
from .utils import get_user
from django.utils.timezone import now
from datetime import timedelta

class KYCView(APIView):

    def get(self, request):
        user = get_user(request)

        if user.role == 'merchant':
            data = KYCSubmission.objects.filter(user=user)
        else:
            data = KYCSubmission.objects.all()

        serializer = KYCSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KYCSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ChangeStateView(APIView):
    def post(self, request, id):
        submission = KYCSubmission.objects.get(id=id)

        try:
            change_state(submission, request.data['state'])

            Notification.objects.create(
                user=submission.user,
                event_type="STATE_CHANGED",
                payload={"state": submission.state}
            )

            return Response({"msg": "updated"})
        except Exception as e:
            return Response({"error": str(e)}, status=400)


class QueueView(APIView):
    def get(self, request):
        submissions = KYCSubmission.objects.filter(state='submitted').order_by('created_at')

        result = []
        for s in submissions:
            at_risk = (now() - s.created_at) > timedelta(hours=24)

            result.append({
                "id": s.id,
                "name": s.name,
                "at_risk": at_risk
            })

        return Response(result)