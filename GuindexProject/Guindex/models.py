import logging

from django.db import models

from GuindexParameters import GuindexParameters

from UserProfile.models import UserProfile

logger = logging.getLogger(__name__)


class Pub(models.Model):

    creator         = models.ForeignKey(UserProfile)
    creationDate    = models.DateTimeField(auto_now_add = True)
    name            = models.CharField(max_length = GuindexParameters.MAX_PUB_NAME_LEN, default = "", unique = True)
    longitude       = models.DecimalField(decimal_places = 7, max_digits = 12, default = 0.0)
    latitude        = models.DecimalField(decimal_places = 7, max_digits = 12, default = 0.0)
    mapLink         = models.TextField(default = "")
    closed          = models.BooleanField(default = False)
    servingGuinness = models.BooleanField(default = True)

    def __unicode__(self):

        return "'%s(%d)'" % (self.name, self.id)

    def getGuini(self, newestFirst):
        """
            Returns list of Guinness objects belonging to this pub
            sorted by creation date
        """
        guini_list = []

        guini = Guinness.objects.filter(pub = self)

        for guin in guini:

            guin_dict = {}

            guin_dict['id']           = str(guin.id)
            guin_dict['creator']      = guin.creator.user.username
            guin_dict['creationDate'] = guin.creationDate
            guin_dict['price']        = guin.price

            guini_list.append(guin_dict.copy())

        return sorted(guini_list, key = lambda k: k['creationDate'], reverse = newestFirst)

    def getFirstVerifiedGuinness(self):
        """
            Return most recently verified Guinness object.
        """

        guini = self.getGuini(True)

        return guini[0] if len(guini) else None

    def getLastVerifiedGuinness(self):
        """
            Return most recently verified Guinness object.
        """

        guini = self.getGuini(False)

        return guini[0] if len(guini) else None


class Guinness(models.Model):

    creator      = models.ForeignKey(UserProfile)
    creationDate = models.DateTimeField(auto_now_add = True)
    price        = models.DecimalField(decimal_places = 2, max_digits = 6)
    pub          = models.ForeignKey(Pub)

    def __unicode__(self):

        return "'%s(%d) - Price: %f'" % (self.pub, self.id, self.price)


class StatisticsSingleton(models.Model):
    """
        This is a singleton class to store statistics.
        Statistics are calculated in the background and wriiten to this singleton
    """

    cheapestPub       = models.ForeignKey(Pub)
    dearestPub        = models.ForeignKey(Pub)
    averagePrice      = models.DecimalField(decimal_places = 2, max_digits = 6)
    standardDevation  = models.DecimalField(decimal_places = 3, max_digits = 12)
    percentageVisited = models.DecimalField(decimal_places = 2, max_digits = 5)
    closedPubs        = models.IntegerField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(StatisticsSingleton, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk = 1)
        return obj


class GuindexUser(models.Model):
    """
        Class to keep track of settings and user contributions.
    """

    userProfile          = models.OneToOneField(UserProfile) # Not really a plugin
    emailAlerts          = models.BooleanField(default = False)
    telegramAlerts       = models.BooleanField(default = False)
    pubsVisited          = models.IntegerField(default = True)
    originalPrices       = models.IntegerField(default = True)
    currentVerifications = models.IntegerField(default = True)


class UserContribution(models.Model):

    title      = models.CharField(max_length = 50)
    descripton = models.TextField()
    url        = models.TextField()
