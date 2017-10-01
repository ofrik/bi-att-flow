from squad.demo_prepro import prepro
from basic.demo_cli import Demo
from evaluate_script import get_score
import json
import pandas as pd


class QuestionAnswerer(object):
    demo = Demo()

    def getAnswer(self, paragraph, question):
        pq_prepro = prepro(paragraph, question)
        if len(pq_prepro['x']) > 1000:
            return "[Error] Sorry, the number of words in paragraph cannot be more than 1000."
        if len(pq_prepro['q']) > 100:
            return "[Error] Sorry, the number of words in question cannot be more than 100."
        answer = self.demo.run(pq_prepro)
        return answer

    def evaluate(self, paragraphs, questions, real_answers):
        scores = []
        answers = []
        assert len(paragraphs) == len(questions)
        assert len(paragraphs) == len(real_answers)
        score = None
        for question, paragraph, answer in zip(questions, paragraphs, real_answers):
            pq_prepro = prepro(paragraph, question)
            if len(pq_prepro['x']) > 1000:
                return "[Error] Sorry, the number of words in paragraph cannot be more than 1000."
            if len(pq_prepro['q']) > 100:
                return "[Error] Sorry, the number of words in question cannot be more than 100."
            model_answer = self.demo.run(pq_prepro)
            if answer is not None:
                score = get_score(model_answer, [answer])
            answers.append(model_answer)
            scores.append(score)
        return answers, scores


if __name__ == "__main__":
    qa = QuestionAnswerer()
    # df = pd.read_csv("data/squad/processed_data.csv")
    # short_df = df[:10]
    # print(qa.evaluate(short_df["p"], short_df["q"], short_df["a"]))
    paragraph = input("Enter the paragraph:")
    while paragraph is not None and not paragraph == "":
        question = input("Enter a question:")
        while question is not None and not question == "":
            answer = qa.getAnswer(paragraph, question)
            print("The answer is: {}".format(answer))
            question = input("Enter a question:")
        paragraph = input("Enter the paragraph:")
