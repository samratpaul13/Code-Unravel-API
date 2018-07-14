from django.contrib import admin
from . import models


admin.site.register(models.USER)
admin.site.register(models.APP_SETTING)
admin.site.register(models.CANDIDATE_PROFILE)
admin.site.register(models.CHALLENGE_QUESTION)
admin.site.register(models.LANGUAGE)
admin.site.register(models.PERMISSION)
admin.site.register(models.RESULT)
admin.site.register(models.ROLE)
admin.site.register(models.ROLE_PERMISSION)
admin.site.register(models.TASK_ASSIGN)

