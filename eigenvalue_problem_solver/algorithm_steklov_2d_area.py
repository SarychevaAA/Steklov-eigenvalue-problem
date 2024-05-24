from ._algorithm_finding_eigenfunctions import AlgorithmFindingEigenfunctions
import numpy as np
import random
import time
import matplotlib.pyplot as plt
from scipy.interpolate import RegularGridInterpolator


class AlgorithmSteklov2D(AlgorithmFindingEigenfunctions):
    def __init__(self, count_functions, count_nodes_x, start_area_x, finish_area_x, count_nodes_y=None,
                 start_area_y=None, finish_area_y=None, tol=0.001, start_area=[]):
        super().__init__(count_functions, count_nodes_x, start_area_x, finish_area_x, count_nodes_y, start_area_y,
                         finish_area_y, tol)
        self.index_array_M = None
        self.count_M = 0
        self.index_array = None
        self.index_matrix = None
        self.new_area = None
        self.file_path = './area.txt'
        self.area_x_count_points = 5
        self.area_y_count_points = 5
        self.area = None
        self.change_area_points_x = int(
            (self.count_nodes_x - self.area_x_count_points) / (self.area_x_count_points - 1))
        self.count = 0
        self.start_area = start_area

    def read_area(self):
        f = open('area.txt', 'r')

        self.area = np.array([np.array([int(el) for el in line.strip().split(" ")]) for line in f])
        print(self.area)

    def find_index(self, i, j, array):
        for k in range(len(array)):
            if array[k][0] == i and array[k][1] == j:
                return k
        return -1

    def gran_points(self, i, j):
        if self.new_area[j, i] != 1:
            if (j - 1 >= 0 and self.new_area[j - 1][i] == 1) or (
                    j + 1 < self.count_nodes_y and self.new_area[j + 1][i] == 1) or (
                    i + 1 < self.count_nodes_x and self.new_area[j][i + 1] == 1) or (
                    i - 1 >= 0 and self.new_area[j][i - 1] == 1) or (
                    j - 1 >= 0 and i - 1 >= 0 and self.new_area[j - 1][i - 1] == 1) or (
                    j - 1 >= 0 and i + 1 < self.count_nodes_x and self.new_area[j - 1][i + 1] == 1) or (
                    j + 1 < self.count_nodes_x and i - 1 >= 0 and self.new_area[j + 1][i - 1] == 1) or (
                    j + 1 < self.count_nodes_x and i + 1 < self.count_nodes_x and self.new_area[j + 1][i + 1] == 1):
                return True
        return False

    def preparing_area(self):
        area_x = np.linspace(self.start_area_x, self.finish_area_x, self.count_nodes_x)
        area_y = np.linspace(self.start_area_y, self.finish_area_y, self.count_nodes_y)
        print("AREA", area_x, self.start_area)
        self.new_area = np.array([np.zeros(self.count_nodes_x) for _ in range(self.count_nodes_y)])

        for j in range(self.count_nodes_y):
            for i in range(self.count_nodes_x):
                if self.find_index(area_x[i], area_y[j], self.start_area) != -1:
                    self.new_area[j][i] = 1
        for j in range(self.count_nodes_y):
            for i in range(self.count_nodes_x):
                if self.gran_points(i, j):
                    self.new_area[j][i] = 2
        # for j in range(self.count_nodes_y):
        #     for i in range(self.count_nodes_x):
        #         if self.new_area[j][i] == 1:
        #             if self.new_area[j - 1][i - 1] == 2:
        #                 if self.new_area[j - 1][i] == 2 and self.new_area[j][i - 1] == 2:
        #                     self.new_area[j - 1][i - 1] = 0
        #             if self.new_area[j - 1][i + 1] == 2:
        #                 if self.new_area[j - 1][i] == 2 and self.new_area[j][i + 1] == 2:
        #                     self.new_area[j - 1][i + 1] = 0
        #             if self.new_area[j + 1][i + 1] == 2:
        #                 if self.new_area[j + 1][i] == 2 and self.new_area[j][i + 1] == 2:
        #                     self.new_area[j + 1][i + 1] = 0
        #             if self.new_area[j + 1][i - 1] == 2:
        #                 if self.new_area[j + 1][i] == 2 and self.new_area[j][i - 1] == 2:
        #                     self.new_area[j + 1][i - 1] = 0

        print(self.new_area)
        for j in range(self.count_nodes_y):
            self.count += np.count_nonzero(self.new_area[j] != 0)
            self.count_M += np.count_nonzero(self.new_area[j] != 0)
        self.index_array = np.array([np.zeros(2) for _ in range(self.count)])
        print("COUNT", len(self.index_array))
        self.index_array_M = np.array([np.zeros(2) for _ in range(self.count_M)])
        k = 0
        for j in range(self.count_nodes_y):
            for i in range(self.count_nodes_x):
                if self.new_area[j][i] != 0:
                    self.index_array[k][0] = int(j)
                    self.index_array[k][1] = int(i)
                    k += 1
        size_matrix_M = size_matrix_A = self.count
        file1 = open('M1.txt', 'w')

        self.M = np.array([np.zeros(size_matrix_M) for _ in range(size_matrix_M)])
        self.step_on_area_x = area_x[1] - area_x[0]
        self.step_on_area_y = area_y[1] - area_y[0]
        print("STEP", self.step_on_area_x, self.step_on_area_y)
        # self.step_on_area_x = 0.165
        # self.step_on_area_y = 0.165
        list_need_value = [1, 2]
        for ind1 in range(size_matrix_M):
            for ind2 in range(size_matrix_M):
                i_ind1 = int(self.index_array[ind1][1])
                j_ind1 = int(self.index_array[ind1][0])
                i_ind2 = int(self.index_array[ind2][1])
                j_ind2 = int(self.index_array[ind2][0])
                if ind1 == ind2:
                    if self.new_area[j_ind1][i_ind1] == 2:
                        array_neubour = []
                        for k in range(-1, 2):
                            for l in range(-1, 2):
                                if not (k == 0 and l == 0):
                                    if 0 <= j_ind1 + k < self.count_nodes_y and 0 <= i_ind1 + l < self.count_nodes_x and \
                                            self.new_area[j_ind1 + k][i_ind1 + l] in [2]:
                                        array_neubour.append([j_ind1 + k, i_ind1 + l])

                        value = 0
                        print(array_neubour)
                        for elem_index in array_neubour:
                            k_ch = 0
                            if elem_index[0] == j_ind1 and abs(elem_index[1] - i_ind1) == 1:
                                k_ch += 1
                                value += 1 / 3 * self.step_on_area_y
                            if elem_index[1] == i_ind1 and abs(elem_index[0] - j_ind1) == 1:
                                k_ch += 1
                                value += 1 / 3 * self.step_on_area_y
                            # if abs(elem_index[0] - j_ind1) == 1 and abs(elem_index[1] - i_ind1) == 1:
                            #     k_ch += 1
                            #     # value += 1 / 8 * self.step_on_area_y**2
                            # # #     # value += (np.sqrt(2) * (self.step_on_area_y ** 5) / 5+0.05)*2
                            #     value += np.sqrt(2) * (self.step_on_area_y) / 5
                            # if k_ch != 1:
                            #     print("AAAA ERRROR")
                        self.M[ind1][ind2] = value

                k_ch = 0
                if abs(i_ind1 - i_ind2) == 1 and abs(j_ind1 - j_ind2) == 0:
                    if self.new_area[j_ind1][i_ind1] == 2 and self.new_area[j_ind2][i_ind2] in [2]:
                        k_ch += 1
                        self.M[ind1][ind2] = 1 / 6 * self.step_on_area_x
                if abs(i_ind1 - i_ind2) == 0 and abs(j_ind1 - j_ind2) == 1:
                    if self.new_area[j_ind1][i_ind1] == 2 and self.new_area[j_ind2][i_ind2] in [2]:
                        k_ch += 1
                        self.M[ind1][ind2] = 1 / 6 * self.step_on_area_y
                # if abs(i_ind1 - i_ind2) == 1 and abs(j_ind1 - j_ind2) == 1:
                #     if self.new_area[j_ind1][i_ind1] == 2 and self.new_area[j_ind2][i_ind2] in [2]:
                #         k_ch += 1
                #         self.M[ind1][ind2] = (self.step_on_area_x)  / (15 * np.sqrt(2))
                # self.M[ind1][ind2] = (1 / (15 * np.sqrt(2)) * (self.step_on_area_x) ** 5+0.12)*10
                # self.M[ind1][ind2] = 1 / 20 * (self.step_on_area_x)**2
            file1.write(str(self.M[ind1]) + " ")
            file1.write(str("AAAA") + " ")
            file1.write("\n ")
        self.A = np.array([np.zeros(size_matrix_A) for _ in range(size_matrix_A)])
        file2 = open('A.txt', 'w')
        list_need_value = [1, 2]
        for ind1 in range(size_matrix_A):
            for ind2 in range(size_matrix_A):
                i_ind1 = int(self.index_array[ind1][1])
                j_ind1 = int(self.index_array[ind1][0])
                i_ind2 = int(self.index_array[ind2][1])
                j_ind2 = int(self.index_array[ind2][0])
                if ind1 == ind2:
                    value = 0
                    if j_ind1 - 1 >= 0 and i_ind1 - 1 >= 0 and \
                            self.new_area[j_ind1 - 1][i_ind1 - 1] in list_need_value and \
                            self.new_area[j_ind1 - 1][i_ind1] in list_need_value and \
                            self.new_area[j_ind1][i_ind1 - 1] in list_need_value and \
                            self.new_area[j_ind1][i_ind1] in list_need_value:
                        value += 2 / 3
                    # elif j_ind1 - 1 >= 0 and i_ind1 - 1 >= 0 and \
                    #         self.new_area[j_ind1 - 1][i_ind1 - 1] in list_need_value and \
                    #         (self.new_area[j_ind1 - 1][i_ind1] in list_need_value or
                    #          self.new_area[j_ind1][i_ind1 - 1] in list_need_value) and \
                    #         self.new_area[j_ind1][i_ind1] in list_need_value:
                    #     value += 1 / 3
                    # elif j_ind1 - 1 >= 0 and i_ind1 - 1 >= 0 and \
                    #         self.new_area[j_ind1 - 1][i_ind1] in list_need_value and \
                    #         self.new_area[j_ind1][i_ind1 - 1] in list_need_value and \
                    #         self.new_area[j_ind1][i_ind1] in list_need_value:
                    #     value += 1 / 2

                    if j_ind1 - 1 >= 0 and i_ind1 + 1 < self.count_nodes_x and \
                            self.new_area[j_ind1 - 1][i_ind1 + 1] in list_need_value and \
                            self.new_area[j_ind1 - 1][i_ind1] in list_need_value and \
                            self.new_area[j_ind1][i_ind1 + 1] in list_need_value and \
                            self.new_area[j_ind1][i_ind1] in list_need_value:
                        value += 2 / 3
                    # elif j_ind1 - 1 >= 0 and i_ind1 + 1 < self.count_nodes_x and \
                    #         self.new_area[j_ind1 - 1][i_ind1 + 1] in list_need_value and \
                    #         (self.new_area[j_ind1 - 1][i_ind1] in list_need_value or
                    #          self.new_area[j_ind1][i_ind1 + 1] in list_need_value) and \
                    #         self.new_area[j_ind1][i_ind1] in list_need_value:
                    #     value += 1 / 3
                    # elif j_ind1 - 1 >= 0 and i_ind1 + 1 < self.count_nodes_x and \
                    #         self.new_area[j_ind1 - 1][i_ind1] in list_need_value and \
                    #         self.new_area[j_ind1][i_ind1 + 1] in list_need_value and \
                    #         self.new_area[j_ind1][i_ind1] in list_need_value:
                    #     value += 1 / 2

                    if j_ind1 + 1 < self.count_nodes_y and i_ind1 + 1 < self.count_nodes_x and \
                            self.new_area[j_ind1 + 1][i_ind1 + 1] in list_need_value and \
                            self.new_area[j_ind1 + 1][i_ind1] in list_need_value and \
                            self.new_area[j_ind1][i_ind1 + 1] in list_need_value and \
                            self.new_area[j_ind1][i_ind1] in list_need_value:
                        value += 2 / 3
                    # elif j_ind1 + 1 < self.count_nodes_y and i_ind1 + 1 < self.count_nodes_x and \
                    #         self.new_area[j_ind1 + 1][i_ind1 + 1] in list_need_value and \
                    #         (self.new_area[j_ind1 + 1][i_ind1] in list_need_value or
                    #          self.new_area[j_ind1][i_ind1 + 1] in list_need_value) and \
                    #         self.new_area[j_ind1][i_ind1] in list_need_value:
                    #     value += 1 / 3
                    # elif j_ind1 + 1 < self.count_nodes_y and i_ind1 + 1 < self.count_nodes_x and \
                    #         self.new_area[j_ind1 + 1][i_ind1] in list_need_value and \
                    #         self.new_area[j_ind1][i_ind1 + 1] in list_need_value and \
                    #         self.new_area[j_ind1][i_ind1] in list_need_value:
                    #     value += 1 / 2

                    if j_ind1 + 1 < self.count_nodes_y and i_ind1 - 1 >= 0 and \
                            self.new_area[j_ind1 + 1][i_ind1 - 1] in list_need_value and \
                            self.new_area[j_ind1 + 1][i_ind1] in list_need_value and \
                            self.new_area[j_ind1][i_ind1 - 1] in list_need_value and \
                            self.new_area[j_ind1][i_ind1] in list_need_value:
                        value += 2 / 3
                    # elif j_ind1 + 1 < self.count_nodes_y and i_ind1 - 1 >= 0 and \
                    #         self.new_area[j_ind1 + 1][i_ind1 - 1] in list_need_value and \
                    #         (self.new_area[j_ind1 + 1][i_ind1] in list_need_value or
                    #          self.new_area[j_ind1][i_ind1 - 1] in list_need_value) and \
                    #         self.new_area[j_ind1][i_ind1] in list_need_value:
                    #     value += 1 / 3
                    # elif j_ind1 + 1 < self.count_nodes_y and i_ind1 - 1 >= 0 and \
                    #         self.new_area[j_ind1 + 1][i_ind1] in list_need_value and \
                    #         self.new_area[j_ind1][i_ind1 - 1] in list_need_value and \
                    #         self.new_area[j_ind1][i_ind1] in list_need_value:
                    #     value += 1 / 2

                    self.A[ind1][ind2] = value
                elif abs(i_ind1 - i_ind2) == 1 and abs(j_ind1 - j_ind2) == 0:
                    if i_ind1 < i_ind2:
                        i_index = i_ind1
                        j_index = j_ind1
                    else:
                        i_index = i_ind2
                        j_index = j_ind2
                    value = 0
                    if j_index - 1 >= 0 and j_index + 1 < self.count_nodes_y and i_index + 1 < self.count_nodes_x and \
                            self.new_area[j_index + 1][i_index] in list_need_value and \
                            self.new_area[j_index - 1][i_index] in list_need_value and \
                            self.new_area[j_index + 1][i_index + 1] in list_need_value and \
                            self.new_area[j_index - 1][i_index + 1] in list_need_value and \
                            self.new_area[j_index][i_index + 1] in list_need_value:
                        value += - 1 / 3
                    else:
                        if j_index + 1 < self.count_nodes_y and i_index + 1 < self.count_nodes_y and \
                                self.new_area[j_index + 1][i_index] in list_need_value and \
                                self.new_area[j_index + 1][i_index + 1] in list_need_value and \
                                self.new_area[j_index][i_index + 1] in list_need_value:
                            value += - 1 / 6
                        # elif j_index + 1 < self.count_nodes_y and i_index + 1 < self.count_nodes_x and \
                        #         ((self.new_area[j_index+1][i_index + 1] in list_need_value and
                        #           (self.new_area[j_index + 1][i_index] in list_need_value or
                        #          self.new_area[j_index][i_index + 1] in list_need_value)) or
                        #          (self.new_area[j_index + 1][i_index] in list_need_value and
                        #           self.new_area[j_index][i_index + 1] in list_need_value)):
                        #     value += - 1 / 6
                        if j_index - 1 >= 0 and i_index + 1 < self.count_nodes_x and \
                                self.new_area[j_index - 1][i_index] in list_need_value and \
                                self.new_area[j_index - 1][i_index + 1] in list_need_value and \
                                self.new_area[j_index][i_index + 1] in list_need_value:
                            value += - 1 / 6
                        # elif j_index - 1 >= 0 and i_index + 1 < self.count_nodes_x and \
                        #         ((self.new_area[j_index - 1][i_index + 1] in list_need_value and
                        #           (self.new_area[j_index - 1][i_index] in list_need_value or
                        #            self.new_area[j_index][i_index + 1] in list_need_value)) or
                        #          (self.new_area[j_index - 1][i_index] in list_need_value and
                        #           self.new_area[j_index][i_index + 1] in list_need_value)):
                        #     value += - 1 / 6
                    self.A[ind1][ind2] = value
                elif abs(i_ind1 - i_ind2) == 0 and abs(j_ind1 - j_ind2) == 1:
                    if j_ind1 < j_ind2:
                        i_index = i_ind1
                        j_index = j_ind1
                    else:
                        i_index = i_ind2
                        j_index = j_ind2
                    value = 0
                    if i_index - 1 >= 0 and i_index + 1 < self.count_nodes_y and \
                            self.new_area[j_index][i_index + 1] in list_need_value and \
                            self.new_area[j_index][i_index - 1] in list_need_value and \
                            self.new_area[j_index + 1][i_index + 1] in list_need_value and \
                            self.new_area[j_index + 1][i_index - 1] in list_need_value and \
                            self.new_area[j_index + 1][i_index] in list_need_value:
                        value += - 1 / 3
                    else:
                        if j_index + 1 < self.count_nodes_y and i_index + 1 < self.count_nodes_x and \
                                self.new_area[j_index][i_index + 1] in list_need_value and \
                                self.new_area[j_index + 1][i_index + 1] in list_need_value and \
                                self.new_area[j_index + 1][i_index] in list_need_value:
                            value += - 1 / 6
                        # elif j_index + 1 < self.count_nodes_y and i_index + 1 < self.count_nodes_x and \
                        #         ((self.new_area[j_index + 1][i_index + 1] in list_need_value and
                        #           (self.new_area[j_index][i_index + 1] in list_need_value or
                        #            self.new_area[j_index + 1][i_index] in list_need_value)) or
                        #          (self.new_area[j_index][i_index + 1] in list_need_value and
                        #           self.new_area[j_index + 1][i_index] in list_need_value)):
                        #     value += - 1 / 6
                        if i_index - 1 >= 0 and j_index + 1 < self.count_nodes_y and \
                                self.new_area[j_index][i_index - 1] in list_need_value and \
                                self.new_area[j_index + 1][i_index - 1] in list_need_value and \
                                self.new_area[j_index + 1][i_index] in list_need_value:
                            value += - 1 / 6
                        # elif i_index - 1 >= 0 and j_index + 1 < self.count_nodes_y and \
                        #         ((self.new_area[j_index + 1][i_index - 1] in list_need_value and
                        #           (self.new_area[j_index][i_index - 1] in list_need_value or
                        #            self.new_area[j_index + 1][i_index] in list_need_value)) or
                        #          (self.new_area[j_index][i_index - 1] in list_need_value and
                        #           self.new_area[j_index + 1][i_index] in list_need_value)):
                        #     value += - 1 / 6
                    self.A[ind1][ind2] = value
                elif abs(i_ind1 - i_ind2) == 1 and abs(j_ind1 - j_ind2) == 1:
                    if j_ind1 > j_ind2:
                        j_index = j_ind2
                    else:
                        j_index = j_ind1
                    if i_ind2 < i_ind1:
                        i_index = i_ind2
                    else:
                        i_index = i_ind1
                    if self.new_area[j_index][i_index] in list_need_value and \
                            self.new_area[j_index + 1][i_index] in list_need_value and \
                            self.new_area[j_index + 1][i_index + 1] in list_need_value and \
                            self.new_area[j_index][i_index + 1] in list_need_value:
                        self.A[ind1][ind2] = -1 / 3
                    # elif self.new_area[j_ind1][i_ind1] in list_need_value and \
                    #         self.new_area[j_ind2][i_ind2] in list_need_value and \
                    #         (self.new_area[j_index + 1][i_index] in list_need_value or
                    #          self.new_area[j_index][i_index + 1] in list_need_value):
                    #     self.A[ind1][ind2] = -1 / 6

                file2.write(str(self.A[ind1][ind2]) + " ")
            file2.write("\n ")

    def random_vector(self):
        start_vector = []
        for i in range(self.count):
            start_vector.append([random.uniform(self.min_value_start_function, self.max_value_start_function)])
        return np.array(start_vector)

    def building_matrix(self):
        pass

    def find_element(self, j, i):
        for k in range(self.count):
            if self.index_array[k][0] == j and self.index_array[k][1] == i and self.new_area[j][i] in [1]:
                return k
        return -1

    def plot_vectors(self):
        x_area = np.linspace(self.start_area_x, self.finish_area_x, self.count_nodes_x)
        y_area = np.linspace(self.start_area_y, self.finish_area_y, self.count_nodes_y)
        X, Y = np.meshgrid(x_area, y_area)
        count = int(np.ceil(len(self.array_final_vectors)/4))
        fig_array = []
        for s in range(count):
            figure = plt.figure()
            for k in range(4):
                if (s*4+k) >= len(self.array_final_vectors):
                    break
                ax = figure.add_subplot(2, 2, (k % 4)+1,
                                        projection='3d')
                plt_vector = np.array([np.zeros(self.count_nodes_x) for _ in range(self.count_nodes_y)])
                for j in range(self.count_nodes_y):
                    for i in range(self.count_nodes_x):
                        index = self.find_element(j, i)
                        if index != -1:
                            plt_vector[j][i] = self.array_final_vectors[s*4+k].T[0][index]
                        else:
                            plt_vector[j][i] = None
                if k == 0 and s==0:
                    plt_vector = np.round(plt_vector, 2)
                scat = ax.plot_surface(X, Y, plt_vector, cmap="plasma")
                ax.set_xlabel('X')
                ax.set_ylabel('Y')
                ax.set_zlabel('Z')
                ax.set_title("Функция задачи Стеклова №" + str(
                    k + 1) + "\n" + f"\u03BB={np.abs(float(np.round(self.get_eigenvalue(self.array_final_vectors[s*4+k]), 3)))}",
                             fontsize=12)
                plt.colorbar(scat, fraction=0.02, pad=0.05)
                plt.gca().invert_yaxis()
                ax.view_init(20, 60)
            fig_array.append((figure, ax))
        return fig_array

    def generate_grid_value(self):
        grid_values = [10]
        current_grid_value = 10
        while current_grid_value * 2 <= min(self.count_nodes_x, self.count_nodes_y) / 2:
            current_grid_value *= 2
            grid_values.append(current_grid_value)
        grid_values.append(min(self.count_nodes_x, self.count_nodes_y))
        return grid_values

    def bootstrapping(self):
        grid_values = self.generate_grid_value()

        for iter_grid_value in range(len(grid_values)):
            self.preparing_area()
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
                print("Q", i, self.get_eigenvalue(final_vector))
                final_vector = final_vector / np.linalg.norm(final_vector)
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

    def alg_process(self):
        # self.read_area()
        self.preparing_area()
        start_vector = self.generate_start_function_nodes()
        for i in range(self.count_functions):
            final_vector, log, koef_r = self.rayleigh_quotient_algorithm(start_vector, self.array_final_vectors)
            final_vector = final_vector / np.linalg.norm(final_vector)
            print("Q", self.get_eigenvalue(final_vector))
            self.array_start_vectors.append(start_vector)
            if all(np.abs(np.dot(final_vector.T, col)) < 10e-9 for col in self.array_final_vectors):
                print("Success")
            else:
                print("Failure")
            self.array_final_vectors.append(final_vector)
            start_vector = self.find_orth_start_vector(final_vector, self.array_orth_start_vectors)
            start_vector = start_vector / np.linalg.norm(start_vector)
            self.array_orth_start_vectors.append(list(final_vector.T[0]))
        return self.plot_vectors()
