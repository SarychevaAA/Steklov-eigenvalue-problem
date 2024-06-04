# Steklov-eigenvalue-problem

Созданная программа представляет собой десктопную программу, написанную на языке программирования Python, для нахождения собственных функций и чисел задачи Стеклова.

В рамках поставленной задачи, также были реализован код для нахождения собственных функций и чисел вспомогательных задач(задачи Дирихле и задачи Неймана).

## Математический пакет
Математический пакет реализован таким образом, что пользователь может получить графическое представление собственных функций всех задач на отрезке или прямоугольных областях, вызвав требуемый функционал данного пакета:
1. Получение спектра задачи Дирихле на отрезке:
```
alg = AlgorithmDirichlet1D(6, 30, 0, math.pi) # arguments (count_functions, count_nodes_x, start_area_x, finish_area_x)
alg.alg_process()
```
В результате будут получены первые 6 собственных функций задачи Дирихле, определенные в промежутке от 0 до $\pi$, при 30 узлах на выбранном отрезке:
![Снимок экрана от 2024-06-03 23-02-12](https://github.com/SarychevaAA/Steklov-eigenvalue-problem/assets/71674859/78bae261-7cf6-4839-b491-5166f0a79dc2)

2.  Получение спектра задачи Неймана на отрезке:
```
alg = AlgorithmNeumann1D(4, 60, 0, math.pi) # arguments (count_functions, count_nodes_x, start_area_x, finish_area_x)
alg.alg_process()
```
В результате будут получены первые 6 собственных функций задачи Неймана, определенные в промежутке от 0 до $\pi$, при 30 узлах на выбранном отрезке:
![image](https://github.com/SarychevaAA/Steklov-eigenvalue-problem/assets/71674859/a1d8433e-028f-43d5-a7d1-0428db862bb5)

3. Получение спектра задачи Дирихле на прямоугольнике:
```
alg = AlgorithmNeumann2D(6, 60, 0, 2*math.pi, 30, 0, math.pi)  # arguments (count_functions, count_nodes_x, start_area_x, finish_area_x, count_nodes_y, start_area_y, finish_area_y)
alg.alg_process()
```
В результате будут получены первые 6 собственных функций задачи Неймана, определенные в промежутке от 0 до $2*\pi$ по оси X и от 0 до $\pi$ по оси Y:
![image](https://github.com/SarychevaAA/Steklov-eigenvalue-problem/assets/71674859/9bdb157b-bbfa-4829-b848-da8aa16bba29)

4. Получение спектра задачи Неймана на прямоугольнике:
```
alg = AlgorithmNeumann2D(6, 20, 0, math.pi, 40, 0, 2*math.pi)  # arguments (count_functions, count_nodes_x, start_area_x, finish_area_x, count_nodes_y, start_area_y, finish_area_y)
alg.alg_process()
```
В результате будут получены первые 6 собственных функций задачи Неймана, определенные в промежутке от 0 до $\pi$ по оси X и от 0 до $2\pi$ по оси Y:
![image](https://github.com/SarychevaAA/Steklov-eigenvalue-problem/assets/71674859/4bab4918-03c9-4ed5-ba36-88c8b6d55b65)

5. Получение спектра задачи Стеклова на квадрате:
 ```
list_points = read_file("area.txt", 15, 0, math.pi, 15, 0, math.pi) # arguments (file_path, count_nodes_x, start_area_x, finish_area_x, count_nodes_y, start_area_y, finish_area_y)
alg = AlgorithmSteklov2D(6, 15, 0, math.pi, 15, 0, math.pi, list_points)
alg.alg_process()
```  
В результате будут получены первые 6 собственных функций задачи Стеклова, определенные в квадратной области от 0 до $\pi$:
![image](https://github.com/SarychevaAA/Steklov-eigenvalue-problem/assets/71674859/c72369e0-1d9c-459d-aebc-cadd1c0622ab)

## Программа
При использование программы можно получить собственные векторы и собственные числа задачи Стеклова, задав область разными способами:
1. Выбор области с помощью прямоугольного объекта:
2. 
   Опеделение основных параметров:
   
![image](https://github.com/SarychevaAA/Steklov-eigenvalue-problem/assets/71674859/e52d0062-6a52-450f-ae7a-607a132650b9)

   Выбор области дискретизации:

![image](https://github.com/SarychevaAA/Steklov-eigenvalue-problem/assets/71674859/42b9ad4c-503e-41d8-8799-98681705b7c4)

  Полученный результат:

![Снимок экрана от 2024-06-04 04-19-07](https://github.com/SarychevaAA/Steklov-eigenvalue-problem/assets/71674859/4c7c1ea5-0e4b-4a4a-b3f0-b26c8c4f5908)

![image](https://github.com/SarychevaAA/Steklov-eigenvalue-problem/assets/71674859/9472165b-d778-487f-9b8b-474a0cc9765d)

2. Выбор области с помощью файла:

   Опеделение основных параметров:
   
![image](https://github.com/SarychevaAA/Steklov-eigenvalue-problem/assets/71674859/49e00960-043e-4607-9b37-17981493a35e)
   
   Выбор области дискретизации:

![Снимок экрана от 2024-06-04 03-23-09-1](https://github.com/SarychevaAA/Steklov-eigenvalue-problem/assets/71674859/1c98e41e-6682-487d-bfbe-f8531763cd68)

  Полученный результат:

![image](https://github.com/SarychevaAA/Steklov-eigenvalue-problem/assets/71674859/7a1461ec-2e19-408b-8403-d2a01e2fac7f)

3. Выбор области с помощью кривой:

   Опеделение основных параметров:

![image](https://github.com/SarychevaAA/Steklov-eigenvalue-problem/assets/71674859/811a23ca-933f-4a15-bc02-b0161e73b058)
   
   Выбор области дискретизации:

![Снимок экрана от 2024-06-04 03-54-31](https://github.com/SarychevaAA/Steklov-eigenvalue-problem/assets/71674859/458b175b-6e27-4c47-b166-21f65ddd24f1)

  Полученный результат:
    
![image](https://github.com/SarychevaAA/Steklov-eigenvalue-problem/assets/71674859/c41ba864-b84a-4feb-aa7c-24f670abd944)

Еще один пример с помощью кривых:

  Опеделение основных параметров:
  
  ![image](https://github.com/SarychevaAA/Steklov-eigenvalue-problem/assets/71674859/3b72556b-fa59-42e4-8ff9-50bb35910339)


  Выбор области дискретизации:
  
![Снимок экрана от 2024-06-04 04-03-46](https://github.com/SarychevaAA/Steklov-eigenvalue-problem/assets/71674859/6f908122-c82d-4c8d-8cb7-186c7522e9b9)

  Полученный результат:

  ![Снимок экрана от 2024-06-04 04-05-11](https://github.com/SarychevaAA/Steklov-eigenvalue-problem/assets/71674859/5fb7eac4-80c1-41bf-986c-db5aa4630bc6)




