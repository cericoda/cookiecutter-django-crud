from django.contrib import admin
from import_export.admin import ImportExportMixin, ImportExportModelAdmin
from import_export import resources
import reversion
from .models import {{ cookiecutter.model_name }}


class IEAdmin(reversion.VersionAdmin, ImportExportModelAdmin):    
    pass

admin.site.register({{ cookiecutter.model_name }}, IEAdmin)


