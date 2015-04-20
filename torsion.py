'''The aim of this project is to calculate the stress at a particular point 
   in different shaped bars under torsion and calculate the location of the point with maximum stress.

   Developed by - Harsh(12117026), Harshit(12117027), Hemant(12117028), Himanshu(12117029)'''

import math

pi = 3.14
G = 77          # Shear Modulus - Change this depending upon the material

# Object for calculating the stresses
# Has different methods for different-shaped beams
class torsion:

  def __init__(self):
    self.yz, self.zx, self.ip ,self.total, self.maximum = 0.0,0.0,0.0,0.0,0.0
    self.theta = 0.0

  '''Function to give stresses when a circular beam is selected'''
  def circular(self):

    print 'Enter radius of beam and applied torque'
    values = str(raw_input()).split(',')
    c = int(values[0])
    torque = int(values[1])

    print 'Enter coordinates where torsion is to be calculated'
    values = str(raw_input()).split(',')
    x = float(values[0]) 
    y = float(values[1])

    if x>c or y>c:
      print 'Coordinates not possible'
    else:
      self.ip = pi * math.pow(c,4)/2.0
      self.yz = torque*x/self.ip
      self.zx = (-1.0)*torque*y/self.ip
      self.theta = math.atan((-1.0)*x/y)

      self.total = math.sqrt(math.pow(self.yz,2) + math.pow(self.yz,2))
      self.maximum = 2*torque/math.pow(c,3)

      self.max_statement = 'Maximum shear stress occurs at the boundary and has magnitude of :' +str(self.maximum)


  '''Function to give stresses when a elliptical beam is selected'''
  def elliptical(self):

    print 'Enter semi-axes of beam and applied torque'
    values = str(raw_input()).split(',')
    a = int(values[0])
    b = int(values[1])
    torque = int(values[2])

    print 'Enter coordinates where torsion is to be calculated'
    values = str(raw_input()).split(',')
    x = float(values[0])
    y = float(values[1])

    if x>a or y>b:
      print 'Coordinates not possible'
    else:
      self.yz = 2*torque*x/(pi*math.pow(a,3)*b)
      self.zx = 2*torque*y/(pi*a*math.pow(b,3))
      self.theta = torque*(a*a + b*b)/(G*pi*math.pow(a,3)*math.pow(b,3))

      self.total = math.sqrt(math.pow(self.yz,2) + math.pow(self.yz,2))
      minor = min(a,b)
      major = max(a,b)
      self.maximum = 2*torque/(pi*major*minor*minor)
    
      self.max_statement = 'Maximum shear stress occurs at maximum of minor axis and has magnitude of :' +str(self.maximum)


  '''Function to give stresses when a triangular beam is selected'''
  def triangle(self):
    
    print 'Enter side-length of equilateral triangle and applied torque'
    values = str(raw_input()).split(',')
    a = int(values[0])
    torque = int(values[1])

    print 'Enter coordinates where torsion is to be calculated'
    values = str(raw_input()).split(',')
    x = float(values[0])
    y = float(values[1])

    self.ip = 3*1.717*math.pow(a,4)
    self.theta = (1.667*torque)/G*self.ip
    self.yz = (G*self.theta*(x*x - y*y + 2*a*x))/2*a
    self.zx = (G*self.theta*y*(x-a))/a

    self.total = math.sqrt(math.pow(self.yz,2) + math.pow(self.yz,2))
    self.maximum = 1.50*G*self.theta*a

    self.max_statement = 'Largest shear stress occurs at middle of sides of triangle with a magnitude of '+str(self.maximum)
    
  
def main():
  t = torsion()
  print "Select the type of beam -"
  print "1 - Circular"
  print "2 - Eliptical"
  print "3 - Triangle"

  choice = input()
  if choice == 1:
    t.circular()
  elif choice == 2:
    t.elliptical()
  elif choice == 3:
    t.triangle()

  print 'The (yz,zx) component of stresses are :' + str((t.yz,t.zx))
  print 'The resultant stress has a magnitude of '+ str(t.total) +' and is directed at an angle of '+str(t.theta)+' radians'
  print t.max_statement

main()
