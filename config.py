import time
import pymysql



#public
date_dict={'year':time.strftime('%Y',time.localtime()),
           'month':time.strftime('%m',time.localtime()),
           'day':time.strftime('%d',time.localtime())
}

conn_dict={'host':'127.0.0.1',
           'port':3306,
           'user':'root',
           'password':'',
           'db':'huyu_data',
           'charset':'utf8mb4',
           'cursorclass':pymysql.cursors.DictCursor
           }

#美颜dau表的配置
my_ds_dict={'name':'my_dau',
              'path':'data',
              'file_pre':"18526_"+date_dict['year']+date_dict['month']+date_dict['day'],
              'type':'text'}

my_sql= "INSERT INTO `meiyan_dau`(date,dau) VALUES (%s,%s)"

my_format_dict={'parse_type':'text',
                       'sep':'\t',
                       'header':False,
                       'extractor':{'date':'int','dau':'int'},
                        'insert_sql':my_sql,
                       'header_attr_dict':{'date':0,'dau':2}
                       }


#test表的配置
test_ds_dict={'name':'test',
              'path':'data',
              'file_pre':"20008_"+date_dict['year']+date_dict['month']+date_dict['day'],
              'type':'text'}

test_sql= "INSERT INTO `test`(date,client_info) VALUES (%s,%s)"

test_format_dict={'parse_type':'text',
                  'sep':' ',
                  'header':True,
                  'extractor':{'date':'int','client_info':'string'},
                  'insert_sql':test_sql
                  }


#lead表的配置
lead_ds_dict={'name':'test',
              'path':'data',
              'file_pre':"20008_"+date_dict['year']+date_dict['month']+date_dict['day'],
              'type':'text'}

lead_sql= "INSERT INTO `lead_report`(day,client_info,landing_UV,langding_uids,watching_times,\
            watching_UV,watching_uids,effect_watching_times,effect_watching_UV,effect_watching_uids,\
            avg_watching_play_time,recharge_amt,recharge_uids,catch_doll_amt,\
            catch_doll_uids,catch_doll_times,live_consume_times,live_inc_amt,\
            live_consume_uids) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

lead_extractor_dict={'day':'int',
               'client_info':'string',
               'landing_UV':'int',
               'langding_uids':'int',
               'watching_times':'int',
               'watching_UV':'int',
               'watching_uids':'int',
               'effect_watching_times':'int',
               'effect_watching_UV':'int',
               'effect_watching_uids':'int',
               'avg_watching_play_time':'float',
               'recharge_amt':'float',
               'recharge_uids':'int',
               'catch_doll_amt':'float',
               'catch_doll_uids':'int',
               'catch_doll_times':'int',
               'live_consume_times':'int',
               'live_inc_amt':'float',
               'live_consume_uids':'int'}

lead_format_dict={'parse_type':'text',
                  'sep':'\t',
                  'header':True,
                  'extractor':lead_extractor_dict,
                  'insert_sql':lead_sql
                  }


# lead_dtype={'day':sqlalchemy.types.INTEGER(),
#             'client_info':sqlalchemy.types.NVARCHAR(length=255),
#             'landing_UV':sqlalchemy.types.INTEGER(),
#             'langding_uids':sqlalchemy.types.INTEGER(),
#             'watching_times':sqlalchemy.types.INTEGER(),
#             'watching_UV':sqlalchemy.types.INTEGER(),
#             'watching_uids':sqlalchemy.types.INTEGER(),
#             'effect_watching_times':sqlalchemy.types.INTEGER(),
#             'effect_watching_UV':sqlalchemy.types.INTEGER(),
#             'effect_watching_uids':sqlalchemy.types.INTEGER(),
#             'avg_watching_play_time':sqlalchemy.types.INTEGER(),
#             'recharge_amt':sqlalchemy.types.Float(),
#             'recharge_uids':sqlalchemy.types.INTEGER(),
#             'catch_doll_amt':sqlalchemy.types.Float(),
#             'catch_doll_uids':sqlalchemy.types.INTEGER(),
#             'catch_doll_times':sqlalchemy.types.INTEGER(),
#             'live_consume_times':sqlalchemy.types.INTEGER(),
#             'live_inc_amt':sqlalchemy.types.Float(),
#             'live_consume_uids':sqlalchemy.types.INTEGER()
#             }






