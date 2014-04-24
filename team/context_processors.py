from django.conf import settings


def user(request):
    """
    Returns context variables for the user
    """
    if hasattr(request,'user'):
        user = request.user
    else:
        user = None

    return {
        'user': user,
    }
