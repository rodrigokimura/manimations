from manim import (
    LEFT,
    RIGHT,
    UP,
    ApplyFunction,
    Arrow,
    Circumscribe,
    Code,
    Create,
    FadeOut,
    ShowPassingFlash,
    Text,
    Uncreate,
    Underline,
    VMobject,
    Write,
)
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

CODE_FIB = '''
def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


# Now call the function we just defined:
fib(2000)
'''.lstrip()

SAMPLE_NONE = """
>>> fib(0)
>>> print(fib(0))
None
""".lstrip()

CODE_FIB_2 = '''
def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a + b
    return result
'''.lstrip()


def bm(mark: str) -> str:
    return f"<bookmark mark='{mark}'/>"


class Main(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(transcription_model="base"))

        self.wait()
        with self.voiceover("Defining functions") as tracker:
            title = Text("Defining functions").scale(2)
            self.play(Write(title), run_time=tracker.duration)
            self.wait_for_voiceover()
            self.wait()

        def shift_and_scale(m: VMobject):
            m.shift(UP * 3)
            m.scale(0.5)
            return m

        self.play(ApplyFunction(shift_and_scale, title))

        code = Code(
            code=CODE_FIB,
            tab_width=4,
            language="python",
            style="monokai",
        )
        with self.voiceover(
            "We can create a function that writes the Fibonacci series to an arbitrary boundary."
        ) as tracker:
            self.play(
                Write(code),
                run_time=tracker.duration,
            )
            self.wait_for_voiceover()
            self.wait()

        with self.voiceover(
            "The keyword <bookmark mark='def'/>def introduces a function definition. "
        ) as tracker:
            def_keyword = code.code[0][0:3]
            self.wait_until_bookmark("def")
            self.play(Circumscribe(def_keyword))
            self.wait_for_voiceover()
            self.wait()

        with self.voiceover(
            "It must be followed by the function <bookmark mark='name'/>name "
            "and the parenthesized list of formal <bookmark mark='parameters'/>parameters. "
        ) as tracker:
            function_name = code.code[0][4:7]
            self.wait_until_bookmark("name")
            self.play(Circumscribe(function_name))

            parameters = code.code[0][7:10]
            self.wait_until_bookmark("parameters")
            self.play(Circumscribe(parameters))
            self.wait_for_voiceover()
            self.wait()

        with self.voiceover(
            "The <bookmark mark='statements'/>statements that form the body of the function "
            "<bookmark mark='end_explanation'/>start at the next line, "
            "and must be <bookmark mark='indent'/>indented."
        ) as tracker:
            statements = code.code[1:7]

            self.wait_until_bookmark("statements")
            self.play(
                Circumscribe(statements),
                run_time=tracker.time_until_bookmark("end_explanation"),
            )
            self.wait_until_bookmark("indent")
            arrows = [
                Arrow(start=LEFT, end=RIGHT).next_to(statement, direction=LEFT)
                for statement in statements
            ]
            self.play(*(Create(arrow) for arrow in arrows))
            self.wait()
            self.play(*(FadeOut(arrow) for arrow in arrows))
            self.wait_for_voiceover()

        with self.voiceover(
            "The first statement of the function body can optionally be a string literal <bookmark mark='end_first_sentence'/>; "
            "this string literal is the function’s documentation string, or docstring."
        ) as tracker:
            docstring = code.code[1]
            self.play(
                Circumscribe(docstring),
                run_time=tracker.time_until_bookmark("end_first_sentence"),
            )
            self.wait_for_voiceover()
            self.wait()

        with self.voiceover(
            "There are tools which use docstrings to automatically produce online "
            "or printed documentation, or to let the user interactively browse through code; "
            "it’s good practice to include docstrings in code that you write, "
            "so make a habit of it."
        ) as tracker:
            n = 10
            for _ in range(n):
                self.play(
                    ShowPassingFlash(Underline(docstring)),
                    run_time=tracker.duration / n,
                )
            self.wait_for_voiceover()
            self.wait()

        self.play(Uncreate(code))

        code = Code(
            code=SAMPLE_NONE,
            tab_width=4,
            language="pycon",
            style="monokai",
        )

        with self.voiceover(
            "Coming from other languages, you might object that fib is not a function "
            "but a procedure since it doesn’t return a value. "
            "In fact, even functions without a return statement do return a value, "
            "albeit a rather boring one. "
            "This value is called <bookmark mark='none'/>None (it’s a built-in name). "
            "Writing the value None, is normally suppressed by the interpreter, if it would be the only value written. "
            "You can see it, if you really want to, using <bookmark mark='print'/>print()."
        ) as tracker:
            self.play(Write(code), run_time=2)
            none = code.code[2]
            self.wait_until_bookmark("none")
            self.play(Circumscribe(none))
            print_call = code.code[1][4:9]
            self.wait_until_bookmark("print")
            self.play(Circumscribe(print_call))
            self.wait_for_voiceover()
            self.wait()

        code = Code(
            code=CODE_FIB_2,
            tab_width=4,
            language="python",
            style="monokai",
        )

        with self.voiceover(
            "It is simple to write a function that "
            f"{bm('return')}returns a list of the numbers of the Fibonacci series, "
            "instead of printing it."
        ) as tracker:
            self.play(Write(code))
            self.wait_until_bookmark("return")
            return_statement = code.code[-1][0:12]
            self.play(Circumscribe(return_statement))
            self.wait_for_voiceover()
            self.wait()

        with self.voiceover(
            "This example, as usual, demonstrates some new Python features. "
            f"The {bm('return')}return statement returns with a value from a function. "
            f"The statement with {bm('append')}'append' calls a method of the list object {bm('result')}'result'."
        ) as tracker:
            self.wait_until_bookmark("return")
            self.play(Circumscribe(return_statement))
            append = code.code[-3][0:18]
            result = code.code[-3][0:5]
            self.wait_until_bookmark("append")
            self.play(Circumscribe(append))
            self.wait_until_bookmark("result")
            self.play(Circumscribe(result))
            self.wait_for_voiceover()
            self.wait()

        self.wait()
