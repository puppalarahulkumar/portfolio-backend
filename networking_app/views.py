from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import NetworkingUserModel
from django.db.models import Q


@method_decorator(csrf_exempt, name="dispatch")
class NetworkingUserView(View):

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)

            user = NetworkingUserModel.objects.create(
                name=data.get("name"),
                phone=data.get("phone"),
                linkedin_url=data.get("linkedin_url"),
                other_url=data.get("other_url"),
                notes=data.get("notes"),
                designation=data.get("designation"),
                location_name=data.get("location_name"),
                latitude=data.get("latitude"),
                longitude=data.get("longitude"),
            )

            return JsonResponse(
                {"message": "User saved successfully!", "id": user.id},
                status=201
            )

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def get(self, request, *args, **kwargs):
        """Fetch all saved networking users"""
        search_query = request.GET.get("search", "").strip()

        if search_query:
            users = NetworkingUserModel.objects.filter(
                Q(name__icontains=search_query) |
                Q(designation__icontains=search_query) |
                Q(location_name__icontains=search_query) |
                Q(notes__icontains=search_query)
            ).order_by("-created_at")
        else:
            users = NetworkingUserModel.objects.all().order_by("-created_at")
        data = [
            {
                "id": user.id,
                "name": user.name,
                "phone": user.phone,
                "linkedin_url": user.linkedin_url,
                "other_url": user.other_url,
                "notes": user.notes,
                "designation": user.designation,
                "location_name": user.location_name,
                "latitude": float(user.latitude) if user.latitude else None,
                "longitude": float(user.longitude) if user.longitude else None,
                "created_at": user.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            }
            for user in users
        ]
        return JsonResponse(data, safe=False, status=200)
