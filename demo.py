# -*- coding: utf-8 -*-
# @Author  : quincyqiang
# @File    : demo.py
# @Time    : 2018/8/28 15:02

from triple_extraction import TripleExtractor

def main():
    content="""著名导演陈烈院线电影《爱是永恒》即将上映h"""
    extractor = TripleExtractor()
    svos = extractor.triples_main(content)
    print('svos', svos)

if __name__ == '__main__':
    main()