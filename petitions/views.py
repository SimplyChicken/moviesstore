from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Petition, PetitionLike
from django.contrib.auth.decorators import login_required

def index(request):
    template_data = {'title': 'Movies Store'}
    petitions = Petition.objects.all().order_by('-id')
    liked_petition_ids = set()
    if request.user.is_authenticated:
        liked_petition_ids = set(
            PetitionLike.objects.filter(user=request.user).values_list('petition_id', flat=True)
        )
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name and description:
            Petition.create_petition(name=name, description=description)
            return redirect('petitions.index')
    return render(request, 'petitions/index.html', {
        'template_data': template_data,
        'petitions': petitions,
        'liked_petition_ids': liked_petition_ids,
    })

@csrf_exempt
@login_required
def like_petition(request):
    if request.method == 'POST':
        petition_id = request.POST.get('petition_id')
        user = request.user
        try:
            petition = Petition.objects.get(id=petition_id)
            already_liked = PetitionLike.objects.filter(user=user, petition=petition).exists()
            if not already_liked:
                PetitionLike.objects.create(user=user, petition=petition)
                petition.upvotes += 1
                petition.save()
                return JsonResponse({'success': True, 'upvotes': petition.upvotes})
            else:
                return JsonResponse({'success': False, 'upvotes': petition.upvotes, 'error': 'Already liked'})
        except Petition.DoesNotExist:
            return JsonResponse({'success': False})
    return JsonResponse({'success': False})

