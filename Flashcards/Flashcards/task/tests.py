from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
from typing import List


CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)

right_keyword = "correct"
wrong_keyword = "wrong"


class Answer(object):

    def __init__(self, answer, is_correct, right_answer=None, is_def_for=None):
        self.answer = answer
        self.is_correct = is_correct
        self.right_answer = right_answer
        self.is_def_for = is_def_for


class CardsClue(object):

    def __init__(self, cards_n, card_names, definitions, answers):
        self.cards_n = cards_n
        self.input = [str(self.cards_n)]
        self.output = ["Input the number of cards"]
        self.cards = []
        self.definitions = set()

        for i in range(0, self.cards_n):
            got_card = False
            got_def = False
            self.output += ["The term for card #" + str(i + 1)]
            while not got_card:
                current_input = card_names[0]
                card_names.pop(0)
                self.input += [current_input]
                if current_input in self.cards:
                    self.output += ["The term \"{0}\" already exists".format(current_input)]
                else:
                    self.cards.append(current_input)
                    got_card = True
            self.output += ["The definition for card #" + str(i + 1)]
            while not got_def:
                current_input = definitions[0]
                definitions.pop(0)
                self.input += [current_input]
                if current_input in self.definitions:
                    self.output += ["The definition \"{0}\" already exists".format(current_input)]
                else:
                    self.definitions.add(current_input)
                    got_def = True

        lines_n = len(self.output)

        self.input += [answer.answer for answer in answers]
        self.output += ["Print the definition of \"{0}\"\n" \
                        "{1}".format(card, self.check_answer(answers[i]))
                        for i, card in enumerate(self.cards)]
        self.output += [str(lines_n)]
        self.output = '\n'.join(self.output)
        self.input = '\n'.join(self.input)

    def check_answer(self, answer: Answer):

        if answer.is_correct:
            return right_keyword
        else:
            return "{0}\t{1}{2}".format(wrong_keyword, answer.right_answer,
                                        "\t" + answer.is_def_for if answer.is_def_for else "")


class FlashcardsTest(StageTest):

    def generate(self) -> List[TestCase]:
        test_cases = [CardsClue(cards_n=2,
                                card_names=["black", "black", "red"],
                                definitions=["white", "white", "green"],
                                answers=[Answer("white", True), Answer("green", True)]),

                      CardsClue(cards_n=2,
                                card_names=["a brother of one's parent",
                                            "a part of the body where the foot and the leg meet"],
                                definitions=["uncle", "ankle"],
                                answers=[Answer("ankle",
                                                False, "uncle",
                                                "a part of the body where the foot and the leg meet"),
                                         Answer("???", False, "ankle")]),

                      CardsClue(cards_n=4,
                                card_names=["c1", "c2", "c3", "c1", "c2", "c3", "c4"],
                                definitions=["d1", "d2", "d3", "d1", "d2", "d3", "d4"],
                                answers=[Answer("d1", True),
                                         Answer("d1", False, "d2", "c1"),
                                         Answer("d3 ddd3", False, "d3"),
                                         Answer("???", False, "d4")])]

        return [TestCase(stdin=test_case.input, attach=test_case.output) for test_case in test_cases]

    def check(self, reply: str, attach: str) -> CheckResult:
        attach = attach.strip().split('\n')
        end_of_cards_input = int(attach[-1])
        attach = attach[:-1]
        lines_n = len(attach)
        reply = reply.strip().split('\n')
        reply_lines_n = len(reply)

        if reply_lines_n < lines_n:
            return CheckResult.wrong("Your program outputs {0} line{1}, "
                                     "while at least {2} line{3} was expected.\n"
                                     "Make sure the formatting of your program matches the example "
                                     "and that all the required messages are printed.\n".format(reply_lines_n,
                                                                                      's' if reply_lines_n != 1 else '',
                                                                                      lines_n,
                                                                                      's' if lines_n != 1 else ''))

        if attach[0].lower().strip() not in reply[0].lower().strip():
            return CheckResult.wrong("\"{0}\" is supposed to be the first line of your program, "
                                     "however, your program outputs \"{1}\" instead".format(attach[0], reply[0]))

        adding_cards_reply = reply[1:end_of_cards_input]
        adding_cards_attach = attach[1:end_of_cards_input]

        for i, attach_line in enumerate(adding_cards_attach):
            if attach_line.lower().strip() not in adding_cards_reply[i].lower().strip():
                if "exists" not in attach_line:
                    return CheckResult.wrong("An error occurred while cards were being added. \n"
                                             "Your program was supposed to output the line \"{0}\", \n"
                                             "but the line \"{1}\" was printed instead. \n"
                                             "Check the punctuation, "
                                             "also make sure that the card's number is correct.".format(attach_line,
                                                                                                    adding_cards_reply[i]))
                else:
                    return CheckResult.wrong("An error occurred while cards were being added. \n"
                                             "Your program was supposed to output the line \"{0}\", \n"
                                             "but the line \"{1}\" was printed instead. \n"
                                             "Check if your programs outputs the correct error message "
                                             "when the user tries to input a duplicate card or definition.".format(attach_line,
                                                                                                    adding_cards_reply[i]))

        check_cards_reply = reply[end_of_cards_input:]
        check_cards_attach = attach[end_of_cards_input:]

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
                    attach_line = attach_line.split('\t')
                    if len(attach_line) == 2:
                        attach_line, correct_answer = attach_line
                        correct_card = None
                    else:
                        attach_line, correct_answer, correct_card = attach_line

                if attach_line.lower().strip() not in reply_line.lower().strip():
                    return CheckResult.wrong("The user's answer is {0}, "
                                             "but the printed line doesn't contain the word \"{1}\":\n"
                                             "\"{2}\"".format(attach_line, attach_line, reply_line))

                if wrong_keyword in attach_line:
                    if correct_answer.lower().strip() not in reply_line.lower().strip():
                        return CheckResult.wrong("If the user's answer is wrong, "
                                                 "the right answer should be printed.\n"
                                                 "The definition \"{0}\" was expected, \n"
                                                 "but it was not found in the line \"{1}\"".format(correct_answer,
                                                                                                   reply_line))
                    if correct_card and correct_card.lower().strip() not in reply_line.lower().strip():
                        return CheckResult.wrong("When the user's definition is wrong for the requested term, "
                                                 "but correct for another term, your program should output "
                                                 "the name of the term for which the given definition is correct.\n"
                                                 "The name of the card \"{0}\" was expected, "
                                                 "but it was not found in the line\n"
                                                 "\"{1}\"".format(correct_card, reply_line))

        return CheckResult.correct()


if __name__ == "__main__":
    FlashcardsTest("flashcards.flashcards").run_tests()
