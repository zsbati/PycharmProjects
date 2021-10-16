from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
from typing import List


CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)

right_keyword = "correct"
wrong_keyword = "wrong"

class CardsClue(object):

    def __init__(self, card_names, definitions, answers):
        self.cards_n = len(card_names)
        self.input = [str(self.cards_n)]
        self.input += ["{0}\n{1}".format(card_name, definitions[i])
                       for i, card_name in enumerate(card_names)]
        self.input += [answer for answer in answers]
        self.input = '\n'.join(self.input)
        self.output = [str(self.cards_n)]
        self.output += ["Input the number of cards:"]
        self.output += ["The term for card #{0}\nThe definition for card #{1}".format(i + 1, i + 1) for i in range(len(card_names))]
        self.output += ["Print the definition of \"{0}\"\n" \
                        "{1}".format(card_name, self.check_answer(answers[i], definitions[i]))
                        for i, card_name in enumerate(card_names)]
        self.output = '\n'.join(self.output)

    def check_answer(self, answer, definition):
        if answer == definition:
            return right_keyword
        else:
            return "{0}\t{1}".format(wrong_keyword, definition)


class FlashcardsTest(StageTest):

    def generate(self) -> List[TestCase]:
        test_cases = [CardsClue(card_names=["black", "white"],
                                definitions=["white", "black"],
                                answers=["white", "blue"]),
                      CardsClue(card_names=["a", "2", "3", "4", "5"],
                                definitions=["a", "2", "3", "4", "5"],
                                answers=["a", "2", "3", "4", "5"]),
                      CardsClue(card_names=["1", "2", "3", "4", "5"],
                                definitions=["1", "2", "3", "4", "5"],
                                answers=["5", "4", "3", "2", "1"]),
                      CardsClue(card_names=["11", "12", "13", "14"],
                                definitions=["21", "22", "23", "24"],
                                answers=["21", "22", "333333", "34"]),
                      CardsClue(card_names=["a brother of one's parent",
                                            "a part of the body where the foot and the leg meet"],
                                definitions=["uncle", "ankle"],
                                answers=["ankle", "??"])]

        return [TestCase(stdin=test_case.input, attach=test_case.output) for test_case in test_cases]

    def check(self, reply: str, attach: str) -> CheckResult:
        attach = attach.strip().split('\n')
        cards_n = int(attach[0])
        attach = attach[1:]
        lines_n = len(attach)
        reply = reply.strip().split('\n')
        reply_lines_n = len(reply)

        if reply_lines_n < lines_n:
            return CheckResult.wrong("Your program outputs {0} line{1}, "
                                     "while at least {2} line{3} was expected.\n"
                                     "Make sure the formatting of your program matches the example.".format(reply_lines_n,
                                                                                      's' if reply_lines_n != 1 else '',
                                                                                      lines_n,
                                                                                      's' if lines_n != 1 else ''))

        if attach[0].lower().strip() not in reply[0].lower().strip():
            return CheckResult.wrong("\"{0}\" is supposed to be the first line of your program, "
                                     "however, your program outputs \"{1}\" instead".format(attach[0], reply[0]))

        adding_cards_reply = reply[1:cards_n * 2 + 1]
        adding_cards_attach = attach[1:cards_n * 2 + 1]

        for i, attach_line in enumerate(adding_cards_attach):
            if attach_line.lower().strip() not in adding_cards_reply[i].lower().strip():
                return CheckResult.wrong("An error occurred while cards were being added. \n"
                                         "Your program was supposed to output the line \"{0}\", \n"
                                         "but the line \"{1}\" was printed instead. \n"
                                         "Check the punctuation, "
                                         "also make sure that the card's number is correct.".format(attach_line,
                                                                                                    adding_cards_reply[i]))

        check_cards_reply = reply[cards_n * 2 + 1:]
        check_cards_attach = attach[cards_n * 2 + 1:]

        for i, attach_line in enumerate(check_cards_attach):
            reply_line = check_cards_reply[i]
            if i % 2 == 0:
                if attach_line.lower().strip() not in reply_line.lower().strip():
                    return CheckResult.wrong("An error occurred while the user's knowledge of cards was tested. \n"
                                             "Your program was supposed to output the line \"{0}\", \n"
                                             "but the line \"{1}\" was printed instead. \n"
                                             "Check the punctuation, "
                                             "also make sure that you ask the definitions in the correct order.".format(attach_line,
                                                                                                        reply_line))
            else:
                if wrong_keyword in attach_line:
                    right_output, correct_definition = attach_line.split('\t')
                    wrong_output = right_keyword
                else:
                    right_output = right_keyword
                    wrong_output = wrong_keyword

                right_output = right_output.lower().strip()
                wrong_output = wrong_output.lower().strip()

                if right_output not in reply_line.lower().strip() or wrong_output in reply_line.lower().strip():
                    return CheckResult.wrong("The user's answer is {0}, "
                                             "but the printed line doesn't contain the word \"{1}\" or contains the word \"{2}\":\n"
                                             "\"{3}\"".format(right_output, right_output, wrong_output, reply_line))

                if wrong_keyword in attach_line and correct_definition.lower().strip() not in reply_line.lower().strip():
                    return CheckResult.wrong("If the user's answer is wrong, "
                                             "the right definition should be printed.\n"
                                             "The definition \"{0}\" was expected, \n"
                                             "but it was not found in the line \"{1}\"".format(correct_definition,
                                                                                               reply_line))

        return CheckResult.correct()


if __name__ == "__main__":
    FlashcardsTest("flashcards.flashcards").run_tests()
