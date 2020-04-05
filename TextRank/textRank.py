#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/2 19:36
# @Author  :Abner Wong
# @Software: PyCharm

from .textPro import Text
from . import utils

from collections import Counter


class TextRank(Text):

    def __init__(self,
                 text=None, windows=2,
                 use_property=True, no_stopwords=True,
                 pr_config={'alpha': 0.85, 'max_iter': 100}):
        super(TextRank, self).__init__(text, use_property, no_stopwords)

        self.pr_config = pr_config
        self.windows = windows
        self.word_index, self.index_word, self.word_num = utils.words_info(self.words_pro)
        self.sorted_words = self._score_items(is_word=True)
        self.sorted_sents = self._score_items(is_word=False)

    def _build_adjacency_matrix(self, is_word=True):

        if is_word:
            adj_matrix = utils.word_adj_matrix(self.words_pro,
                                               self.windows,
                                               self.word_num,
                                               self.word_index)
        else:
            adj_matrix = utils.sent_adj_matrix(self.words_pro)

        return adj_matrix

    def _score_items(self, is_word=True):
        if is_word:
            adj_matrix = self._build_adjacency_matrix(is_word=is_word)
            scores = utils.cal_score(adj_matrix, **self.pr_config)
            sorted_items = utils.get_sorted_items(scores, self.index_word)
        else:
            adj_matrix = self._build_adjacency_matrix(is_word=is_word)
            scores = utils.cal_score(adj_matrix, **self.pr_config)
            index_sent = dict(zip(range(len(self.sents)), self.sents))
            sorted_items = utils.get_sorted_items(scores, index_sent)

        return sorted_items

    def get_n_keywords(self, N):
        return self.sorted_words[:N]

    def get_n_sentences(self, N):
        return self.sorted_sents[:N]
