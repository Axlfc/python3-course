#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.shortcuts import render


def simple(request):
    return render(request, 'simple.html', {})
