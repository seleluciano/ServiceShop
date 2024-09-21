from .models import Avatar

def avatar_processor(request):
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user).first()
    else:
        avatar = None
    return {'imagen': avatar}
