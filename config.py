import time
import pymysql



#public
date_dict={'year':time.strftime('%Y',time.localtime(time.time() - 8*60*60)),
           'month':time.strftime('%m',time.localtime(time.time() - 8*60*60)),
           'day':time.strftime('%d',time.localtime(time.time() - 8*60*60)),
           'last_day_year':time.strftime('%Y',time.localtime(time.time() - 32*60*60)),
           'last_day_month':time.strftime('%m',time.localtime(time.time() - 32*60*60)),
           'last_day_day':time.strftime('%d',time.localtime(time.time() - 32*60*60))
}

doll_year=date_dict['last_day_year']
doll_month=date_dict['last_day_month']
doll_day=date_dict['last_day_day']




conn_dict={'host':'127.0.0.1',
           'port':3306,
           'user':'root',
           'password':'',
           'db':'huyu_data',
           'charset':'utf8mb4',
           'cursorclass':pymysql.cursors.DictCursor
           }

path='data'
#美颜dau表的配置
my_ds_dict={'name':'my_dau',
              'path':path,
              'file_pre':"18526_"+date_dict['year']+date_dict['month']+date_dict['day'],
              'type':'text'}

my_sql= "INSERT INTO `meiyan_dau`(day,dau) VALUES (%s,%s)"

my_format_dict={'parse_type':'text',
                       'sep':'\t',
                       'header':False,
                        'is_fst_line':True,
                       'extractor':{'day':'int','dau':'int'},
                        'insert_sql':my_sql,
                       'header_attr_dict':{'day':0,'dau':2}
                       }


#美拍dau表的配置
mp_ds_dict={'name':'mp_dau',
            'path':path,
            'file_pre':"17555_"+date_dict['year']+date_dict['month']+date_dict['day'],
            'type':'text'}

mp_sql= "INSERT INTO `meipai_dau`(day,dau) VALUES (%s,%s)"

mp_format_dict={'parse_type':'text',
                'sep':'\t',
                'header':False,
                'is_fst_line':False,
                'extractor':{'day':'int','dau':'int'},
                'insert_sql':mp_sql,
                'header_attr_dict':{'day':0,'dau':2}
                }


#秀秀dau表的配置
xx_ds_dict={'name':'xx_dau',
           'path':path,
           'file_pre':"20160_"+date_dict['year']+date_dict['month']+date_dict['day'],
           'type':'text'}

xx_sql= "INSERT INTO `xiuxiu_dau`(day,dau) VALUES (%s,%s)"

xx_format_dict={'parse_type':'text',
                'sep':'\t',
                'header':False,
                'is_fst_line':False,
                'extractor':{'day':'int','dau':'int'},
                'insert_sql':xx_sql,
                'header_attr_dict':{'day':0,'dau':2}
                }





#lead表的配置
lead_ds_dict={'name':'lead_index',
              'path':path,
              'file_pre':"20008_"+date_dict['year']+date_dict['month']+date_dict['day'],
              'type':'text'}

lead_sql= "INSERT INTO `lead_index`(day,client_info,landing_UV,langding_uids,watching_times,\
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
                  'is_fst_line':False,
                  'extractor':lead_extractor_dict,
                  'insert_sql':lead_sql
                  }

#三端dau通过sql查询给出具体值更新到lead_app_dau表中
dau_sql="""
Insert into lead_app_dau(day,`client_info`,
dau
)
select
day,
'美拍' as client_info,
dau
from
meipai_dau
where day=CONCAT(substr(DATE_SUB(curdate(),INTERVAL 1 DAY),1,4),
substr(DATE_SUB(curdate(),INTERVAL 1 DAY),6,2),
substr(DATE_SUB(curdate(),INTERVAL 1 DAY),9,2))

union all

select
day,
'美颜' as client_info,
dau
from
meiyan_dau
where day=CONCAT(substr(DATE_SUB(curdate(),INTERVAL 1 DAY),1,4),
substr(DATE_SUB(curdate(),INTERVAL 1 DAY),6,2),
substr(DATE_SUB(curdate(),INTERVAL 1 DAY),9,2))

union all


select
day,
'秀秀' as client_info,
dau
from
xiuxiu_dau
where day=CONCAT(substr(DATE_SUB(curdate(),INTERVAL 1 DAY),1,4),
substr(DATE_SUB(curdate(),INTERVAL 1 DAY),6,2),
substr(DATE_SUB(curdate(),INTERVAL 1 DAY),9,2))

union all

select
day,
'整体' as client_info,
sum(dau) as dau
from
(
select
day,
dau
from
meipai_dau
where day=CONCAT(substr(DATE_SUB(curdate(),INTERVAL 1 DAY),1,4),
substr(DATE_SUB(curdate(),INTERVAL 1 DAY),6,2),
substr(DATE_SUB(curdate(),INTERVAL 1 DAY),9,2))

union all

select
day,
dau
from
meiyan_dau
where day=CONCAT(substr(DATE_SUB(curdate(),INTERVAL 1 DAY),1,4),
substr(DATE_SUB(curdate(),INTERVAL 1 DAY),6,2),
substr(DATE_SUB(curdate(),INTERVAL 1 DAY),9,2))

union all


select
day,
dau
from
xiuxiu_dau
where day=CONCAT(substr(DATE_SUB(curdate(),INTERVAL 1 DAY),1,4),
substr(DATE_SUB(curdate(),INTERVAL 1 DAY),6,2),
substr(DATE_SUB(curdate(),INTERVAL 1 DAY),9,2))
) a
group by day
"""



