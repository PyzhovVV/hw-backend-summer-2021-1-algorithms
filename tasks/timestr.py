__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    second = seconds % 60
    minutes = seconds // 60 % 60
    hours = seconds // 3600 % 24
    days = seconds // 86400 % 365
    if days:
        return f'{days:0>2d}d{hours:0>2d}h{minutes:0>2d}m{second:0>2d}s'
    elif hours:
        return f'{hours:0>2d}h{minutes:0>2d}m{second:0>2d}s'
    elif minutes:
        return f'{minutes:0>2d}m{second:0>2d}s'
    else:
        return f'{second:0>2d}s'
