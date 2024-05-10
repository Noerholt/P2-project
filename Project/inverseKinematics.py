import os
import kinematicsLibrary as k

os.system('cls')

T = k.TransformDesired(-163.079247,-153.284908,464.035240,85.371,-24.595,11.010)
S = k.CalculateThetaValues(T)
k.printSolution(S)

"""
[     0.892539,    -0.422618,     0.157379,  -163.079247 ;
      0.173648,     0.000000,    -0.984808,  -153.284908 ;
      0.416198,     0.906308,     0.073387,   464.035240 ;
      0.000000,     0.000000,     0.000000,     1.000000 ];
"""