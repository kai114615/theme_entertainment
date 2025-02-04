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


class Events(models.Model):
    """整合性活動資訊模型"""
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField('唯一識別碼', max_length=100, unique=True, db_index=True)
    activity_name = models.TextField('活動名稱')
    description = models.TextField('活動描述', null=True, blank=True)
    organizer = models.CharField('主辦單位', max_length=200, null=True, blank=True)
    address = models.TextField('地址', null=True, blank=True)
    start_date = models.DateField('開始日期', null=True, blank=True)
    end_date = models.DateField('結束日期', null=True, blank=True)
    location = models.CharField('地點', max_length=200, null=True, blank=True)
    latitude = models.DecimalField(
        '緯度', max_digits=12, decimal_places=8, null=True, blank=True)
    longitude = models.DecimalField(
        '經度', max_digits=12, decimal_places=8, null=True, blank=True)
    ticket_price = models.TextField('票價資訊', null=True, blank=True)
    related_link = models.TextField('相關連結', null=True, blank=True)
    image_url = models.TextField('圖片網址', null=True, blank=True)
    created_at = models.DateTimeField('建立時間', auto_now_add=True)

    class Meta:
        db_table = 'events'
        verbose_name = '活動資訊'
        verbose_name_plural = '活動資訊列表'
        indexes = [
            models.Index(fields=['start_date', 'end_date']),
            models.Index(fields=['location']),
        ]

    def __str__(self):
        return self.activity_name


class ImportDates(models.Model):
    """資料匯入時間紀錄"""
    id = models.BigAutoField(primary_key=True)
    import_date = models.DateTimeField('匯入時間')
    timezone_type = models.IntegerField('時區類型')
    timezone = models.CharField('時區', max_length=50)

    class Meta:
        db_table = 'import_dates'
        verbose_name = '匯入紀錄'
        verbose_name_plural = '匯入紀錄列表'

    def __str__(self):
        return f'{self.import_date} ({self.timezone})'


class QueryResults(models.Model):
    """查詢結果紀錄"""
    id = models.BigAutoField(primary_key=True)
    query_timestamp = models.CharField('查詢時間戳記', max_length=50)
    limit_count = models.IntegerField('限制筆數')
    offset_count = models.IntegerField('位移筆數')
    total_count = models.IntegerField('總筆數')
    sort_order = models.CharField('排序方式', max_length=50, null=True, blank=True)
    created_at = models.DateTimeField('建立時間', auto_now_add=True)
    events = models.ManyToManyField(
        Events,
        through='QueryEventRelations',
        through_fields=('query_id', 'event_id'),
        verbose_name='相關活動'
    )

    class Meta:
        db_table = 'query_results'
        verbose_name = '查詢結果'
        verbose_name_plural = '查詢結果列表'

    def __str__(self):
        return f'查詢 {self.query_timestamp} (共 {self.total_count} 筆)'


class QueryEventRelations(models.Model):
    """查詢結果與活動的關聯"""
    query_id = models.ForeignKey(
        QueryResults,
        on_delete=models.CASCADE,
        db_column='query_id',
        verbose_name='查詢ID'
    )
    event_id = models.ForeignKey(
        Events,
        on_delete=models.CASCADE,
        db_column='event_id',
        verbose_name='活動ID'
    )
    display_order = models.IntegerField('顯示順序')

    class Meta:
        db_table = 'query_event_relations'
        unique_together = (('query_id', 'event_id'),)
        verbose_name = '查詢活動關聯'
        verbose_name_plural = '查詢活動關聯列表'

    def __str__(self):
        return f'{self.query_id} - {self.event_id} ({self.display_order})'


class Entertainment(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name='活動名稱')
    description = models.TextField(verbose_name='活動描述', null=True, blank=True)
    location = models.CharField(
        max_length=255, verbose_name='地點', null=True, blank=True)
    start_date = models.DateField(verbose_name='開始日期', null=True, blank=True)
    end_date = models.DateField(verbose_name='結束日期', null=True, blank=True)
    organizer = models.CharField(
        max_length=255, verbose_name='主辦單位', null=True, blank=True)
    website = models.URLField(verbose_name='活動網站', null=True, blank=True)
    image_url = models.URLField(verbose_name='圖片網址', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='建立時間')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新時間')
    source = models.CharField(
        max_length=50, verbose_name='資料來源', null=True, blank=True)

    class Meta:
        db_table = 'entertainment'
        verbose_name = '活動資訊'
        verbose_name_plural = '活動資訊'

    def __str__(self):
        return self.title
