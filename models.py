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
    total_inc_amt = db.Column(db.Float)


class Month_consume_user_feature_report(db.Model):
    __tablename__ = 'month_consume_user_feature_report'
    mo_p = db.Column(db.Integer, primary_key=True)
    hour= db.Column(db.String)
    refer = db.Column(db.String)
    gender = db.Column(db.String)
    age_rank = db.Column(db.String)
    amt_rank = db.Column(db.String)
    freq_rank = db.Column(db.String)
    province_name = db.Column(db.String)
    city_level = db.Column(db.String)
    reg_age = db.Column(db.String)
    user_active_type = db.Column(db.String)
    tag_name = db.Column(db.String)
    gift_type = db.Column(db.String)
    gift_name = db.Column(db.String)
    anchor_looks_rank = db.Column(db.String)
    anchor_talent_rank = db.Column(db.String)
    anchor_interaction_rank = db.Column(db.String)
    city_name = db.Column(db.String)
    uids = db.Column(db.Integer)
    coins = db.Column(db.Float)









