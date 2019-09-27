# Automatic probe "Voyager-1", exploring the solar system and its surroundings launched on Sep 5. 1977
#  Sep 25 2009 Voyager-1 was at a distance of 16.637 billion miles from the sun and was traveling at a speed of 38,241 miles / hour.
#  The user enters the number of days from September 25, the program considers the distance in miles, km and the astronomer. units
# # Calculate the delay of wireless communication at a wave propagation speed of 299792458 m / h
days = int(input())
speed = 38241
newdistml = 16637000000 + (speed*24*days)
newdistkm = newdistml*1.61
newdistau = newdistkm/1.496e+8
svspeed = 299792458*3.6
sv = newdistkm/svspeed
print('Distance, miles:', newdistml)
print('Distance, km:',newdistkm)
print('Distance, au:',newdistau)
print('Communication delay:',sv)

