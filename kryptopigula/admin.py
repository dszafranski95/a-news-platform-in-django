from django.contrib import admin
from django.db import models  # Import models from django
from .models import Editorial, CryptoAnalysis, PressRelease, News
from ckeditor.widgets import CKEditorWidget  # Import from ckeditor

class EditorialAdmin(admin.ModelAdmin):  # Use the regular ModelAdmin
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

class PressReleaseAdmin(admin.ModelAdmin):  # Use the regular ModelAdmin
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }
    
class NewsAdmin(admin.ModelAdmin):  
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }


admin.site.register(News, NewsAdmin)
admin.site.register(Editorial, EditorialAdmin)
admin.site.register(CryptoAnalysis)
admin.site.register(PressRelease, PressReleaseAdmin)
