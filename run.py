# -*- coding: utf-8 -*-
import data_source as ds
import db
import config as cf
import data_pump as pump





if __name__ == "__main__":
    ds=ds.data_source(cf.lead_ds_dict)
    ds.set_file_access()
    databse=db.db(cf.conn_dict)
    databse.set_conn()
    databse.set_cursor()
    conn=databse.conn
    cursor=databse.cursor
    dp=pump.data_pump(ds,databse,cf.lead_format_dict)
    para_list=dp.source_insert()