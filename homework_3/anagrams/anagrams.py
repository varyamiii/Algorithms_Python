from typing import Dict, List, Tuple


def group_anagrams(words: List[str]) -> List[List[str]]:
    """Группирует слова, состоящие из одинаковых наборов символов."""
    groups_by_signature: Dict[Tuple[str, ...], List[str]] = {}

    for word in words:
        signature = tuple(sorted(word))
        if signature not in groups_by_signature:
            groups_by_signature[signature] = []
        groups_by_signature[signature].append(word)

    return list(groups_by_signature.values())


def main() -> None:
    print("Введите слова через пробел и нажмите Enter:")
    words = input().split()
    print(group_anagrams(words))


if __name__ == "__main__":
    main()
