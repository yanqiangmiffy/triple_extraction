# -*- coding: utf-8 -*-
# @Author  : quincyqiang
# @File    : sentence_parser.py
# @Time    : 2018/8/28 10:46

import os
from pyltp import Segmentor,Postagger,Parser,NamedEntityRecognizer,SementicRoleLabeller
class LtpParser:
    def __init__(self):
        # ltp 模型路径
        LTP_DATA_DIR='./ltp_data'

        # 分词模型
        self.segmentor=Segmentor()
        self.segmentor.load(os.path.join(LTP_DATA_DIR,'cws.model'))

        # 词性标注模型
        self.postagger=Postagger()
        self.postagger.load(os.path.join(LTP_DATA_DIR,'pos.model'))

        # 依存句法分析
        self.parser=Parser()
        self.parser.load(os.path.join(LTP_DATA_DIR,'parser.model'))

        # 命名实体识别
        self.recognizer=NamedEntityRecognizer()
        self.recognizer.load(os.path.join(LTP_DATA_DIR,'ner.model'))

        # 语义角色标注
        self.labeller=SementicRoleLabeller()
        self.labeller.load(os.path.join(LTP_DATA_DIR,'pisrl_win.model'))

    def format_label_role(self, words, postags):
        """
        语义角色标注
        :param self:
        :param words:
        :param postags:
        :return:
        """
        arcs = self.parser.parse(words, postags)
        roles = self.labeller.label(words,postags,arcs)
        roles_dict={}

        for role in roles:
            roles_dict[role.index]={arg.name:[arg.name,arg.range.start,arg.range.end] for arg in roles.arguments}
        return roles_dict

    def build_parse_child_dict(self,words,postags,arcs):
        """
        句法分析---为句子的每个词语维护一个保存语法依存儿子节点的字典
        :param words:
        :param postags:
        :param arcs:
        :return:
        """
        child_dict_list=[]
        format_parse_list=[]

        for index in range(len(words)):
            child_dict=dict()
            for arc_index in range(len(arcs)):
                if arcs[arc_index].head==index+1:# arcs的索引从1开始
                    if arcs[arc_index].relation in child_dict:
                        child_dict[arcs[arc_index].relation].append(arc_index)
                    else:
                        child_dict[arcs[arc_index].relation]=[]
                        child_dict[arcs[arc_index].relation].append(arc_index)
            child_dict_list.append(child_dict)
        rely_id=[arc.head for arc in arcs] # 提取依存父节点id
        relation=[arc.relation for arc in arcs]
        heads=['Root' if id==0 else words[id-1] for id in rely_id]
