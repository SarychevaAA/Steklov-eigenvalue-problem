from _algorithm_finding_eigenfunctions import AlgorithmFindingEigenfunctions
import numpy as np
import random
import constants
import matplotlib.pyplot as plt


class AlgorithmNeumann1D(AlgorithmFindingEigenfunctions):
    def __init__(self, count_functions, count_nodes_x, start_area_x, finish_area_x, count_nodes_y=None,
                 start_area_y=None,
                 finish_area_y=None, tol=0.001):
        super().__init__(count_functions, count_nodes_x, start_area_x, finish_area_x, count_nodes_y, start_area_y,
                         finish_area_y, tol)

    def random_vector(self):
        start_vector = []
        for i in range(self.count_nodes_x):
            start_vector.append([random.uniform(self.min_value_start_function, self.max_value_start_function)])
        return np.array(start_vector)

    def building_matrix(self):
        x_area = np.linspace(self.start_area_x, self.finish_area_x, self.count_nodes_x)
        size_matrix_M = size_matrix_A = self.count_nodes_x
        self.step_on_area_x = x_area[1] - x_area[0]
        self.M = np.array([np.zeros(size_matrix_M) for _ in range(size_matrix_M)])
        for j in range(size_matrix_M):
            for i in range(size_matrix_M):
                if i == j:
                    if i == 0 or i == self.count_nodes_x - 1:
                        self.M[j][i] = self.step_on_area_x * constants.KOEF_MATRIX_M_2D_NEUMON[
                            "complete_intersection_border"]
                    else:
                        self.M[j][i] = self.step_on_area_x * constants.KOEF_MATRIX_M_2D_NEUMON["complete_intersection"]
                if abs(i - j) == 1:
                    self.M[j][i] = self.step_on_area_x * constants.KOEF_MATRIX_M_2D_NEUMON["partial_intersection"]
        self.A = np.array([np.zeros(size_matrix_A) for _ in range(size_matrix_A)])
        for j in range(size_matrix_A):
            for i in range(size_matrix_A):
                if i == j:
                    if i == 0 or i == self.count_nodes_x - 1:
                        self.A[j][i] = (1 / self.step_on_area_x) * constants.KOEF_MATRIX_A_2D_NEUMON[
                            "complete_intersection_border"]
                    else:
                        self.A[j][i] = (1 / self.step_on_area_x) * constants.KOEF_MATRIX_A_2D_NEUMON[
                            "complete_intersection"]
                if abs(i - j) == 1:
                    self.A[j][i] = (1 / self.step_on_area_x) * constants.KOEF_MATRIX_A_2D_NEUMON["partial_intersection"]
        print("M:", self.M)
        print("A", self.A)

    def plot_vectors(self):
        x_area = np.linspace(self.start_area_x, self.finish_area_x, self.count_nodes_x)
        figure = plt.figure(figsize=(25, 15))
        ax = figure.add_subplot(1, 1, 1)
        for i in range(len(self.array_final_vectors)):
            ax.plot(x_area, self.array_final_vectors[i], '-b', label="Собственная функция №" + str(i + 1))
            ax.plot(x_area, self.array_start_vectors[i], '-.m',
                    label="Начальное приближение собственной функции №" + str(i + 1))
            plt.legend(fontsize=13)
            ax.set_title("Собственная функция задачи Неймана №" + str(i + 1), fontsize=16)
            ax.set_ylabel('y', fontsize=14)
            ax.set_xlabel('x', fontsize=14)
        plt.show()
