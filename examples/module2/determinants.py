import numpy as np
A = np.array(
    [[4, -5, 7],
     [1, -4, 9],
     [-4, 0, 5],
     ]
    )
At = np.transpose(A)
print("Початкова матриця A:")
print(A)
print(f"Визначник базової матриці А: {int(np.linalg.det(A))}")
print("Транспонована матриця At:")
print(At)
print(f"Визначник транспонованої матриці At: {int(np.linalg.det(At))}")

########################

import numpy as np
A = np.array(
    [[2, 7, 1, 2],
     [6, 1, 3, -1],
     [0, 0, 0, 0],
     [2, 9, 5, -1],
     ]
    )
print(f"Визначник матриці А: {int(np.linalg.det(A))}")

##################

import numpy as np
A = np.array(
    [[1, 0, -1],
     [11, 4, 7],
     [-6, 0, 0],
     ]
    )
B = np.array(
    [[11, 4, 7],
     [1, 0, -1],
     [-6, 0, 0],
     ]
    )
print(f"Визначник матриці А: {int(np.linalg.det(A))}")
print(f"Визначник матриці B: {int(np.linalg.det(B))}")

###################

import numpy as np
A = np.array(
    [[2, 7, 1, 2],
     [6, 1, 3, -1],
     [2, 7, 1, 2],
     [2, 9, 5, -1],
     ]
    )
print(f"Визначник матриці А: {int(np.linalg.det(A))}")

###########

import numpy as np
A = np.array(
    [[2, 4, -12],
     [10, 3, 0],
     [1, -1, 1],
     ]
    )
B = np.array(
    [[1, 2, -6],
     [10, 3, 0],
     [1, -1, 1],
     ]
    )
print(f"Визначник матриці А: {int(np.linalg.det(A))}")
print(f"Визначник матриці B: {int(np.linalg.det(B))}")

#####################

import numpy as np
A = np.array(
    [[6, 4, 12],
     [10, 3, 0],
     [1, -1, 1],
     ]
    )
# [6,4,12] = [2+4,3+1,9+3]
B = np.array(
    [[2, 3, 9],
     [10, 3, 0],
     [1, -1, 1],
     ]
    )
C = np.array(
    [[4, 1, 3],
     [10, 3, 0],
     [1, -1, 1],
     ]
    )
print(f"Визначник матриці А: {round(np.linalg.det(A))}")
print(f"Визначник матриці B: {round(np.linalg.det(B))}")
print(f"Визначник матриці C: {round(np.linalg.det(C))}")

#########

import numpy as np
A = np.array(
    [[2, 7, -1],
     [0, 1, 3],
     [2, 9, 5],
     ]
    )
print(f"Визначник матриці А: {round(np.linalg.det(A))}")

###############

import numpy as np
A = np.array(
    [[3, 8, 0],
     [1, 1, 1],
     [2, 9, 5],
     ]
    )
# Зміни: новий рядок 1 = рядок 1 - рядок 2
B = np.array(
    [[2, 7, -1],
     [1, 1, 1],
     [2, 9, 5],
     ]
    )
print(f"Визначник матриці А: {round(np.linalg.det(A))}")
print(f"Визначник матриці B: {round(np.linalg.det(B))}")

#############

import numpy as np
A = np.array(
    [[4, -5, 7],
     [1, -4, 9],
     [-4, 0, 5],
     ]
    )
print(round(np.linalg.det(A)))

