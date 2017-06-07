#!/usr/bin/python

''' =========================================================================================== '''
# Functions to do the triangulation to get the locations of peripherals
#
# By using it, Call estimateLocation(centralA, centralB, centralC, distA, distB, distC)
#
# where centralA, centralB and centralC are the closest three central devices' coordinates
# as tuples, i.e. (x,y)
# distA, distB and distC are the distances from this peripherial to the three centrals.
#
''' =========================================================================================== '''

# Return the distance between two given points
# Points are given by coordinates as tuples, i.e.(x,y)
def distance(point1, point2):
	return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

# Helper function of calculating the Intersection for CASE3 which
# is the general case that two circles have intersections
def getGeneralIntersect(circleA, circleB, toCompare, dist1, dist2):
	dSqr = ((circleB[0]-circleA[0])**2 + (circleB[1]-circleA[1])**2)
	K = (0.25) * (math.sqrt(((dist1+dist2)**2 - dSqr) * (dSqr - (dist1-dist2)**2)))

	x1 = ((0.5)*(circleB[0] + circleA[0]) + (1/2)*(circleB[0] - circleA[0])*(dist1**2 - dist2**2)/dSqr) + (2*(circleB[1]-circleA[1])*K/dSqr)
	x2 = ((0.5)*(circleB[0] + circleA[0]) + (1/2)*(circleB[0] - circleA[0])*(dist1**2 - dist2**2)/dSqr) - (2*(circleB[1]-circleA[1])*K/dSqr)
	y1 = ((0.5)*(circleB[1] + circleA[1]) + (1/2)*(circleB[1] - circleA[1])*(dist1**2 - dist2**2)/dSqr) - (2*(circleB[0]-circleA[0])*K/dSqr)
	y2 = ((0.5)*(circleB[1] + circleA[1]) + (1/2)*(circleB[1] - circleA[1])*(dist1**2 - dist2**2)/dSqr) + (2*(circleB[0]-circleA[0])*K/dSqr)

	point1 = (x1, y1)
	point2 = (x2, y2)

    # pick the point that closer to the third point
	if(distance(point1, toCompare) <= distance(point2, toCompare)):
		return point1
	else:
		return point2

# Get the intersections given two centrals and distances
# Return the intersection by coordinate as tuples, i.e.(x,y)
def getIntersect(center1, center2, centerToCompare, dist1, dist2):
	# CASE 1: if one circle is inside the other
	if(dist1 > distance(center1, center2) + dist2):
		while(dist1 > distance(center1, center2) + dist2):
			dist2 += 1
		return getGeneralCaseIntersect(center2, center1, centerToCompare, dist1, dist2)
	elif(dist2 > distance(center1, center2) + dist1):
		while(dist2 > distance(center1, center2) + dist1):
			dist1 += 1
	# CASE 2: if two circles are independent
	elif(distance(center1, center2) > (dist1 + dist2)):
		while(distance(center1, center2) > (dist1 + dist2)):
			dist1 += 1
			dist2 += 1
	# CASE 3: else the general case that two circles have intersections
	return getGeneralIntersect(center1, center2, centerToCompare, dist1, dist2)

# Get the estimated location given the centrals and distances
# First estimate the region that peripherial device can be contained
# then return the center of that region by coordinates as tuples
def estimateLocation(centralA, centralB, centralC, distA, distB, distC):
	p1 = getIntersect(centralA, centralB, centralC, distA, distB)
	p2 = getIntersect(centralB, centralC, centralA, distB, distC)
	p3 = getIntersect(centralC, centralA, centralB, distC, distA)

	# Check if points are the same
	if(p1 == p2 and p2 == p3):
		return p1
	elif(p1 == p2 or p3 == p2):
		return ((p1[0]+p3[0])/2, (p1[1]+p3[1])/2)
	elif(p1 == p3):
		return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
	else:
		return ((p1[0]+p2[0]+p3[0])/3, (p1[1]+p2[1]+p3[1])/3)