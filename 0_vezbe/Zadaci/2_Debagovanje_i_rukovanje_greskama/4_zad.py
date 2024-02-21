"""Napraviti program koji ispisuje jučerašnji, današnji I sutrašnji datum."""

import datetime

def vreme():
    danas = datetime.datetime.today() 
    print(f"Danas: {danas}")

    juce = danas - datetime.timedelta(days = 1) # time delta oduzima odnosno dodaje dani u odnosu na danas
    print(f"Juce: {juce}")

    sutra = danas + datetime.timedelta(days = 1)
    print(f"Sutra: {sutra}")

vreme()