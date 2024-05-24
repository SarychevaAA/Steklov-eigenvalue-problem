from _algorithm_finding_eigenfunctions import AlgorithmFindingEigenfunctions
import numpy as np
import random
import constants
import matplotlib.pyplot as plt


class AlgorithmDirichlet1D(AlgorithmFindingEigenfunctions):
    def __init__(self, count_functions, count_nodes_x, start_area_x, finish_area_x, count_nodes_y=None,
                 start_area_y=None,
                 finish_area_y=None, tol=0.001):
        super().__init__(count_functions, count_nodes_x, start_area_x, finish_area_x, count_nodes_y, start_area_y,
                         finish_area_y, tol)

    def random_vector(self):
        start_vector = []
        for i in range(self.count_nodes_x - 2):
            start_vector.append([random.uniform(self.min_value_start_function, self.max_value_start_function)])
        return np.array(start_vector)

    def building_matrix(self):
        if self.count_nodes_x < 2:
            print("Для задачи Дерехле требуется больше 2 точек")
        x_area = np.linspace(self.start_area_x, self.finish_area_x, self.count_nodes_x)
        size_matrix_A = size_matrix_M = self.count_nodes_x - 2
        self.step_on_area_x = x_area[1] - x_area[0]

        self.M = np.array([np.zeros(size_matrix_M) for _ in range(size_matrix_M)])
        for j in range(size_matrix_M):
            for i in range(size_matrix_M):
                if i == j:
                    self.M[j][i] = self.step_on_area_x * constants.KOEF_MATRIX_M_2D_DIRICHLET["complete_intersection"]
                if abs(i - j) == 1:
                    self.M[j][i] = self.step_on_area_x * constants.KOEF_MATRIX_M_2D_DIRICHLET["partial_intersection"]

        self.A = np.array([np.zeros(size_matrix_A) for _ in range(size_matrix_A)])
        for j in range(size_matrix_A):
            for i in range(size_matrix_A):
                if i == j:
                    self.A[j][i] = 1 / self.step_on_area_x * constants.KOEF_MATRIX_A_2D_DIRICHLET[
                        "complete_intersection"]
                if abs(i - j) == 1:
                    self.A[j][i] = 1 / self.step_on_area_x * constants.KOEF_MATRIX_A_2D_DIRICHLET[
                        "partial_intersection"]

    @staticmethod
    def preparing_vectors_for_drawing(vectors):
        array_vectors = []
        for el in vectors:
            vector = [0]
            for i in el:
                vector.append(i[0])
            vector.append(0)
            array_vectors.append(vector)
        return array_vectors

    def plot_vectors(self):
        x_area = np.linspace(self.start_area_x, self.finish_area_x, self.count_nodes_x)
        figure = plt.figure(figsize=(25, 15))
        array_final_vectors = self.preparing_vectors_for_drawing(self.array_final_vectors)
        array_start_vectors = self.preparing_vectors_for_drawing(self.array_start_vectors)
        for i in range(len(array_start_vectors)):
            ax = figure.add_subplot(2, 2, i + 1)
            ax.plot(x_area, array_final_vectors[i], '-b', label="Собственная функция №" + str(i + 1))
            ax.plot(x_area, array_start_vectors[i], '-.m',
                    label="Начальное приближение собственной функции №" + str(i + 1))
            plt.legend(fontsize=13)
            ax.set_title("Собственная функция задачи Дирихле №" + str(i + 1), fontsize=16)
            ax.set_ylabel('y', fontsize=14)
            ax.set_xlabel('x', fontsize=14)
        plt.show()
