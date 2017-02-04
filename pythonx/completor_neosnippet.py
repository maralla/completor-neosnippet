# -*- coding: utf-8 -*-

import vim
from completor import Completor


_cache = {}


class Neosnippet(Completor):
    filetype = 'neosnippet'
    sync = True

    @staticmethod
    def _get_snippets():
        get_snippets = vim.Function(
            'neosnippet#helpers#get_completion_snippets')
        return [{
            'word': item['word'],
            'menu': ' '.join(['[neosnip]', item['description']])
        } for item in get_snippets().values()]

    def parse(self, base):
        if not self.ft or not base:
            return []

        if self.ft not in _cache:
            try:
                _cache[self.ft] = self._get_snippets()
            except Exception:
                _cache[self.ft] = []

        pat = base.rstrip().rsplit(' ', 1)[-1]
        return [item for item in _cache[self.ft] if pat in item['word']]
