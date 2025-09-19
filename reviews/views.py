from django.shortcuts import render
from .models import Review
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.

def reviews_list(request):
    reviews = Review.objects.order_by('-created_at')
    return render(request, 'reviews_list.html', {'reviews': reviews})

def submit_review(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip() or 'Anonymous'
        comment = request.POST.get('comment', '').strip()
        if comment:
            Review.objects.create(name=name, comment=comment)
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})
