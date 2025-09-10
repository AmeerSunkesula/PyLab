#Calculate Volume and Surface Area of a Cone
import math
radius=float(input("Enter the radius of the cone: "))
height=float(input("Enter the height of the cone: "))
volume=(1/3)*math.pi*radius*radius*height
slant_height=math.sqrt(radius*radius+height*height)
surface_area=math.pi*radius*(radius+slant_height)
print(f"Volume of the cone is: {volume:.2f}")
print(f"Surface Area of the cone is: {surface_area:.2f}")