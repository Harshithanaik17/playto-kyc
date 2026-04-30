from .models import User

def get_user(request):
    user_id = request.headers.get("user_id")

    if not user_id:
        return User.objects.first()   # fallback

    return User.objects.get(id=user_id)