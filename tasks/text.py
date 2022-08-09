from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    splited = text.split()
    if splited:
        longest = max(splited, key=len)
        shortest = min(splited, key=len)
        return (shortest, longest) if longest and shortest and longest != shortest else (None, None)
    return None, None

