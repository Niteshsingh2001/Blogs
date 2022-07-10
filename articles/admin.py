from django.contrib import admin

from .models import Article
# Register your models here.
class article_text(admin.ModelAdmin):

    list_display =  ['id','tittle','content']
    search_fields = ['tittle']
    


admin.site.register(Article,article_text)