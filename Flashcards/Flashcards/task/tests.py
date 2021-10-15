from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
from typing import List


CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)

right_answer_keyword = "right"
wrong_answer_keyword = "wrong"


class FlashcardsTest(StageTest):

    def generate(self) -> List[TestCase]:
        return [TestCase(stdin="a purring animal\ncat\ncat", attach=[right_answer_keyword, wrong_answer_keyword]),
                TestCase(stdin="a purring animal\ncat\n????\n", attach=[wrong_answer_keyword, right_answer_keyword]),
                TestCase(stdin="a barking animal\ndog\ncat\n", attach=[wrong_answer_keyword, right_answer_keyword]),
                TestCase(stdin="a barking animal\ndog\ndog\n", attach=[right_answer_keyword, wrong_answer_keyword])]

    def check(self, reply: str, attach: str) -> CheckResult:
        lines_n = 1
        right_output, wrong_output = attach
        right_output = right_output.strip()
        wrong_output = wrong_output.strip()
        reply = reply.lower().strip().split('\n')
        reply_lines_n = len(reply)

        if reply_lines_n != lines_n:
            return CheckResult.wrong("Your program outputs {0} line{1}, "
                                     "while {2} line{3} was expected".format(reply_lines_n,
                                                                             's' if reply_lines_n != 1 else '',
                                                                             lines_n,
                                                                             's' if lines_n != 1 else ''))

        if right_output not in reply[0]:
            return CheckResult.wrong("\"{}\" word was expected, "
                                     "but wasn't found in the output of your program".format(right_output))
        if wrong_output in reply[0]:
            return CheckResult.wrong("\"{}\" word was not expected, "
                                     "but was found in the output of your program".format(wrong_output))

        return CheckResult.correct()


if __name__ == "__main__":
    FlashcardsTest("flashcards.flashcards").run_tests()
