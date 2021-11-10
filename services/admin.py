from django.contrib import admin
from .models import AssignmentWritingService, ProofReadingService, DissertationAndThesisHelp, ContentWritingService
# Register your models here.

admin.site.register(AssignmentWritingService)
admin.site.register(ProofReadingService)
admin.site.register(DissertationAndThesisHelp)
admin.site.register(ContentWritingService)
