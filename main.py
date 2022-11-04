import pandas as pd
from pytextdist.edit_distance import lcs_similarity

import re

def no_accent_vietnamese(s):
    s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
    s = re.sub('[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'A', s)
    s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
    s = re.sub('[ÉÈẺẼẸÊẾỀỂỄỆ]', 'E', s)
    s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
    s = re.sub('[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'O', s)
    s = re.sub('[íìỉĩị]', 'i', s)
    s = re.sub('[ÍÌỈĨỊ]', 'I', s)
    s = re.sub('[úùủũụưứừửữự]', 'u', s)
    s = re.sub('[ÚÙỦŨỤƯỨỪỬỮỰ]', 'U', s)
    s = re.sub('[ýỳỷỹỵ]', 'y', s)
    s = re.sub('[ÝỲỶỸỴ]', 'Y', s)
    s = re.sub('đ', 'd', s)
    s = re.sub('Đ', 'D', s)
    return s


def totalResult(df,city, keyword):
    count = 0
    for index in df.index:
        if no_accent_vietnamese(city.lower()) in no_accent_vietnamese(df['City'][index].lower()):
            if no_accent_vietnamese(keyword.lower()) in no_accent_vietnamese(df['Tag'][index].lower()):
                count +=1
    
    return count

def searchAll(df,city, keyword):

    listIndex = []
    dict = {}   
    for index in df.index:
        if no_accent_vietnamese(city.lower()) in no_accent_vietnamese(df['City'][index].lower()):
            if no_accent_vietnamese(keyword.lower()) in no_accent_vietnamese(df['Tag'][index].lower()):
                dict[f"{index}"] = lcs_similarity(no_accent_vietnamese(keyword.lower()),no_accent_vietnamese(df['Tag'][index].lower()))
    for i in sorted(dict, key=dict.get, reverse=True):
        listIndex.append(int(i))
    
    return listIndex
    
def searchTop4(df,city, keyword):

    listIndex = []
    dict = {}   
    count = 0
    for index in df.index:
        if no_accent_vietnamese(city.lower()) in no_accent_vietnamese(df['City'][index].lower()):
            if no_accent_vietnamese(keyword.lower()) in no_accent_vietnamese(df['Tag'][index].lower()):
                dict[f"{index}"] = lcs_similarity(no_accent_vietnamese(keyword.lower()),no_accent_vietnamese(df['Tag'][index].lower()))
    for i in sorted(dict, key=dict.get, reverse=True):
        count+=1
        listIndex.append(int(i))
        if count == 4:
            break

    return listIndex