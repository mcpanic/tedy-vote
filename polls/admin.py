from django.contrib import admin
from polls.models import Poll
from polls.models import Choice
from polls.models import Voter

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Voter)
