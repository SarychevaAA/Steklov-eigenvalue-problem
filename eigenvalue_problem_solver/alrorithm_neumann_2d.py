from _algorithm_finding_eigenfunctions import AlgorithmFindingEigenfunctions
import numpy as np
import random
import time
import matplotlib.pyplot as plt
from scipy.interpolate import RegularGridInterpolator


class AlgorithmNeumann2D(AlgorithmFindingEigenfunctions):
    def __init__(self, count_functions, count_nodes_x, start_area_x, finish_area_x, count_nodes_y=None,
                 start_area_y=None, finish_area_y=None, tol=0.001):
        super().__init__(count_functions, count_nodes_x, start_area_x, finish_area_x, count_nodes_y, start_area_y,
                         finish_area_y, tol)

    def random_vector(self, count_nodes_x, count_nodes_y):
        start_vector = []
        for i in range(count_nodes_x * count_nodes_y):
            start_vector.append([random.uniform(self.min_value_start_function, self.max_value_start_function)])
        return np.array(start_vector)

    def building_matrix(self, start_area_x, finish_area_x, count_nodes_x, start_area_y, finish_area_y, count_nodes_y, ):
        x_area = np.linspace(start_area_x, finish_area_x, count_nodes_x)
        y_area = np.linspace(start_area_y, finish_area_y, count_nodes_y)
        size_matrix_M = size_matrix_A = count_nodes_x * count_nodes_y
        self.M = np.array([np.zeros(size_matrix_M) for _ in range(size_matrix_M)])
        self.step_on_area_x = x_area[1] - x_area[0]
        self.step_on_area_y = y_area[1] - y_area[0]
        file1 = open('M.txt', 'w')

        for ind1 in range(size_matrix_M):
            for ind2 in range(size_matrix_M):
                i_ind1 = ind1 % count_nodes_x
                j_ind1 = ind1 // count_nodes_y
                i_ind2 = ind2 % count_nodes_x
                j_ind2 = ind2 // count_nodes_y
                if ind1 == ind2:
                    if j_ind1 == 0 or j_ind1 == count_nodes_y - 1:
                        if i_ind1 == 0 or i_ind1 == count_nodes_x - 1:
                            self.M[ind1][ind2] = (self.step_on_area_x * self.step_on_area_y) / 9
                        else:
                            self.M[ind1][ind2] = 2 * (self.step_on_area_x * self.step_on_area_y) / 9
                    elif i_ind1 == 0 or i_ind1 == count_nodes_x - 1:
                        self.M[ind1][ind2] = 2 * (self.step_on_area_x * self.step_on_area_y) / 9
                    else:
                        self.M[ind1][ind2] = 4 * (self.step_on_area_x * self.step_on_area_y) / 9
                if abs(i_ind1 - i_ind2) == 1 and abs(j_ind1 - j_ind2) == 0:
                    if j_ind1 == 0 or j_ind1 == count_nodes_y - 1:
                        self.M[ind1][ind2] = (self.step_on_area_x * self.step_on_area_y) / 18
                    else:
                        self.M[ind1][ind2] = (self.step_on_area_x * self.step_on_area_y) / 9
                if abs(i_ind1 - i_ind2) == 0 and abs(j_ind1 - j_ind2) == 1:
                    if i_ind1 == 0 or i_ind1 == count_nodes_y - 1:
                        self.M[ind1][ind2] = (self.step_on_area_x * self.step_on_area_y) / 18
                    else:
                        self.M[ind1][ind2] = (self.step_on_area_x * self.step_on_area_y) / 9
                if abs(i_ind1 - i_ind2) == 1 and abs(j_ind1 - j_ind2) == 1:
                    self.M[ind1][ind2] = (self.step_on_area_x * self.step_on_area_y) / 36
                file1.write(str(self.M[ind1][ind2]) + " ")
            file1.write("\n ")
        file1 = open('A.txt', 'w')

        self.A = np.array([np.zeros(size_matrix_A) for _ in range(size_matrix_A)])
        for ind1 in range(size_matrix_A):
            for ind2 in range(size_matrix_A):
                i_ind1 = ind1 % count_nodes_x
                j_ind1 = ind1 // count_nodes_y
                i_ind2 = ind2 % count_nodes_x
                j_ind2 = ind2 // count_nodes_y
                if ind1 == ind2:
                    if j_ind1 == 0 or j_ind1 == count_nodes_y - 1:
                        if i_ind1 == 0 or i_ind1 == count_nodes_x - 1:
                            self.A[ind1][ind2] = 2 / 3
                        else:
                            self.A[ind1][ind2] = 4 / 3
                    elif i_ind1 == 0 or i_ind1 == count_nodes_x - 1:
                        self.A[ind1][ind2] = 4 / 3
                    else:
                        self.A[ind1][ind2] = 8 / 3
                if abs(i_ind1 - i_ind2) == 1 and abs(j_ind1 - j_ind2) == 0:
                    if j_ind1 == 0 or j_ind1 == count_nodes_y - 1 or j_ind2 == 0 or j_ind2 == count_nodes_y - 1:
                        self.A[ind1][ind2] = -1 / 6
                    else:
                        self.A[ind1][ind2] = -1 / 3
                if abs(i_ind1 - i_ind2) == 0 and abs(j_ind1 - j_ind2) == 1:
                    if i_ind1 == 0 or i_ind1 == count_nodes_x - 1:
                        self.A[ind1][ind2] = -1 / 6
                    else:
                        self.A[ind1][ind2] = -1 / 3
                if abs(i_ind1 - i_ind2) == 1 and abs(j_ind1 - j_ind2) == 1:
                    self.A[ind1][ind2] = -1 / 3
                file1.write(str(self.A[ind1][ind2]) + " ")
            file1.write("\n ")

    def bootstrapping(self):
        grid_values = self.generate_grid_value()

        for iter_grid_value in range(len(grid_values)):
            self.building_matrix(self.start_area_x, self.finish_area_x, grid_values[iter_grid_value], self.start_area_y,
                                 self.finish_area_y, grid_values[iter_grid_value])
            array_start_function = []
            if iter_grid_value == 0:
                array_start_function.append(
                    self.generate_start_function_nodes(grid_values[iter_grid_value], grid_values[iter_grid_value]))
            else:
                array_start_function = self.array_final_vectors.copy()
            self.array_final_vectors = []

            for i in range(self.count_functions):
                if iter_grid_value != 0:
                    array_start_function[i] = self.update_vector_len(array_start_function[i],
                                                                     grid_values[iter_grid_value - 1],
                                                                     grid_values[iter_grid_value - 1],
                                                                     grid_values[iter_grid_value],
                                                                     grid_values[iter_grid_value])
                final_vector, log, koef_r = self.rayleigh_quotient_algorithm(array_start_function[i],
                                                                             self.array_final_vectors)
                final_vector = final_vector / np.linalg.norm(final_vector)
                print("Q", self.get_eigenvalue(final_vector))
                self.array_start_vectors.append(array_start_function[i])
                if all(np.abs(np.dot(final_vector.T, col)) < 10e-9 for col in self.array_final_vectors):
                    print("Success")
                else:
                    print("Failure")
                self.array_final_vectors.append(final_vector)
                if iter_grid_value == 0:
                    start_vector = self.find_orth_start_vector(final_vector, self.array_orth_start_vectors)
                    start_vector = start_vector / np.linalg.norm(start_vector)
                    self.array_orth_start_vectors.append(list(final_vector.T[0]))
                    array_start_function.append(start_vector)

    def generate_start_function_nodes(self, count_nodes_x, count_nodes_y):
        start_function_nodes = self.random_vector(count_nodes_x, count_nodes_y)
        start_function_nodes = start_function_nodes / np.linalg.norm(start_function_nodes)
        return start_function_nodes

    def update_vector_len(self, vector, count_x, count_y, count_nodes_x, count_nodes_y):
        x_st_area = np.linspace(self.start_area_x, self.finish_area_x, count_x)
        y_st_area = np.linspace(self.start_area_y, self.finish_area_y, count_y)
        x_area = np.linspace(min(x_st_area[:]), max(x_st_area[:]), count_nodes_x)
        y_area = np.linspace(min(y_st_area[:]), max(y_st_area[:]), count_nodes_y)
        X, Y = np.meshgrid(x_area, y_area)
        vector = np.reshape(vector.T[0], (count_x, count_y))
        interp = RegularGridInterpolator((x_st_area[:], y_st_area[:]), vector)
        Z = interp((X, Y))
        return np.reshape(Z, newshape=(count_nodes_x - 2 * count_nodes_y - 2, 1))

    def plot_vectors(self):
        x_area = np.linspace(self.start_area_x, self.finish_area_x, self.count_nodes_x)
        y_area = np.linspace(self.start_area_y, self.finish_area_y, self.count_nodes_y)
        X, Y = np.meshgrid(x_area, y_area)
        figure = plt.figure(figsize=(25, 15))
        for i in range(len(self.array_final_vectors)):
            ax = figure.add_subplot(2, (self.count_functions // 2 + self.count_functions % 2), i + 1,
                                    projection='3d')
            vector = self.array_final_vectors[i]
            if i == 0:
                vector = np.round(vector, 2)
            vector = np.reshape(vector, (self.count_nodes_y, self.count_nodes_x))
            scat = ax.plot_surface(X, Y, vector, cmap="plasma")
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.set_title("Функция задачи Неймана №" + str(
                i + 1) + "\n" + f"\u03BB={np.abs(float(np.round(self.get_eigenvalue(self.array_final_vectors[i]), 3)))}",
                         fontsize=16)
            plt.colorbar(scat, fraction=0.030, pad=0.1)
            plt.gca().invert_yaxis()
            ax.view_init(20, 60)
        plt.show()

    def alg_process(self):
        start_time = time.time()
        self.bootstrapping()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('Elapsed time: ', elapsed_time)
        self.plot_vectors()

    def generate_grid_value(self):
        grid_values = [10]
        current_grid_value = 10
        while current_grid_value * 2 <= min(self.count_nodes_x, self.count_nodes_y) / 2:
            current_grid_value *= 2
            grid_values.append(current_grid_value)
        grid_values.append(min(self.count_nodes_x, self.count_nodes_y))
        return grid_values
