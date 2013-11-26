"""
A Simple Module to Create a Matplotlib Custom Colour Map with any number of
colours, as well as setting a specific colour for zero, wherever that lies in
the range

The function to call is makecmap

"""

import numpy as n
import matplotlib


# The Default Colour Map, Negative Values are Red, Zero is White#
colhex = [
	"FF0000",
	"FFFFFF",
	"0776A0",
	"FF8500",
	"00B945",
	"7608AA",
	]


def zeropoint(vmin, vmax):
	if vmin > 0.0: return 0.0

	vrange = 1.0 * (vmax - vmin)

	return (-vmin)/vrange

def hextodecnorm(hexval):
	return int(hexval, 16)/(2.0**8 - 1.0)

def hexcoltonorm(hexstring):
	""" Breaking 3 Value Hex String into component colours """

	collist = []
	collist.append(hextodecnorm(hexstring[0:2]))
	collist.append(hextodecnorm(hexstring[2:4]))
	collist.append(hextodecnorm(hexstring[4:6]))

	return collist 

# Colour 1 is for negative values
# Other Colours are for positive values
# White goes between col1 and col2 

def makecdict(vmin, vmax, collist=colhex):

	numcols = len(collist)

	newcdict = {
		'red': [],
		'green': [],
		'blue':  []
		}

	newvpoints = [0.0]
	newzeropoint = zeropoint(vmin, vmax)
	remainingpoints = n.linspace(newzeropoint, 1.0, numcols-1).tolist()
	newvpoints = newvpoints + remainingpoints

	for i_pt in range(len(newvpoints)):
		coldec = hexcoltonorm(collist[i_pt])
		newcdict['red'].append((newvpoints[i_pt], coldec[0], coldec[0]))
		newcdict['green'].append((newvpoints[i_pt], coldec[1], coldec[1]))
		newcdict['blue'].append((newvpoints[i_pt], coldec[2], coldec[2]))

	return newcdict

def makecmap(vmin, vmax, N=65536, collist=colhex):
	"""
	Makes a matplotlib colour map with values from
	vmin to vmax, with a specific colour set to the zero value.

	Arguments:
		vmin: 		minimum value of dataset 
		vmax: 		maximum value of dataset
		N: 			number of colours to populate in the colour map
		collist: 	list of strings, each holding a hex value for colour
					(without the hashtag in each string).
					A minimum of three colours are required. 
					- The 0th value is for the negative values
					- The 1st value	is for the zeropoint
					- All other values are for positive values

	Returns:
		newcolmap:	A matplotlib colourmap (can send it to various matplotlib
					functions, such as imshow or scatter)

	"""
	cdict = makecdict(vmin, vmax, collist)
	newcolmap = matplotlib.colors.LinearSegmentedColormap("newcolmap", cdict, N=N)

	return newcolmap