import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize

friends = [[0, 0, 1, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 1, 1],
           [1, 0, 0, 1, 1, 0, 0],
           [1, 0, 1, 0, 1, 0, 0],
           [1, 0, 1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 1],
           [0, 1, 0, 0, 0, 1, 0]]

gender = [[0, 0, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 1, 1],
          [1, 0, 0, 1, 1, 0, 0],
          [1, 0, 1, 0, 1, 0, 0],
          [1, 0, 1, 1, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 1],
          [0, 1, 0, 0, 0, 1, 0]]

row = ["Bob", "Alice", "Frank", "George", "Dennis", "Claire", "Esther"]
col = ["Bob", "Alice", "Frank", "George", "Dennis", "Claire", "Esther"]

friendMatrix = pd.DataFrame(friends, index=row, columns=col)
genderMatrix = pd.DataFrame(gender, index=row, columns=col)

options = {"maxiter": 50000, "rng": 1}

qap = scipy.optimize.quadratic_assignment(friendMatrix, genderMatrix, options=options)

print(qap)

# graph quadratic assignment
plt.plot(scipy.optimize.quadratic_assignment(friendMatrix, genderMatrix, options=options).col_ind)
plt.show()
