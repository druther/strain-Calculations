'''The aim of this project is to calculate the torsion at a particular point 
   in different shaped bars and calculate the location of the point with maximum torsion'''

import math
import numpy

pi = 3.14

class torsion:

  def __init__(self):
    self.yz, self.zx, self.ip ,self.total, self.maximum = 0.0,0.0,0.0,0.0,0.0
    self.theta = 0.0

  '''Function to give torsion whena circular beam is selected'''
  def circular(self):
    print 'Enter radius of beam and torsion'
    values = str(raw_input()).split(',')
    c = int(values[0])
    torsion = int(values[1])

    print 'Enter coordinates where torsion is to be calculated'
    values = str(raw_input()).split(',')
    x = float(values[0]) 
    y = float(values[1])

    self.ip = pi * math.pow(c,4)/2.0
    self.yz = torsion*x/self.ip
    self.zx = (-1.0)*torsion*y/self.ip
    self.theta = math.atan((-1.0)*x/y)

    self.total = math.sqrt(math.pow(self.yz,2) + math.pow(self.yz,2))

    
  
def main():
  t = torsion()
  print "Select the type of beam -"
  print "1 - Circular"
  print "2 - Eliptical"
  print "3 - Triangle"
  choice = input()
  if choice == 1:
      t.circular()

  
  print 'The component of stresses are :' + str((t.yz,t.zx))
  print 'The resultant stress has a magnitude of '+ str(t.total)+' and is directed at an angle of ' +str(t.theta)+' radians'

main()
