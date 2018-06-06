# -*- coding: utf-8 -*-

import pandas as pd
import db
import data_source as ds
import config as cf






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
        print(header_dict)
        paras_list=[]
        if(line):
            strs=line.strip().split(self.format_dict['sep'])
            for k,v in self.format_dict['extractor'].items():
                print(k)
                num=header_dict[k]
                print(strs[num])
                if(v=='int'):
                    attr=int(strs[header_dict[k]])
                elif(v=='float'):
                    attr=float(strs[header_dict[k]])
                else:
                    attr=strs[header_dict[k]]
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
            if self.format_dict['header']==True:
                next(file)
                for line in file:
                    para_list=self.extract_params(line,header_dict)
                    self.sql_insert_by_line(para_list)
            elif self.format_dict['header']==False:
                for line in file:
                    para_list=self.extract_params(line,header_dict)
                    self.sql_insert_by_line(para_list)


if __name__ == "__main__":
    ds=ds.data_source(cf.lead_ds_dict)
    ds.set_file_access()
    databse=db.db(cf.conn_dict)
    databse.set_conn()
    databse.set_cursor()
    conn=databse.conn
    cursor=databse.cursor
    dp=data_pump(ds,databse,cf.lead_format_dict)
    para_list=dp.source_insert()
