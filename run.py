#!/usr/bin/env python
from app import create_app,db
from models import Daily_kpi_report
import os
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand
import controllers



app=create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate =Migrate(app,db)





def make_shell_context():
    return dict(app=app,db=db,Daily_kpi_report=Daily_kpi_report)
manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)

@manager.command
def hello():
    controllers.insert_daily_kpi_report_test()
    controllers.insert_daily_kpi_report_te()





if __name__=='__main__':
    manager.run()

