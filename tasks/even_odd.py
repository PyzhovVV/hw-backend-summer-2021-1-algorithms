__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    sum_even = 0
    sum_odd = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            sum_even += arr[i]
        else:
            sum_odd += arr[i]
    return sum_even/sum_odd if sum_odd else 0
