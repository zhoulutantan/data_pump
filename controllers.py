from app import db
import util as ut
from models import Daily_kpi_report



def insert_daily_kpi_report(ds_key):
    re= ut.get_rs_data(ds_key)
    if re['status']=='OK':
        for line in re['rs_dict']:
            daily_kpi_report=Daily_kpi_report(date=line.get('date'),
                                        client_name=line.get('client_name'),
                                        app_dau=line.get('app_dau'),
                                        sdk_dau = line.get('sdk_dau'),
                                        sdk_uids = line.get('sdk_uids'),
                                        watch_cnt = line.get('watch_cnt'),
                                        watch_uv = line.get('watch_uv'),
                                        watch_uids = line.get('watch_uids'),
                                        effect_watch_cnt = line.get('effect_watch_cnt'),
                                        effect_watch_uv = line.get('effect_watch_uv'),
                                        effect_watch_uids = line.get('effect_watch_uids'),
                                        avg_watch_play_time = line.get('avg_watch_play_time'),
                                        recharge_amt = line.get('recharge_amt'),
                                        recharge_uids = line.get('recharge_uids'),
                                        catch_doll_cnt = line.get('catch_doll_cnt'),
                                        catch_doll_amt = line.get('catch_doll_amt'),
                                        catch_doll_uids = line.get('catch_doll_uids'),
                                        live_and_video_gift_cnt = line.get('live_and_video_gift_cnt'),
                                        live_and_video_gift_amt = line.get('live_and_video_gift_amt'),
                                        live_and_video_gift_uids = line.get('live_and_video_gift_uids'),
                                        total_inc_amt = line.get('total_inc_amt'))
            db.session.add(daily_kpi_report)
            try:
                db.session.commit()
            except Exception as err:
                print(err)
                db.session.rollback()

def insert_daily_kpi_report_test():
    daily_kpi_report=Daily_kpi_report(date=20180710,
                                              client_name='美拍',
                                              app_dau=102,
                                              sdk_dau = 102,
                                              sdk_uids = 102,
                                              watch_cnt = 102,
                                              watch_uv = 102,
                                              watch_uids = 102,
                                              effect_watch_cnt = 102,
                                              effect_watch_uv = 102,
                                              effect_watch_uids = 102,
                                              avg_watch_play_time = 102,
                                              recharge_amt = 102.3,
                                              recharge_uids = 102,
                                              catch_doll_cnt = 102,
                                              catch_doll_amt = 102,
                                              catch_doll_uids = 102,
                                              live_and_video_gift_cnt = 102,
                                              live_and_video_gift_amt = 102,
                                              live_and_video_gift_uids = 102,
                                              total_inc_amt=104
                                      )
    db.session.add(daily_kpi_report)
    try:
        db.session.commit()
    except Exception as err:
        print(err)
        db.session.rollback()

def insert_daily_kpi_report_t(date):
    daily_kpi_report=Daily_kpi_report(date=date,
                                      client_name='美拍',
                                      app_dau=1202,
                                      sdk_dau = 1202,
                                      sdk_uids = 1202,
                                      watch_cnt = 1202,
                                      watch_uv = 1202,
                                      watch_uids = 1202,
                                      effect_watch_cnt = 1202,
                                      effect_watch_uv = 1202,
                                      effect_watch_uids = 1202,
                                      avg_watch_play_time = 1202,
                                      recharge_amt = 102.3,
                                      recharge_uids = 1202,
                                      catch_doll_cnt = 1202,
                                      catch_doll_amt = 1202,
                                      catch_doll_uids = 1202,
                                      live_and_video_gift_cnt = 1202,
                                      live_and_video_gift_amt = 1202,
                                      live_and_video_gift_uids = 1202,
                                      total_inc_amt = 104)
    db.session.add(daily_kpi_report)
    try:
        db.session.commit()
    except Exception as err:
        print(err)
        db.session.rollback()




