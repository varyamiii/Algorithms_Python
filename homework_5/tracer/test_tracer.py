import unittest
from contextlib import redirect_stdout
from io import StringIO

from homework_5.tracer.tracer import trace


class TracerTests(unittest.TestCase):
    def test_recursive_calls_have_matching_indentation_and_results(self) -> None:
        output = StringIO()

        @trace(stream=output)
        def factorial(number: int) -> int:
            if number <= 1:
                return 1
            return number * factorial(number - 1)

        self.assertEqual(factorial(3), 6)
        self.assertEqual(
            output.getvalue().splitlines(),
            [
                "-> factorial(3)",
                "  -> factorial(2)",
                "    -> factorial(1)",
                "    <- factorial = 1",
                "  <- factorial = 2",
                "<- factorial = 6",
            ],
        )

    def test_keyword_arguments_are_displayed(self) -> None:
        output = StringIO()

        @trace(stream=output, indent="....")
        def countdown(number: int, *, step: int) -> int:
            if number <= 0:
                return 0
            return countdown(number - step, step=step)

        self.assertEqual(countdown(2, step=1), 0)
        lines = output.getvalue().splitlines()
        self.assertEqual(lines[0], "-> countdown(2, step=1)")
        self.assertEqual(lines[1], "....-> countdown(1, step=1)")
        self.assertEqual(lines[2], "........-> countdown(0, step=1)")

    def test_exception_is_displayed_and_depth_is_restored(self) -> None:
        output = StringIO()

        @trace(stream=output)
        def fail(number: int) -> int:
            if number == 0:
                raise ValueError("zero")
            return fail(number - 1)

        with self.assertRaisesRegex(ValueError, "zero"):
            fail(1)
        with self.assertRaisesRegex(ValueError, "zero"):
            fail(0)

        lines = output.getvalue().splitlines()
        self.assertEqual(lines[-2], "-> fail(0)")
        self.assertEqual(lines[-1], "!! fail raised ValueError('zero')")

    def test_default_stream_uses_current_stdout(self) -> None:
        @trace
        def identity(value: int) -> int:
            return value

        output = StringIO()
        with redirect_stdout(output):
            self.assertEqual(identity(7), 7)

        self.assertIn("-> identity(7)", output.getvalue())
        self.assertIn("<- identity = 7", output.getvalue())

    def test_decorator_preserves_function_metadata(self) -> None:
        @trace(stream=StringIO())
        def documented() -> None:
            """Описание функции."""

        self.assertEqual(documented.__name__, "documented")
        self.assertEqual(documented.__doc__, "Описание функции.")


if __name__ == "__main__":
    unittest.main()