dau_format_dict={'insert_sql':dau_sql
                  }


#dau 和其他指标表拼凑report表
report_sql="""
Insert into lead_report(day,`client_info`,
  dau,
  `landing_UV`,
  `langding_uids`,
  `watching_times`,
  `watching_UV`,
  `watching_uids`,
  `effect_watching_times`,
  `effect_watching_UV`,
  `effect_watching_uids`,
  `avg_watching_play_time`,
  `recharge_amt`,
  `recharge_uids`,
  `catch_doll_amt`,
  `catch_doll_uids`,
  `catch_doll_times`,
  `live_consume_times`,
  `live_inc_amt`,
  `live_consume_uids`) 
select
a.`day` as day,
  a.`client_info` as client_info,
  b.dau as dau,
  `landing_UV`,
  `langding_uids`,
  `watching_times`,
  `watching_UV`,
  `watching_uids`,
  `effect_watching_times`,
  `effect_watching_UV`,
  `effect_watching_uids`,
  `avg_watching_play_time`,
  `recharge_amt`,
  `recharge_uids`,
  c.catch_doll_amt as catch_doll_amt,
  c.catch_doll_uids as catch_doll_uids,
  c.catch_doll_times as catch_doll_times,
  `live_consume_times`,
  `live_inc_amt`,
  `live_consume_uids`
from 
lead_index a
join
lead_app_dau b
ON
a.day = b.day 
and a.client_info = b.client_info
join
doll_report c
a.day = c.day 
and a.client_info = c.client_info
where a.day=CONCAT(substr(DATE_SUB(curdate(),INTERVAL 1 DAY),1,4),
substr(DATE_SUB(curdate(),INTERVAL 1 DAY),6,2),
substr(DATE_SUB(curdate(),INTERVAL 1 DAY),9,2))
"""



report_format_dict={'insert_sql':report_sql
                 }



# 三个端的抓娃娃数据
doll_ds_dict={'name':'doll',
            'url':'http://admin.m.arwawa.sklxsj.com/income/meitu_'
                  +doll_year+'-'+doll_month+'-'+doll_day+'.log',
            'type':'url'}

doll_sql= "INSERT INTO `doll_report`(day,client_info,catch_doll_times,catch_doll_amt,catch_doll_uids) VALUES (%s,%s,%s,%s,%s)"

doll_format_dict={'parse_type':'html',
                'sep':' ',
                'header':False,
                'is_fst_line':True,
                'extractor':{'day':'date','client_info':'string','catch_doll_times':'int','catch_doll_amt':'float',
                'catch_doll_uids':'int'},
                'insert_sql':doll_sql,
                'header_attr_dict':{'day':0,'client_info':1,
                                    'catch_doll_times':2,'catch_doll_amt':3,'catch_doll_uids':4}
                }




#report表 补数
bulk_report_sql="""
Insert into lead_report(day,`client_info`,
  dau,
  `landing_UV`,
  `langding_uids`,
  `watching_times`,
  `watching_UV`,
  `watching_uids`,
  `effect_watching_times`,
  `effect_watching_UV`,
  `effect_watching_uids`,
  `avg_watching_play_time`,
  `recharge_amt`,
  `recharge_uids`,
  `catch_doll_amt`,
  `catch_doll_uids`,
  `catch_doll_times`,
  `live_consume_times`,
  `live_inc_amt`,
  `live_consume_uids`) 
select
a.`day` as day,
  a.`client_info` as client_info,
  b.dau as dau,
  `landing_UV`,
  `langding_uids`,
  `watching_times`,
  `watching_UV`,
  `watching_uids`,
  `effect_watching_times`,
  `effect_watching_UV`,
  `effect_watching_uids`,
  `avg_watching_play_time`,
  `recharge_amt`,
  `recharge_uids`,
  if(a.client_info='整体',a.catch_doll_am,c.catch_doll_am) as catch_doll_amt,
  if(a.client_info='整体',a.catch_doll_uids,c.catch_doll_uids) as catch_doll_uids,
  if(a.client_info='整体',a.catch_doll_times,c.catch_doll_times) as catch_doll_times,
  `live_consume_times`,
  `live_inc_amt`,
  `live_consume_uids`
from 
lead_index a
left join
lead_app_dau b
ON
a.day = b.day 
and a.client_info = b.client_info
left join
(select
day,
case when client_info='meitu' then '秀秀'
when client_info='mtmv' then '美拍'
when client_info='myxj' then '美颜'
end as client_info,
round(catch_doll_amt/10,2) as catch_doll_amt,
catch_doll_uids,
catch_doll_times
from
doll_report
)c
on
a.day = c.day 
and a.client_info = c.client_info
"""



bulk_report_fomat_dict={'insert_sql':bulk_report_sql
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





test_sql= "INSERT INTO `test`(id,client_info) VALUES (%s,%s)"

test_format_dict={
    'insert_sql':test_sql
}

