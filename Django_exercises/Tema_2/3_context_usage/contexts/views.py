#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.shortcuts import render


def simple(request):
    return render(request, 'simple.html', {})


def dynamic(request, name):
    categories = ['code', 'design', 'art']
    context = {'name_tag': name,
               'categories': categories
               }
    return render(request, 'dynamic.html', context)
