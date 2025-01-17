from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection


def theme_list(request):
    return render(request, 'theme_entertainment/list.html')


def theme_create(request):
    return render(request, 'theme_entertainment/create.html')


def activity_management(request):
    return render(request, 'theme_entertainment/activity_management.html')


def get_event_detail(request, event_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    uid,
                    activity_name as title,
                    description,
                    organizer,
                    location,
                    start_date as startDate,
                    end_date as endDate,
                    address,
                    image_url as imageUrl,
                    related_link as url
                FROM events
                WHERE uid = %s
            """, [event_id])

            columns = [col[0] for col in cursor.description]
            row = cursor.fetchone()

            if row:
                event = dict(zip(columns, row))
                return JsonResponse(event)
            else:
                return JsonResponse({'error': '找不到該活動'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_events(request):
    try:
        with connection.cursor() as cursor:
            # 查詢所有活動資料
            cursor.execute("""
                SELECT
                    uid,
                    activity_name as title,
                    description,
                    organizer,
                    location,
                    start_date as startDate,
                    end_date as endDate,
                    address,
                    image_url as imageUrl,
                    related_link as url
                FROM events
                WHERE image_url IS NOT NULL AND image_url != ''
                ORDER BY start_date DESC
            """)

            # 獲取列名
            columns = [col[0] for col in cursor.description]

            # 將查詢結果轉換為字典列表
            events = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

            return JsonResponse(events, safe=False)

    except Exception as e:
        return JsonResponse(
            {'error': str(e)},
            status=500
        )
