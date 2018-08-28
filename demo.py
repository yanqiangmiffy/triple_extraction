# -*- coding: utf-8 -*-
# @Author  : quincyqiang
# @File    : demo.py
# @Time    : 2018/8/28 15:02

from triple_extraction import TripleExtractor

def main():
    content="""一个年轻女士在地下车库遭遇三个壮汉的纠缠，难免有应激反应，网文当中有“表达出入”，
    只要没有造成严重的社会危害，司法机关应该给予更多的安抚而不是惩戒。"""
    extractor = TripleExtractor()
    svos = extractor.triples_main(content)
    print('svos', svos)

if __name__ == '__main__':
    main()