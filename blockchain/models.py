from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class WebSocket(TimeStampedModel):
    uri = models.URLField(
        verbose_name=_('URI'),
        unique=True,
    )

    class Meta:
        verbose_name = _('socket')
        verbose_name_plural = _('sockets')

        indexes = [
            models.Index(fields=['created', ]),
        ]

    def __str__(self):
        return '{} {}'.format(self.uri, self.created)


class Block(models.Model):
    index = models.IntegerField(
        verbose_name=_('index'),
        unique=True,
    )

    previous_block_hash = models.CharField(
        verbose_name=_('previous block hash'),
        max_length=128,
        unique=True,
    )

    hash = models.CharField(
        verbose_name=_('block hash'),
        max_length=128,
        unique=True,
    )

    difficulty = models.IntegerField(
        verbose_name=_('difficulty'),
    )

    nonce = models.IntegerField(
        verbose_name=_('nonce'),
    )

    timestamp = models.DateTimeField(
        verbose_name=_('timestamp'),
    )

    data = models.TextField(
        verbose_name=_('transaction data'),
    )

    class Meta:
        verbose_name = _('block')
        verbose_name_plural = _('blocks')

    def __str__(self):
        return '{} {} {} {} {}'.format(self.index, self.hash, self.difficulty, self.nonce, self.timestamp)
