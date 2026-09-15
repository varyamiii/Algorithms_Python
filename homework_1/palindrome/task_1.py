def is_palindrome(number: int) -> bool:
    if number < 0:
        return False

    original_number = number
    reversed_number = 0

    while number > 0:
        last_digit = number % 10
        reversed_number = reversed_number * 10 + last_digit
        number //= 10

    return original_number == reversed_number


def main() -> None:
    print("Введите целое положительное число и нажмите Enter:")
    number = int(input())
    print(is_palindrome(number))


if __name__ == "__main__":
    main()
