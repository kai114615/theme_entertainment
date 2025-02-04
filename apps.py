from django.apps import AppConfig


class ThemeEntertainmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'theme_entertainment'
    verbose_name = '主題育樂'

    # def ready(self):
    #     # 避免在開發環境中重複執行
    #     import os
    #     if os.environ.get('RUN_MAIN', None) != 'true':
    #         # 導入資料下載模組
    #         from . import main
    #         # 執行下載功能
    #         main.download_all_data()
