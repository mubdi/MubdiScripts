#!/usr/bin/env python
# Converting Equatorial to Galactic Coordinates
# Algorithms taken from the WCStools Subroutines
# Mubdi Rahman, May 31, 2010

import numpy as n


# The Equatorial to Galactic Rotation Matrix

jgal = n.array( [[-0.054875539726,-0.873437108010,-0.483834985808],\
                     [0.494109453312,-0.444829589425, 0.746982251810],\
                     [-0.867666135858,-0.198076386122, 0.455983795705]])



def s2v3(rra, rdec, r):
    pos0 = r * n.cos(rra) * n.cos(rdec) 
    pos1 = r * n.sin(rra) * n.cos(rdec) 
    pos2 = r * n.sin(rdec)
    return n.array([pos0, pos1, pos2])

def v2s3(pos):
    x = pos[0]
    y = pos[1]
    z = pos[2]

    if n.isscalar(x): x, y, z = n.array([x]), n.array([y]), n.array([z])
    rra = n.arctan2(y, x)

    low = n.where(rra < 0.0)
    high = n.where(rra > 2.0 * n.pi)
    if len(low[0]): rra[low] = rra[low] + (2.0*n.pi)
    if len(high[0]): rra[high] = rra[high] - (2.0*n.pi)

    rxy = n.sqrt(x**2 + y**2)
    rdec = n.arctan2(z, rxy)
    r = n.sqrt(x**2 + y**2 + z**2)

    if x.size == 1:
        rra = rra[0]
        rdec = rdec[0]
        r = r[0]

    return rra, rdec, r

def gal2fk5(gl, gb):

    dgl = n.array(gl)
    dgb = n.array(gb)
    rgl = n.deg2rad(gl) 
    rgb = n.deg2rad(gb)
    r = 1.0
    pos = s2v3(rgl, rgb, r)

    pos1 = n.dot(pos.transpose(), jgal).transpose()

    rra, rdec, r = v2s3(pos1)
    
    dra = n.rad2deg(rra)
    ddec = n.rad2deg(rdec)

    return dra, ddec

def fk52gal(ra, dec):

    dra = n.array(ra)
    ddec = n.array(dec)
    rra = n.deg2rad(ra) 
    rdec = n.deg2rad(dec)
    r = 1.0
    pos = s2v3(rra, rdec, r)

    pos1 = n.dot(jgal, pos)

    rgl, rgb, r = v2s3(pos1)
    
    dgl = n.rad2deg(rgl)
    dgb = n.rad2deg(rgb)

    return dgl, dgb
