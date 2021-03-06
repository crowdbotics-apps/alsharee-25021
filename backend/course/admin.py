from django.contrib import admin
from .models import (
    Category,
    Course,
    Enrollment,
    Event,
    Group,
    Module,
    Recording,
    Subscription,
    SubscriptionType,
)

admin.site.register(Course)
admin.site.register(Subscription)
admin.site.register(SubscriptionType)
admin.site.register(Recording)
admin.site.register(Category)
admin.site.register(Group)
admin.site.register(Event)
admin.site.register(Enrollment)
admin.site.register(Module)

# Register your models here.
