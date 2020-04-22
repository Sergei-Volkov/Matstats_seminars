# -*- coding: cp65001 -*-
import typing
import numpy as np


def generate_brownian(sigma: typing.Union[int, float, complex] = 1,
                      *,
                      n_proc: int = 10,
                      n_dims: int = 2,
                      n_steps: int = 100) -> np.ndarray:
    """
    :param sigma:    стандартное отклонение нормального распределения,
                     генерирующего пошаговые смещения координат
                     
    :param n_proc:   число процессов для генерации (количество различных частиц)
    
    :param n_dims:   количество пространственных измерений для генерации процесса
    
    :param n_steps:  количество последовательных изменений координат (шагов), приходящихся на один процесс

    :return:         np.ndarray размера (n_proc, n_dims, n_steps), содеражащий на позиции
                     [i,j,k] значение j-й координаты i-й частицы на k-м шаге.
    """
    if not np.issubdtype(type(sigma), np.number):
        raise TypeError("Параметр 'sigma' должен быть числом")
    # Для кандидатов в отличники: <ДОПИСАТЬ ПРОВЕРКИ ТИПОВ>
    
    for par in [n_proc, n_dims, n_steps]:  # проверка типов данных
        if not np.issubdtype(type(par), np.number):
            raise TypeError("Параметр '{}' должен быть числом".format(par))
    
    result = np.random.normal(0, sigma**2, (n_proc, n_dims, n_steps - 1))  # генерируем случайные приращения координат
    result = np.concatenate([result, np.zeros((n_proc, n_dims, 1))], axis=2)  # начальные координаты - нули
    result = np.cumsum(result, axis=2)  # считаем координаты частиц на каждом шаге

    return result
