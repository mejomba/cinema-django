from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    director = models.CharField(max_length=50, verbose_name='کارگردان')
    year = models.IntegerField(verbose_name='سال تولید')
    length = models.IntegerField(verbose_name='زمان فیلم')
    descreption = models.TextField(verbose_name='توضیحات')
    poster = models.ImageField(verbose_name='پوستر', upload_to='movie_poster/')

    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم'

    def __str__(self):
        return self.name
    

class Cinema(models.Model):
    cinema_code = models.IntegerField(primary_key=True, verbose_name ='کد سینما')
    name = models.CharField(max_length=50, verbose_name ='نام')
    city = models.CharField(max_length=30, default='تهران', verbose_name ='شهر')
    capacity = models.IntegerField(verbose_name ='ظرفیت')
    phone = models.CharField(max_length=20, null=True, verbose_name ='تلفن')
    address = models.TextField(verbose_name ='آدرس')
    image = models.ImageField(verbose_name='تصویر', upload_to='cinema_image/')

    class Meta:
        verbose_name = 'سینما'
        verbose_name_plural = 'سینما'
        
    def __str__(self):
        return self.name


# TODO VALIDATOR >>> Sanse.salable_seat and Sanse.free_seat must be lower than or equal to Cinama.capacity
class Sanse(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, verbose_name ='فیلم')
    cinema = models.ForeignKey(Cinema, on_delete=models.PROTECT, verbose_name ='سینما')

    start_time = models.DateTimeField(verbose_name ='زمان شروع')
    price = models.IntegerField(verbose_name ='قیمت')
    salable_seats = models.IntegerField(verbose_name ='صندلی های قابل فروش')
    free_seat = models.IntegerField(verbose_name ='صندلی های خالی')

    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKETS_SOLD = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CALCELED = 6
    status_choices = (
        (SALE_NOT_STARTED, "فروش آغاز نشده"),
        (SALE_OPEN, "در حال بلیت فروشی"),
        (TICKETS_SOLD, "بلیت تمام شد"),
        (SALE_CLOSED, "پایان فروش"),
        (MOVIE_PLAYED, "فیلم پخش شد"),
        (SHOW_CALCELED, "نمایش لغو شد")
    )
    status = models.IntegerField(choices=status_choices, verbose_name ='وضعیت')

    class Meta:
        verbose_name = 'سانس'
        verbose_name_plural = 'سانس'

    def __str__(self):
        return '{} - {} - {}'.format(self.movie, self.cinema, self.start_time)
