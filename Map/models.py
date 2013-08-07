from django.contrib.gis.db import models


# Create your models here.
class Address(models.Model):
    Address_ID = models.AutoField(primary_key=True, verbose_name='Address ID')
    Historic_Address = models.CharField(max_length=50)
    Modern_Address = models.CharField(max_length=50)
    Area = models.CharField()
    Longitude = models.FloatField(null=True)
    Latitude = models.FloatField(null=True)


    mpoly = models.PointField(srid=4326)
    objects = models.GeoManager()


    def __unicode__(self):
        return self.Historic_Address


class Occupant_1861(models.Model):

    Occupant_ID = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=30)
    Surname = models.CharField(max_length=50)
    Occupation = models.CharField(max_length=100)
    Birth_Place = models.CharField(max_length=100)
    Birth_Country = models.CharField(max_length=100)
    Age = models.IntegerField()
    Marital_Status = models.CharField(max_length=20)
    Household_Status = models.CharField(max_length=20)
    Address_ID = models.ForeignKey(Address)

    #def __unicode__(self):
     #   return '%s %s %s %s' % (self.Occupant_ID, self.First_Name, self.Surname, self.Occupation)

#Table of 1881 census occupants
class Occupant_1881(models.Model):

    Occupant_ID = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=30)
    Surname = models.CharField(max_length=50)
    Occupation = models.CharField(max_length=100)
    Birth_Place = models.CharField(max_length=100)
    Birth_Country = models.CharField(max_length=100)
    Age = models.IntegerField()
    Marital_Status = models.CharField(max_length=20)
    Household_Status = models.CharField(max_length=20)
    Address_ID = models.ForeignKey(Address)

    #def __unicode__(self):
    #    return '%s %s %s %s' % (self.Occupant_ID, self.First_Name, self.Surname, self.Occupation)

#Table of 1911 census occupants
class Occupant_1911(models.Model):

    Occupant_ID = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=30)
    Surname = models.CharField(max_length=50)
    Occupation = models.CharField(max_length=100)
    Birth_Place = models.CharField(max_length=100)
    Birth_Country = models.CharField(max_length=100)
    Age = models.IntegerField()
    Marital_Status = models.CharField(max_length=20)
    Household_Status = models.CharField(max_length=20)
    Address_ID = models.ForeignKey(Address)
