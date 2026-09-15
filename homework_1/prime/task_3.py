def is_prime(number: int) -> bool:
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def count_primes(limit: int) -> int:
    prime_count = 0
    for number in range(2, limit):
        if is_prime(number):
            prime_count += 1

    return prime_count


def main() -> None:
    print("Введите целое число N и нажмите Enter:")
    limit = int(input())
    print(count_primes(limit))


if __name__ == "__main__":
    main()
