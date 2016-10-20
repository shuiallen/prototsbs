from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Panel
from .models import Participant
from .models import PanelStitchingRecord
from .models import ImportData
from .models import UploadData


admin.site.register(Panel)
admin.site.register(PanelStitchingRecord)
admin.site.register(Participant)
admin.site.register(ImportData)
admin.site.register(UploadData)