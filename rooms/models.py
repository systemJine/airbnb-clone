from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ Roomtype Model Definitsion """

    pass


class Amenity(AbstractItem):
    """ Amenity Model Definitsion """

    pass


class Facility(AbstractItem):
    """ Facility Model Definitsion """

    pass


class HouseRule(AbstractItem):
    """ Hodw Model Definitsion """

    pass


class Room(core_models.TimeStampModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guest = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity)
    facilities = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)

    def __str__(self):
        return self.name
