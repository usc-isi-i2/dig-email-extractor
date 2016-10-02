# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-21 12:36:47
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-10-02 15:42:03

import copy 
import types
from digExtractor.extractor import Extractor
from dig_email_extractor import DIGEmailExtractor

class EmailExtractor(Extractor):

    def __init__(self):
        self.renamed_input_fields = ['text']

    def extract(self, doc):
        if 'text' in doc
            return DIGEmailExtractor(_output_format='obfuscation').extract_email(doc['text'])
            # return DIGEmailExtractor(_output_format='list').extract_email(doc['text'])
        return None

    def get_metadata(self):
        return copy.copy(self.metadata)

    def set_metadata(self, metadata):
        self.metadata = metadata
        return self

    def get_renamed_input_fields(self):
        return self.renamed_input_fields

