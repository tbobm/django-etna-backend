#!/usr/bin/env python
"""
Django backend requesting ETNA APIs for auth.

User existence and registration is based on the API request
"""
from django.contrib.auth.models import User
from etnawrapper import EtnaWrapper


class EtnaAPIBackend:
    """Authenticate through the ETNA API."""

    def authenticate(self, request, username=None, password=None):
        """Make a request to the API and check for the return code."""
        client = EtnaWrapper(username=username, password=password)
        infos = client.get_infos()

