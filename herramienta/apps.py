# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class HerramientaConfig(AppConfig):
    name = 'herramienta'

    def ready(self):
       import signals
