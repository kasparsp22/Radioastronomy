
# page_4 exercise_5


# Write a complex number by a given number of degrees in the complex plane -e.g
# a  = 1.0 +1.0j
# b = 90.0
# [ my code
# returns -1.0 + 1.0j

import math

compl_numb = 1.0 + 1.0j
angle_to_rot_deg = 90

angle_to_rot_rad = math.radians(angle_to_rot_deg)  # Converts deg to rad
angle_to_rot_compl = math.cos(angle_to_rot_rad)+math.sin(angle_to_rot_rad)*1j  # Converts deg to complex value

rotated_vec = compl_numb*angle_to_rot_compl  # Rotating vector by doing multiplication
print 'Rotating vector ',compl_numb, 'by angle',angle_to_rot_deg, 'we get vector', rotated_vec
print math.atan(-1)*180/math.pi

