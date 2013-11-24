#!/usr/bin/env python
# Interstellar Extinction Curve 
# Taken from Cardelli, J. A., Clayton., G. C., & Mathis, 
# J.S., 1989, ApJ, 345, 245.

"""
The Interstellar Extinction Curve
"""

import numpy as n

def alambda(lam1, rv1=3.1):
    """
    The ratio of extinctions (in Magnitudes) with respect to the wavelength
    in microns
    """
    
    if n.isscalar(lam1): 
        lam1 = n.array([lam1])
    
    lam1 = n.array(lam1)
    
    xx1 = 1.0/lam1

    aa1 = n.zeros(n.size(xx1))
    bb1 = n.zeros(n.size(xx1))
    
    index1 = n.where((xx1 >= 0.3) & (xx1 < 1.1))
    index2 = n.where((xx1 >= 1.1) & (xx1 < 3.3))
    index3 = n.where((xx1 >= 3.3) & (xx1 < 8.0))
    index4 = n.where((xx1 >= 8.0) & (xx1 <= 10.0))

    if n.size(index1):
        aa1[index1] = 0.574*xx1[index1]**1.61
        bb1[index1] = -0.527*xx1[index1]**1.61    
    
    if n.size(index2):
        pol1 = [0.32999, -0.77530, 0.01979, 0.72085, -0.02427, -0.50447, \
        0.17699, 1]
        pol2 = [-2.09002, 5.30260, -0.62251, -5.38434, 1.07233, 2.28305, \
        1.41338, 0]
        yy1 = xx1[index2]-1.82
        aa1[index2] = n.polyval(pol1, yy1)
        bb1[index2] = n.polyval(pol2, yy1)
    
    if n.size(index3):
        tempx = xx1[index3]
        fa1 = n.zeros(n.size(index3))
        fb1 = n.zeros(n.size(index3))
        tempindex = n.where(tempx >= 5.9)
        
        if n.size(tempindex): 
            fa1[tempindex] = -0.04473*(tempx[tempindex]-5.9)**2 - \
            0.009779*(tempx[tempindex]-5.9)**3
            fb1[tempindex] = 0.2130*(tempx[tempindex]-5.9)**2 + \
            0.1207*(tempx[tempindex]-5.9)**3

        aa1[index3] =  1.752 - 0.316*tempx + fa1 - 0.104/(((tempx-4.67)**2)\
        +0.341)
        bb1[index3] =  -3.090 + 1.825*tempx + fb1 + 1.206/(((tempx-4.62)**2)\
        +0.341)
        
    if n.size(index4):
        tempx = xx1[index4] - 8
        aa1[index4] = -1.073 - 0.628*tempx + 0.137*tempx**2 - 0.070*tempx**3
        bb1[index4] =  13.670 + 4.257*tempx - 0.420*tempx**2 + 0.374*tempx**3
        
    
    alam = aa1 + bb1/rv1

    if n.size(alam) == 1: 
        alam = alam[0]
    
    return alam