"""Декоратор для визуализации стека рекурсивных вызовов."""

from contextvars import ContextVar
from functools import wraps
import sys
from typing import Any, Callable, TextIO, TypeVar, cast


Function = TypeVar("Function", bound=Callable[..., Any])
_stack_depth: ContextVar[int] = ContextVar("tracer_stack_depth", default=0)


def _format_arguments(args: tuple[Any, ...], kwargs: dict[str, Any]) -> str:
    parts = [repr(argument) for argument in args]
    parts.extend(f"{name}={value!r}" for name, value in kwargs.items())
    return ", ".join(parts)


def trace(
    function: Function | None = None,
    *,
    stream: TextIO | None = None,
    indent: str = "  ",
) -> Function | Callable[[Function], Function]:
    """Печатает вход и выход каждого вызова декорированной функции.

    Декоратор можно применять как ``@trace`` и как
    ``@trace(stream=output, indent="....")``. Если поток не передан, текущий
    ``sys.stdout`` выбирается непосредственно во время вызова. Благодаря этому
    декоратор корректно работает с ``redirect_stdout``.
    """

    def decorate(target: Function) -> Function:
        @wraps(target)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            depth = _stack_depth.get()
            padding = indent * depth
            output = stream if stream is not None else sys.stdout
            arguments = _format_arguments(args, kwargs)
            print(f"{padding}-> {target.__name__}({arguments})", file=output)

            token = _stack_depth.set(depth + 1)
            try:
                result = target(*args, **kwargs)
            except BaseException as error:
                print(
                    f"{padding}!! {target.__name__} raised {error!r}",
                    file=output,
                )
                raise
            else:
                print(
                    f"{padding}<- {target.__name__} = {result!r}",
                    file=output,
                )
                return result
            finally:
                _stack_depth.reset(token)

        return cast(Function, wrapper)

    if function is None:
        return decorate
    return decorate(function)


def main() -> None:
    @trace
    def factorial(number: int) -> int:
        if number <= 1:
            return 1
        return number * factorial(number - 1)

    print("Результат:", factorial(4))


if __name__ == "__main__":
    main()
