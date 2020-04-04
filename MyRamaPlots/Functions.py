import sys
import numpy as np
import math
import matplotlib.pyplot as plt

def read_PDB(file_name):
    """
    Reads a PDB file
    :param file_name: Name of the file
    :return: List of atoms
    """
    my_atmos = []
    input_file_name = file_name
    try:
        my_fo = open(input_file_name, 'r')
    except IOError:
        print('Error! Can not find file', input_file_name)
        sys.exit('Finishing program execution!')
    for line in my_fo:
        if 'ATOM' in line[0:6]:
            my_atmos.append(line)
    my_fo.close()

    return my_atmos


def torsion(p1, p2, p3, p4):
    """
    Function to calculate torsion angle for atoms a,b,c, and d
    """

    # Get coordinates for vectors q1, q2 and q3
    q1 = np.subtract(p2, p1)  # b - a
    q2 = np.subtract(p3, p2)  # c - b
    q3 = np.subtract(p4, p3)  # d - c
    # Calculate cross vectors
    q1_x_q2 = np.cross(q1, q2)
    q2_x_q3 = np.cross(q2, q3)
    n1 = q1_x_q2 / np.sqrt(np.dot(q1_x_q2, q1_x_q2))
    n2 = q2_x_q3 / np.sqrt(np.dot(q2_x_q3, q2_x_q3))
    # Calculate unit vectors
    u1 = n2
    u3 = q2 / (np.sqrt(np.dot(q2, q2)))
    u2 = np.cross(u3, u1)
    # Calculate cosine and sine
    cos_theta = np.dot(n1, u1)
    sin_theta = np.dot(n1, u2)
    # Calculate torsion angle
    theta = -math.atan2(sin_theta, cos_theta)
    theta_deg = np.degrees(theta)

    # Return torsion angle in degrees
    return theta_deg


def calc_torsion(list_of_atoms_in):
    """
    Function to calculate torsion angles
    """
    # We have the number of rows and number of columns equal to 3
    # matrix = [[0]*column for i in range(row)]
    columns = 3
    rows = len(list_of_atoms_in)
    co = np.array([[0] * columns] * rows, float)
    n = np.array([[0] * columns] * rows, float)
    ca = np.array([[0] * columns] * rows, float)
    # Set up counts
    count_ca = 0
    count_co = 0
    count_n = 0
    count_res = 0
    for line in list_of_atoms_in:
        if line[13:15] == "C ":
            co[count_co][0] = float(line[30:38])
            co[count_co][1] = float(line[38:46])
            co[count_co][2] = float(line[46:54])

            count_co += 1
        elif line[13:15] == "N ":
            n[count_n][0] = float(line[30:38])
            n[count_n][1] = float(line[38:46])
            n[count_n][2] = float(line[46:54])
            count_n += 1
        elif line[13:15] == "CA":
            ca[count_ca][0] = float(line[30:38])
            ca[count_ca][1] = float(line[38:46])
            ca[count_ca][2] = float(line[46:54])
            count_ca += 1

        count_res += 1
    # Set up arrays for phi and psi angles
    phi = np.zeros(count_res - 1)
    psi = np.zeros(count_res - 1)
    # Looping through phi psi atoms in each residue
    for i in range(count_res - 2):
        # Calls torsion function
        phi[i] = torsion(co[i], n[i + 1], ca[i + 1], co[i + 1])
        psi[i] = torsion(n[i + 1], ca[i + 1], co[i + 1], n[i + 2])
    # Return arrays
    return phi, psi


def plot(x, y, x_label_in, y_label_in):
    """
    Function to plot two one-dimensional arrays
    """
    # Generate plot
    plt.plot(x, y, ".")
    plt.xlim(-180, 180)  # Sets axis limits
    plt.ylim(-180, 180)  # Sets axis limits
    plt.xticks(np.arange(-180.1, 180.1, 30))  # Sets ticks markers for x axis
    plt.yticks(np.arange(-180.1, 180.1, 30))  # Sets ticks makers for y axis
    plt.xlabel(x_label_in)  # Adds axis label
    plt.ylabel(y_label_in)  # Adds axis label
    plt.arrow(-180, 0, 360, 0)  # Creates an arrow
    plt.arrow(0, -180, 0, 360)  # Creates an arrow
    # Show plot
    plt.show()
