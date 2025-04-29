# Mohi (w1972510)
from django.contrib import admin
from .models import SessionAssignment, Session, Card, Vote

admin.site.register(SessionAssignment)
admin.site.register(Session)
admin.site.register(Card)
admin.site.register(Vote)
