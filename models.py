from django.db import models
from django.utils import timezone


class BaseEvent(models.Model):
    """活動基礎模型"""
    title = models.CharField('活動名稱', max_length=255)
    description = models.TextField('活動描述', blank=True)
    start_date = models.DateTimeField('開始時間', null=True, blank=True)
    end_date = models.DateTimeField('結束時間', null=True, blank=True)
    location = models.CharField('地點', max_length=255, blank=True)
    image_url = models.URLField('圖片網址', max_length=500, blank=True)
    source_url = models.URLField('活動來源網址', max_length=500, blank=True)
    created_at = models.DateTimeField('建立時間', default=timezone.now)
    updated_at = models.DateTimeField('更新時間', auto_now=True)

    class Meta:
        abstract = True


class TaipeiEvent(BaseEvent):
    """台北市政府網站整合平台之熱門活動"""
    category = models.CharField('活動分類', max_length=100, blank=True)
    district = models.CharField('行政區', max_length=50, blank=True)
    organizer = models.CharField('主辦單位', max_length=255, blank=True)
    price = models.CharField('票價資訊', max_length=255, blank=True)
    source = models.CharField('資料來源', max_length=50, default='taipei_city')

    class Meta:
        verbose_name = '台北市熱門活動'
        verbose_name_plural = '台北市熱門活動'


class NewTaipeiEvent(BaseEvent):
    """新北市政府近期活動"""
    category = models.CharField('活動分類', max_length=100, blank=True)
    district = models.CharField('行政區', max_length=50, blank=True)
    organizer = models.CharField('主辦單位', max_length=255, blank=True)
    source = models.CharField('資料來源', max_length=50, default='new_taipei_city')

    class Meta:
        verbose_name = '新北市文化活動'
        verbose_name_plural = '新北市文化活動'


class TaiwanCulturalEvent(BaseEvent):
    """文化部整合全國綜藝、藝文活動"""
    category = models.CharField('活動分類', max_length=100, blank=True)
    city = models.CharField('城市', max_length=50, blank=True)
    district = models.CharField('地區', max_length=50, blank=True)
    organizer = models.CharField('主辦單位', max_length=255, blank=True)
    source = models.CharField('資料來源', max_length=50, default='culture_taiwan')

    class Meta:
        verbose_name = '全國綜藝藝文活動'
        verbose_name_plural = '全國綜藝藝文活動'


class TFAMEvent(BaseEvent):
    """台北市立美術館展覽"""
    exhibition_type = models.CharField('展覽類型', max_length=100, blank=True)
    artist = models.CharField('藝術家', max_length=255, blank=True)
    admission = models.CharField('入場資訊', max_length=255, blank=True)
    source = models.CharField('資料來源', max_length=50, default='tfam')

    class Meta:
        verbose_name = '北美館展覽'
        verbose_name_plural = '北美館展覽'


class Event(models.Model):
    uid = models.CharField(max_length=100, primary_key=True)
    activity_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    organizer = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    address = models.CharField(max_length=200)
    image_url = models.URLField(null=True, blank=True)
    related_link = models.URLField(null=True, blank=True)

    class Meta:
        db_table = 'events'
        verbose_name = '活動'
        verbose_name_plural = '活動列表'

    def __str__(self):
        return self.activity_name
