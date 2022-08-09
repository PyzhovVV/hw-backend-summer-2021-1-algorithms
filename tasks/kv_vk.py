from typing import TypeVar

__all__ = (
    'flip_kv_vk',
    'flip_kv_vk_safe',
)


KT = TypeVar('KT')
KV = TypeVar('KV')


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    """
    Функция должна возвращать словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - ключи.
    Например,
    flip_kv_vk({
        'tokyo': 'Токио',
        'moscow': 'Москва',
    }) == {
        'Токио': 'tokyo',
        'Москва': 'moscow',
    }
    """
    new_dict = {}
    for i in d.items():
        new_dict[i[1]] = i[0]
    return new_dict


def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    """
    Функция должна возвращать словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - массив ключей конфликтующих
    значений.
    Например,
    flip_kv_vk({
        'Санкт-Петербург': '+3',
        'Москва': '+3',
    }) == {
        '+3': ['Москва', 'Санкт-Петербург'],
    }
    """
    if d:
        new_dict = {}
        tuple_values = tuple(d.values())
        tuple_keys = tuple(d.keys())
        new_dict[tuple_values[0]] = [tuple_keys[0], ]
        for i in range(1, len(tuple_values)):
            if tuple_values[i] == tuple_values[i - 1]:
                new_dict[tuple_values[i]].append(tuple_keys[i])
            else:
                new_dict[tuple_values[i]] = [tuple_keys[i], ]
        return new_dict
    return {}
