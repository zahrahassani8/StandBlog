from blog.models import *

def health_tips(request):
    tips = Tip.objects.order_by('-created')
    return{"tips":tips}