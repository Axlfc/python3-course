#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.http import HttpResponse


def greet(request):
    return HttpResponse("Hello World!")


def bye(request):
    return HttpResponse("Goodbye!")


def adult(request, age):
    if age >= 18:
        return HttpResponse("+18")
    else:
        return HttpResponse("Under 18")