# -*- coding: utf-8 -*-
"""
Raster Accuracy Assessment Plugin
Herhangi iki raster harita için doğrulama analizi
"""

def classFactory(iface):
    from .accuracy_assessment import AccuracyAssessmentPlugin
    return AccuracyAssessmentPlugin(iface)
