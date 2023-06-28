#from django.shortcuts import render, redirect, get_object_or_404
#from ..models import Category, Writer, Book
from django import template
register = template.Library()


@register.filter(name='text_short')
def text_short(value):
	temp = value[0:18]
	return temp
