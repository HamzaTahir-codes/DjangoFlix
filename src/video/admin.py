from django.contrib import admin
from .models import Video, VideoProxy

class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'video_id', 'is_published']
    search_fields = ['title']
    list_filter = ['active']
    readonly_fields = ['id','is_published']
    class Meta:
        model = Video

class VideoProxyAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id']
    search_fields = ['title']
    class Meta:
        model = VideoProxy

    def get_queryset(self, request):
        return VideoProxy.objects.filter(active=True)

admin.site.register(Video, VideoAdmin)
admin.site.register(VideoProxy, VideoProxyAdmin)
