# -*- coding: utf-8 -*-

import logging
from completor import Completor, vim

_cache = {}

logger = logging.getLogger('completor')


class Neosnippet(Completor):
    filetype = 'neosnippet'
    sync = True

    @staticmethod
    def _get_snippets():
        get_snippets = vim.Function(
            'neosnippet#helpers#get_completion_snippets')
        snippets = [{
            'word': item[b'word'],
            'dup': 1,
            'menu': b' '.join([b'[neosnip]', item[b'description']])
        } for item in get_snippets().values()]
        snippets.sort(key=lambda x: x['word'])
        return snippets

    def parse(self, base):
        if not self.ft or not base or base.endswith((' ', '\t')):
            return []

        if self.ft not in _cache:
            try:
                _cache[self.ft] = self._get_snippets()
            except Exception:
                _cache[self.ft] = []

        token = self.input_data.split()[-1]
        candidates = [dict(item) for item in _cache[self.ft]
                      if item['word'].startswith(token.encode('utf-8'))]
        logger.info(candidates)

        offset = len(self.input_data) - len(token)
        for c in candidates:
            c['abbr'] = c['word']
            c['offset'] = offset
        return candidates
