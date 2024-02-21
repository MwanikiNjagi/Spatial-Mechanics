#script for simple mathematical transformations of a point through different axis
import numpy as np
import math as m

#Translation
def Z_axis_translation(theta, vector):
    vector = np.array([vector])
    vector = vector.T
    
    z_axis = [[ 1, 0, 0 ],
             [ 0, m.cos(theta),-m.sin(theta)],
             [ 0, m.sin(theta), m.cos(theta)]]

    z_trans_cood = np.matmul(z_axis,vector)
   
    return z_trans_cood



def Y_axis_translation(theta, vector):
    vector = np.array([vector])
    vector = vector.T

    y_axis =[[ m.cos(theta), 0, m.sin(theta)],
            [ 0           , 1, 0           ],
            [-m.sin(theta), 0, m.cos(theta)]]
    
    y_trans_cood = np.matmul (y_axis, vector)
   
    return y_trans_cood


def X_axis_translation(theta, vector):
    vector = np.array([vector])
    vector = vector.T

    x_axis = [[ m.cos(theta), -m.sin(theta), 0 ],
            [ m.sin(theta), m.cos(theta) , 0 ],
            [ 0           , 0            , 1 ]]
    
   
    x_trans_cood = np.matmul(x_axis, vector)
    return x_trans_cood



#Example problems for transformation
#defining point
single_axis_robot = [4, 4, 3.464]

#transforming it about 60 degrees in the y axis
single_axis_robot_trans = Y_axis_translation(60, single_axis_robot)

print(single_axis_robot_trans)