TYPE_AREA = {
    "0": "2D",
    "1": "3D"
}

TYPE_CONDITIONS = {
    "0": "Условие Дирихле",
    "1": "Условие Неймона",
    "2": "Условие Стеклова"
}

KOEF_MATRIX_M_2D_DIRICHLET = {
    "complete_intersection": 2 / 3,
    "partial_intersection": 1 / 6
}

KOEF_MATRIX_A_2D_DIRICHLET = {
    "complete_intersection": 2,
    "partial_intersection": -1
}

KOEF_MATRIX_M_2D_NEUMON = {
    "complete_intersection_border": 1 / 3,
    "complete_intersection": 2 / 3,
    "partial_intersection": 1 / 6,
}

KOEF_MATRIX_A_2D_NEUMON = {
    "complete_intersection_border": 1,
    "complete_intersection": 2,
    "partial_intersection": -1
}
