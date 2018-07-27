# -*- coding: utf-8 -*-

import pandas as pd
import db
import data_source as ds
import config as cf
import util as ut






class data_pump(object):
    def __init__(self,data_source,db,format_dict):
        self.data_source = data_source
        self.db=db
        self.format_dict=format_dict




    def get_data_frame(self):
        if(self.format_dict['type']=="pandas"):
            file_name=self.data_source.file_access
            df=pd.read_csv(file_name, sep=self.format_dict['sep'])
        else:
            df=None
        return df




    def get_data_file(self):
        if(self.format_dict['parse_type']=="text"):
            file = open(self.data_source.file_access)
        else:
            file=None
        return file


    def get_data_response(self):
        res=''
        if(self.format_dict['parse_type']=="html"):
            res = ut.get_url_response(self.data_source._source_dict['url'])
        else:
            res=None
        return res



    def get_header_dict(self):
        header_list_dict={}
        if(self.format_dict['header']==True):
            sep=self.format_dict['sep']
            file=self.get_data_file()
            idx=0
            for line in file:
                if(idx==0):
                    strs=line.strip().split(sep)
                    for j in strs:
                        header_list_dict[j]=strs.index(j)
                idx=idx+1
        elif(self.format_dict['header']==False):
            header_list_dict=self.format_dict['header_attr_dict']
        else:
            pass
        return header_list_dict


    def extract_params(self,line,header_dict):
        paras_list=[]
        if(line):
            strs=line.strip().split(self.format_dict['sep'])
            #print(strs)
            for k,v in self.format_dict['extractor'].items():
                num=header_dict[k]
                if(strs[num]):
                    if(v=='int'):
                        attr=int(strs[num])
                    elif(v=='float'):
                        attr=float(strs[num])
                    elif(v=='date'):
                        attr=ut.date_trans(strs[num],"%Y%m%d")
                    else:
                        attr=strs[num]
                else:
                    attr=0
                paras_list.append(attr)
        return paras_list


    def sql_insert_by_line(self,para_list):
        try:
            self.db.cursor.execute(self.format_dict['insert_sql'],para_list)
            self.db.conn.commit()
        except Exception as e:
            print(e)

    #对整体进行处理
    def source_insert(self):
        if(self.data_source._source_dict['type']=='text'):
            file=self.get_data_file()
            header_dict=self.get_header_dict()
            if self.format_dict['is_fst_line']==False:
                next(file)
                for line in file:
                    print(line)
                    para_list=self.extract_params(line,header_dict)
                    self.sql_insert_by_line(para_list)
            elif self.format_dict['is_fst_line']==True:
                for line in file:
                    para_list=self.extract_params(line,header_dict)
                    self.sql_insert_by_line(para_list)
        elif(self.data_source._source_dict['type']=='url'):
            res=self.get_data_response()
            if(res!='404'):
                header_dict=self.get_header_dict()
                if self.format_dict['is_fst_line']==False:
                    next(res)
                    for line in res:
                        para_list=self.extract_params(line,header_dict)
                        self.sql_insert_by_line(para_list)
                elif self.format_dict['is_fst_line']==True:
                    for line in res.split('\n'):
                        para_list=self.extract_params(line,header_dict)
                        self.sql_insert_by_line(para_list)


    #sql整体处理
    def sql_insert_from_db(self):
        try:
            self.db.cursor.execute(self.format_dict['insert_sql'])
            self.db.conn.commit()
        except Exception as e:
            print(e)


    def sql_insert_test(self,para_list):
        try:
            self.db.cursor.execute(self.format_dict['insert_sql'],para_list)
            self.db.conn.commit()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    #日报补数
    ds=None
    db=db.db(cf.conn_dict)
    db.set_conn()
    db.set_cursor()
    conn=db.conn
    cursor=db.cursor
    para_list=[None,1]
    dp=data_pump(ds,db,cf.test_format_dict)
    dp.sql_insert_test(para_list)
