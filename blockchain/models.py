from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class WebSocket(TimeStampedModel):
    url = models.URLField(
        verbose_name=_('url'),
    )

    class Meta:
        verbose_name = _('socket')
        verbose_name_plural = _('sockets')

        indexes = [
            models.Index(fields=['created', ]),
        ]

    def __str__(self):
        return '{} {}'.format(self.url, self.created)
