from abc import ABC, abstractmethod
import numpy as np
from scipy import linalg


class AlgorithmFindingEigenfunctions(ABC):
    def __init__(self, count_functions, count_nodes_x, start_area_x, finish_area_x, count_nodes_y=None,
                 start_area_y=None,
                 finish_area_y=None, tol=0.001):
        self.M = None
        self.A = None
        self.step_on_area_x = None
        self.step_on_area_y = None
        self.count_functions = count_functions
        self.count_nodes_x = count_nodes_x
        self.start_area_x = start_area_x
        self.finish_area_x = finish_area_x
        self.count_nodes_y = count_nodes_y
        self.start_area_y = start_area_y
        self.finish_area_y = finish_area_y
        self.tol = tol
        self.min_value_start_function = 0
        self.max_value_start_function = 1
        self.array_start_vectors = []
        self.array_final_vectors = []
        self.array_orth_start_vectors = []
        # self.f = open('rayl1.txt', 'w')
        # self.f1 = open('rayl2.txt', 'w')
        # self.f2 = open('rayl3.txt', 'w')

    @abstractmethod
    def random_vector(self):
        pass

    @abstractmethod
    def building_matrix(self):
        pass

    @abstractmethod
    def plot_vectors(self):
        pass

    def generate_start_function_nodes(self):
        start_function_nodes = self.random_vector()
        start_function_nodes = start_function_nodes / np.linalg.norm(start_function_nodes)
        return start_function_nodes

    def get_eigenvalue(self, x):
        return (np.dot(np.transpose(x), np.dot(self.A, x)) / np.dot(np.transpose(x), np.dot(self.M, x)))[0][0]

    def find_orth_start_vector(self, last_find_vector, array_start_vectors):
        last_find_vector = last_find_vector.T[0]
        new_array = []
        for el in array_start_vectors:
            new_array.append(el)
        new_array.append(last_find_vector)
        tmp_array_start_vectors = new_array
        matrix_for_orth = np.matrix(tmp_array_start_vectors).T
        new_start_vector = [self.find_orth_vector(matrix_for_orth)]
        new_start_vector = np.array([new_start_vector])
        new_start_vector = new_start_vector.reshape(-1, 1)
        new_start_vector = new_start_vector / np.linalg.norm(new_start_vector)
        return new_start_vector

    def find_orth_vector(self, orth_matrix):
        rand_vec = np.random.rand(orth_matrix.shape[0], 1)
        A = np.hstack((orth_matrix, rand_vec))
        b = np.zeros(orth_matrix.shape[1] + 1)
        b[-1] = 1
        return np.linalg.lstsq(A.T, b, rcond=-1)[0]

    def check_all_vectors(self, prev, cur):
        if not np.all(np.isclose(prev, cur, atol=0.005)):
            return True
        return False

    def check_step(self, p, eigen_vector1, iteration_number, rayleigh_quotient, galt, all_function, delta):
        eigen_vector = eigen_vector1 + delta * p
        if len(all_function) > 0:
            sum = 0
            for el in all_function:
                sum += np.dot(el,
                              np.dot(eigen_vector.T[0], el.T[0]) / np.dot(el.T[0], el.T[0]))
            eigen_vector = eigen_vector - sum
        eigen_vector = eigen_vector / np.linalg.norm(eigen_vector)
        if self.get_eigenvalue(eigen_vector) > self.get_eigenvalue(eigen_vector1):
            return False
        return True

    def rayleigh_quotient_algorithm(self, eigen_vector, all_function=[]):
        # self.M = np.asfortranarray(self.M)
        # self.A = np.asfortranarray(self.A)
        u1 = np.dot(self.M, eigen_vector)
        q = np.sqrt(np.dot(np.transpose(eigen_vector), u1))
        eigen_vector = eigen_vector / q
        u = u1 / q
        v = np.dot(self.A, eigen_vector)
        iteration_number = 0
        g = eigen_vector
        log = []
        koef_r = []
        rayleigh_quotient = np.dot(np.transpose(eigen_vector), v)
        gnorm = np.inf
        delta = np.inf
        last_eigen_vector = np.inf
        kf_r = self.get_eigenvalue(eigen_vector)
        k_s = (self.count_nodes_x**2)
        k_c = 0
        gnorm_min = gnorm
        gnorm_min_count = 0
        f = open('count.txt', 'w')
        while max(np.abs(last_eigen_vector-eigen_vector))>1e-14:
            k_c += 1
            iteration_number += 1
            galt = g
            g = 2 * (v - rayleigh_quotient * u)/q
            if iteration_number == 1:
                p = -g
            else:
                p = -g + np.dot(np.dot(np.transpose(g), self.M), g) / (np.dot(np.dot(np.transpose(galt), self.M), galt)) * p
            a = np.dot(np.transpose(np.hstack((eigen_vector, p))), np.hstack((v, np.dot(self.A, p))))
            b = np.dot(np.transpose(np.hstack((eigen_vector, p))), np.hstack((u, np.dot(self.M, p))))
            [ll, qq] = linalg.eig(a, b)
            ii = np.argmin(ll)
            rayleigh_quotient = ll[ii]
            if qq[0, ii] == 0:
                delta = 1e-8
            else:
                delta = qq[1, ii] / qq[0, ii]
            last_eigen_vector = eigen_vector
            check = self.check_step(p, eigen_vector, iteration_number, rayleigh_quotient, g, all_function, delta)
            if check==False:
                delta = delta * 0.05
            k_w = 10
            k_w_c = 0
            if check == False:
                while self.check_step(p, eigen_vector, iteration_number, rayleigh_quotient, g, all_function, delta) == False and k_w_c < k_w:
                    k_w_c +=1
                    delta = delta * 0.01
            eigen_vector = eigen_vector + delta * p

            if len(all_function) > 0:
                sum = 0
                for el in all_function:
                    sum += np.dot(el,
                                  np.dot(eigen_vector.T[0], el.T[0]) / np.dot(el.T[0], el.T[0]))
                eigen_vector = eigen_vector - sum
            eigen_vector = eigen_vector / np.linalg.norm(eigen_vector)
            u = np.dot(self.M, eigen_vector)
            q = np.sqrt(np.dot(np.transpose(eigen_vector), u))
            eigen_vector = eigen_vector / q
            u = u / q
            v = np.dot(self.A, eigen_vector)
            gnorm = np.linalg.norm(g)
            if gnorm_min == gnorm:
                gnorm_min_count += 1
            else:
                gnorm_min = np.min([gnorm_min, gnorm])
                gnorm_min_count = 0
            kf_r = self.get_eigenvalue(eigen_vector)
            koef_r.append(kf_r)
            log.append([iteration_number, rayleigh_quotient, gnorm])
        return (eigen_vector, log, koef_r)


    def alg_process(self):
        self.building_matrix()
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
        self.plot_vectors()
