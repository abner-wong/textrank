#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/2 18:13
# @Author  :Abner Wong
# @Software: PyCharm

import jieba.posseg as pseg

import re
from .const import STOPWORDS, PROPERTY_FILTER

SENTENCE_SP_PATTERN = re.compile(r"。|\.|！|\!|？|\?|;")


class Text:
    def __init__(self, text, use_property, no_stopwords):
        """

        :param text:
        :param use_property: 是否根据词性进行筛选
        :param no_stopwords: 是否去停用词
        """

        if text is None:
            raise ValueError('text should not be none!')
        elif not isinstance(text, str):
            raise ValueError('text type must be str!')

        self.sents = self._sentence_split(text)
        self.words_pro = self._get_words(self.sents, use_property, no_stopwords)

    def _get_words(self, sents, use_property, no_stopwords):

        words = list()

        if len(sents) < 1:
            return None

        for s in sents:
            cut_s = pseg.cut(s)
            if use_property:
                cut_s = [w for w in cut_s if w.flag in PROPERTY_FILTER]
            else:
                cut_s = [w for w in cut_s]

            cut_s = self._clean_words(cut_s)
            if no_stopwords:
                cut_s = [w.strip() for w in cut_s if w.strip() not in STOPWORDS]
            words.append(cut_s)

        return words

    @staticmethod
    def _sentence_split(text):
        sents = [i.strip() for i in SENTENCE_SP_PATTERN.split(text) if i != '' ]
        return sents

    @staticmethod
    def _clean_words(sent):
        w_ls = [w.word.strip() for w in sent if w.flag != 'x']
        w_ls = [word for word in w_ls if len(word) > 0]
        return w_ls

