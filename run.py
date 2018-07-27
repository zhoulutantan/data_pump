# -*- coding: utf-8 -*-
import data_source as ds
import db
import config as cf
import data_pump as pump





if __name__ == "__main__":

    database=db.db(cf.conn_dict)
    database.set_conn()
    database.set_cursor()
    conn=database.conn
    cursor=database.cursor

# 根据文件把dau数据放入dau表
    xx_ds=ds.data_source(cf.xx_ds_dict)
    #print(cf.xx_ds_dict)
    xx_ds.set_file_access()
    #print(xx_ds.file_access)
    xx_dp=pump.data_pump(xx_ds,database,cf.xx_format_dict)
    xx_dp.source_insert()

    mp_ds=ds.data_source(cf.mp_ds_dict)
    #print(cf.mp_ds_dict)
    mp_ds.set_file_access()
    #print(mp_ds.file_access)
    mp_dp=pump.data_pump(mp_ds,database,cf.mp_format_dict)
    mp_dp.source_insert()

    my_ds=ds.data_source(cf.my_ds_dict)
    #print(cf.my_ds_dict)
    my_ds.set_file_access()
    #print(my_ds.file_access)
    my_dp=pump.data_pump(my_ds,database,cf.my_format_dict)
    my_dp.source_insert()


    #把数据放入lead_index
    li_ds=ds.data_source(cf.lead_ds_dict)
    #print(cf.lead_ds_dict)
    li_ds.set_file_access()
    #print(li_ds.file_access)
    li_dp=pump.data_pump(li_ds,database,cf.lead_format_dict)
    li_dp.source_insert()

    #整合dau
    dau_ds=None
    dau_dp=pump.data_pump(dau_ds,database,cf.dau_format_dict)
    dau_dp.sql_insert_from_db()


    #把数据放入娃娃机日报
    doll_ds=ds.data_source(cf.doll_ds_dict)
    doll_ds.set_file_access()
    doll_dp=pump.data_pump(doll_ds,database,cf.doll_format_dict)
    doll_dp.source_insert()

    #整合report
    report_ds=None
    report_dp=pump.data_pump(report_ds,database,cf.report_format_dict)
    report_dp.sql_insert_from_db()

    database.conn_close()