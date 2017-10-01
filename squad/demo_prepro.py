import argparse
import json
import os
import nltk
# data: q, cq, (dq), (pq), y, *x, *cx
# shared: x, cx, (dx), (px), word_counter, char_counter, word2vec
# no metadata
from collections import Counter

from tqdm import tqdm

from squad.utils import get_word_span, process_tokens, get_word_idx


def prepro(paragraph, question):
    data_type = 'demo'
    out_name = 'demo'

    sent_tokenize = lambda para: [para]  # nltk.sent_tokenize

    def word_tokenize(tokens):
        return [token.replace("''", '"').replace("``", '"') for token in nltk.word_tokenize(tokens)]

    q, cq, y, rx, rcx, ids, idxs = [], [], [], [], [], [], []
    cy = []
    x, cx = [], []
    answerss = []

    xi = [word_tokenize(paragraph)]
    cxi = [[list(xij) for xij in xi]]
    qi = word_tokenize(question)
    cqi = [list(qij) for qij in qi]
    yi = [[(0, 0), (0, 0)]]
    cyi = [[0, 0]]
    answers = []
    q.append(qi)
    cq.append(cqi)
    y.append(yi)
    cy.append(cyi)
    x.append(xi)
    cx.append(xi)
    ids.append(0)
    idxs.append(len(idxs))
    answerss.append(answers)

    data = {'q': q, 'cq': cq, 'y': y, 'x': x, 'cx': cx, 'cy': cy, 'p': [paragraph],
            'idxs': idxs, 'ids': ids, 'answerss': answerss}
    return data


if __name__ == "__main__":
    d = prepro("Architecturally, the school has a Catholic character. Atop the Main Building's gold dome is a golden statue of the Virgin Mary. Immediately in front of the Main Building and facing it, is a copper statue of Christ with arms upraised with the legend \"Venite Ad Me Omnes\". Next to the Main Building is the Basilica of the Sacred Heart. Immediately behind the basilica is the Grotto, a Marian place of prayer and reflection. It is a replica of the grotto at Lourdes, France where the Virgin Mary reputedly appeared to Saint Bernadette Soubirous in 1858. At the end of the main drive (and in a direct line that connects through 3 statues and the Gold Dome), is a simple, modern stone statue of Mary.","To whom did the Virgin Mary allegedly appear in 1858 in Lourdes France?")
    print(d)