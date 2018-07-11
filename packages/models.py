from django.db import models


class Author(models.Model):
    """ Author of a package """
    name = models.CharField(max_length=50)
    contact = models.EmailField()


class Package(models.Model):
    """ Represent a software package """
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=200)
    website = models.URLField()
    authors = models.ManyToManyField(Author)


class Alias(models.Model):
    """ One package can be know with it's aliases """
    name = models.CharField(max_length=25)
    package_id = models.ForeignKey(Package, on_delete=models.CASCADE)


class Version(models.Model):
    """ Each package must have one version """
    name = models.CharField(max_length=25)
    url = models.URLField()
    checksum = models.CharField(max_length=255)
    os = models.CharField(max_length=10)
    arch = models.CharField(max_length=10)
    package_id = models.ForeignKey(Package, on_delete=models.CASCADE)
