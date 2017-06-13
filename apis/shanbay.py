__author__ = 'cyrbuzz'
"""
https://www.shanbay.com/
Shanbay 查询单词的Api.
"""
import json

from apiBase import HttpRequest


class ShanbaySearch(HttpRequest):
    
    searchWordUrl = 'https://api.shanbay.com/bdc/search/?word={word}'

    def searchWord(self, word):
        try:
            result = self.httpRequest(self.searchWordUrl.format(word=word))
        except:
            return {'definition': '网络超时.'}
        result = json.loads(result.text)

        if result['msg'] == 'SUCCESS':

            # 目前只返回翻译。
            # 扇贝返回的翻译前面有一个空格。
            return {'definition': '{word}\n{definition}'.format(word=word, definition=result['data']['definition'][1:])}
        else:
            return {'definition': '没有找到.'}


if __name__ == '__main__':
    shanbaySearch = ShanbaySearch()
    test = shanbaySearch.searchWord('one')

    print(test)
