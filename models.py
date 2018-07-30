from app import db




class Daily_kpi_report(db.Model):
    __tablename__ = 'daily_kpi_report'
    date = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(64), primary_key=True)
    app_dau=db.Column(db.Integer)
    sdk_dau = db.Column(db.Integer)
    sdk_uids = db.Column(db.Integer)
    watch_cnt = db.Column(db.Integer)
    watch_uv = db.Column(db.Integer)
    watch_uids = db.Column(db.Integer)
    effect_watch_cnt = db.Column(db.Integer)
    effect_watch_uv = db.Column(db.Integer)
    effect_watch_uids = db.Column(db.Integer)
    avg_watch_play_time = db.Column(db.Integer)
    recharge_amt = db.Column(db.Float)
    recharge_uids = db.Column(db.Integer)
    catch_doll_cnt = db.Column(db.Integer)
    catch_doll_amt = db.Column(db.Float)
    catch_doll_uids = db.Column(db.Integer)
    live_and_video_gift_cnt = db.Column(db.Integer)
    live_and_video_gift_amt = db.Column(db.Float)
    live_and_video_gift_uids = db.Column(db.Integer)
    live_and_video_gift_arpu = db.Column(db.Float)
    total_consume_amt = db.Column(db.Float)
    total_consume_uids = db.Column(db.Integer)









