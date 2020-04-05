#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/2 19:39
# @Author  :Abner Wong
# @Software: PyCharm

import numpy as np
import math


def words_info(words_list):
    """
    :param words_list:
    :return:
    """
    word_index = dict()
    index_word = dict()
    word_num = 0

    for index_s, words in enumerate(words_list):
        for index_w, word in enumerate(words):
            word_index[word] = word_num
            index_word[word_num] = word
            word_num += 1

    return word_index, index_word, word_num


def sents_info(sents_list):

    return dict(zip(range(len(sents_list)), sents_list))


def word_adj_matrix(words_pro, windows, word_num, word_index):
    """
    Adjacency Matrix
    :param windows:
    :return:
    """
    def _word_combine(words, window):
        """
        Keyword arguments:
        :param window:
        """
        if window < 2: window = 2

        for x in range(1, window):
            if x >= len(words):
                break
            words2 = words[x:]
            res = zip(words, words2)
            for r in res:
                yield r

    matrix = np.zeros((word_num, word_num))

    for words in words_pro:
        for w1, w2 in _word_combine(words, windows):
            if w1 in word_index and w2 in word_index:
                index1 = word_index.get(w1)
                index2 = word_index.get(w2)
                matrix[index1][index2] = 1.0
                matrix[index2][index1] = 1.0

    return matrix


def sent_adj_matrix(words_pro):

    def _get_similarity(word_ls1, word_ls2):
        co_occur_num = len(set(word_ls1) & set(word_ls2))
        if abs(co_occur_num) <= 1e-12:
            return 0.

        if len(word_ls1) == 0 or len(word_ls2) == 0:
            return 0.

        denominator = math.log(float(len(word_ls1))) + math.log(float(len(word_ls2)))

        if abs(denominator) < 1e-12:
            return 0.

        return co_occur_num / denominator

    sentences_num = len(words_pro)
    matrix = np.zeros((sentences_num, sentences_num))

    for x in range(sentences_num):
        for y in range(x, sentences_num):
            s = _get_similarity(words_pro[x], words_pro[y])
            matrix[x, y] = s
            matrix[y, x] = s
    return matrix


def cal_score(ad_matrix, alpha=0.85, max_iter=100):

    N = len(ad_matrix)
    ad_sum = ad_matrix.sum(axis=0).astype(float)
    ad_sum[ad_sum == 0.0] = 0.001
    ad_matrix = ad_matrix / ad_sum
    pr = np.full([N, 1], 1 / N)

    for _ in range(max_iter):
        pr = np.dot(ad_matrix, pr) * alpha + (1 - alpha)
    pr = pr / pr.sum()

    scores = dict(zip(range(len(pr)), [i[0] for i in pr]))

    return scores


def get_sorted_items(scores, index_items):
    """
    :param scores:
    :param index_items:
    :return: list[tuple]
    """
    items_scores = dict()
    for index, score in scores.items():
        items_scores[index_items.get(index)] = score
    sorted_items = sorted(items_scores.items(), key=lambda item: item[1], reverse=True)
    return sorted_items



