import os
from kinematicsLibrary import *

os.system('cls')

T = TransformDesired(128.167582,-101.224607,440.447678,116.194,20.604,62.554)
S = CalculateThetaValues(T)
PrintAngleSolution(S)

"""
[     0.431438,     0.537267,     0.724711,   128.167582 ;
      0.830679,     0.076767,    -0.551434,  -101.224607 ;
     -0.351901,     0.839912,    -0.413176,   440.447678 ;
      0.000000,     0.000000,     0.000000,     1.000000 ];
"""