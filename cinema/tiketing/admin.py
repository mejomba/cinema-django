from django.contrib import admin
from tiketing.models import Movie, Cinema, Sanse


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'director', 'length', 'year', 'poster']


admin.site.register(Movie, MovieAdmin)


class CinemaAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'capacity', 'phone', 'address', 'image', 'cinema_code']


admin.site.register(Cinema, CinemaAdmin)


class SanseAdmin(admin.ModelAdmin):
    list_display = ['movie', 'cinema', 'start_time', 'price', 'salable_seats', 'free_seat', 'id']


admin.site.register(Sanse, SanseAdmin)