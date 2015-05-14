from django.contrib import admin

from .models import QQAccount, Activity
# Register your models here.

class QQAccountAdmin(admin.ModelAdmin):
	fields = ['qq', 'nick_name', 'gender', 'balance', 'club_level', 'activity_times', 'accumulate_points', 'card', 'comments', 'other_comments', 'weixin_id']
	list_display =('qq', 'nick_name', 'gender', 'balance', 'club_level', 'activity_times', 'accumulate_points', 'card', 'comments', 'other_comments', 'weixin_id')
	list_filter = ['qq']
	search_fields = ['qq','nick_name']
    
class ActivityAdmin(admin.ModelAdmin):
	fields = ['title', 'discription', 'activity_position', 'start_time', 'stop_time', 'cost_male', 'cost_female', 'max_participants', 'dead_line', 'organiser', 'organiser_phone']
	list_display =('title', 'discription', 'activity_position', 'start_time', 'stop_time', 'cost_male', 'cost_female', 'max_participants', 'dead_line', 'organiser', 'organiser_phone')


admin.site.register(QQAccount, QQAccountAdmin)
admin.site.register(Activity, ActivityAdmin)
