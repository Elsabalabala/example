#!usr/bin/env python
#coding=utf-8

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(numerator, denominator):
    if denominator!=0:
        return float(numerator) / denominator
    else:
        return "error input"

def pow(a, b):
        return a ** b
