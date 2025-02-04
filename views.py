from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.db.models import F
from theme_entertainment.models import Events


def theme_list(request):
    return render(request, 'theme_entertainment/list.html')


def theme_create(request):
    return render(request, 'theme_entertainment/create.html')


def activity_management(request):
    return render(request, 'theme_entertainment/activity_management.html')


def get_event_detail(request, event_id):
    try:
        event = Events.objects.filter(uid=event_id).values(
            'uid',
            'description',
            'organizer',
            'location',
            'address',
            title=F('activity_name'),
            startDate=F('start_date'),
            endDate=F('end_date'),
            imageUrl=F('image_url'),
            url=F('related_link')
        ).first()

        if event:
            return JsonResponse(event)
        return JsonResponse({'error': '找不到該活動'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_events(request):
    try:
        events = Events.objects.all().values(
            'uid',
            'description',
            'organizer',
            'location',
            'address',
            title=F('activity_name'),
            startDate=F('start_date'),
            endDate=F('end_date'),
            imageUrl=F('image_url'),
            url=F('related_link')
        )
        return JsonResponse(list(events), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
