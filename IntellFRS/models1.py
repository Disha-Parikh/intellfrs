from datetime import datetime
from IntellFRS import db, login_manager
from flask_login import UserMixin

class Att(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    pa = db.Column(db.String(8), nullable=False)
    # date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    # time = db.Column(db.Time, nullable=False, default=datetime.utcnow)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    reg_no= db.Column(db.Integer, nullable=False)

    def __repr__(self):
        # return f"Attendance('{self.id}', '{self.name}', '{self.pa}', '{self.date}','{self.time}','{self.datetime}', '{self.reg_no}')"
        return f"Att('{self.id}', '{self.name}', '{self.pa}','{self.datetime}', '{self.reg_no}')"
#
# from IntellFRS.models1 import db,Att
# a1=Att(name='a',pa='P',datetime='2019-02-27 09:15:17.030035', reg_no=1)
# a2=Att(name='a',pa='P',datetime='2019-02-26 09:15:17.030035', reg_no=1)
# a3=Att(name='a',pa='P',datetime='2019-02-25 09:15:17.030035', reg_no=1)
# a4=Att(name='a',pa='P',datetime='2019-02-24 09:15:17.030035', reg_no=1)
# a5=Att(name='a',pa='P',datetime='2019-02-23 09:15:17.030035', reg_no=1)
# a6=Att(name='a',pa='P',datetime='2019-02-22 09:15:17.030035', reg_no=1)
# a7=Att(name='a',pa='P',datetime='2019-02-21 09:15:17.030035', reg_no=1)
# a8=Att(name='a',pa='P',datetime='2019-02-20 09:15:17.030035', reg_no=1)
# a9=Att(name='a',pa='P',datetime='2019-02-19 09:15:17.030035', reg_no=1)
#
# db.session.add(a1)
# db.session.add(a2)
# db.session.add(a3)
# db.session.add(a4)
# db.session.add(a5)
# db.session.add(a6)
# db.session.add(a7)
# db.session.add(a8)
# db.session.add(a9)
# db.session.commit()
#
# a1=Att(name='a',pa='P',datetime='2019-03-27 09:15:17.030035', reg_no=1)
# a2=Att(name='a',pa='P',datetime='2019-03-26 09:15:17.030035', reg_no=1)
# a3=Att(name='a',pa='P',datetime='2019-03-25 09:15:17.030035', reg_no=1)
# a4=Att(name='a',pa='P',datetime='2019-03-24 09:15:17.030035', reg_no=1)
# a5=Att(name='a',pa='P',datetime='2019-03-23 09:15:17.030035', reg_no=1)
# a6=Att(name='a',pa='P',datetime='2019-03-22 09:15:17.030035', reg_no=1)
# a7=Att(name='a',pa='P',datetime='2019-03-21 09:15:17.030035', reg_no=1)
# a8=Att(name='a',pa='P',datetime='2019-03-20 09:15:17.030035', reg_no=1)
# a9=Att(name='a',pa='P',datetime='2019-03-19 09:15:17.030035', reg_no=1)
#
# db.session.add(a1)
# db.session.add(a2)
# db.session.add(a3)
# db.session.add(a4)
# db.session.add(a5)
# db.session.add(a6)
# db.session.add(a7)
# db.session.add(a8)
# db.session.add(a9)
# db.session.commit()
#
#
# a1=Att(name='a',pa='P',datetime='2019-04-27 09:15:17.030035', reg_no=1)
# a2=Att(name='a',pa='P',datetime='2019-04-26 09:15:17.030035', reg_no=1)
# a3=Att(name='a',pa='P',datetime='2019-04-25 09:15:17.030035', reg_no=1)
# a4=Att(name='a',pa='P',datetime='2019-04-24 09:15:17.030035', reg_no=1)
# a5=Att(name='a',pa='P',datetime='2019-04-23 09:15:17.030035', reg_no=1)
# a6=Att(name='a',pa='P',datetime='2019-04-22 09:15:17.030035', reg_no=1)
# a7=Att(name='a',pa='P',datetime='2019-04-21 09:15:17.030035', reg_no=1)
# a8=Att(name='a',pa='P',datetime='2019-04-20 09:15:17.030035', reg_no=1)
# a9=Att(name='a',pa='P',datetime='2019-04-19 09:15:17.030035', reg_no=1)
#
#
# db.session.add(a1)
# db.session.add(a2)
# db.session.add(a3)
# db.session.add(a4)
# db.session.add(a5)
# db.session.add(a6)
# db.session.add(a7)
# db.session.add(a8)
# db.session.add(a9)
# db.session.commit()
#
# a1=Att(name='a',pa='P',datetime='2019-05-27 09:15:17.030035', reg_no=1)
# a2=Att(name='a',pa='P',datetime='2019-05-26 09:15:17.030035', reg_no=1)
# a3=Att(name='a',pa='P',datetime='2019-05-25 09:15:17.030035', reg_no=1)
# a4=Att(name='a',pa='P',datetime='2019-05-24 09:15:17.030035', reg_no=1)
# a5=Att(name='a',pa='P',datetime='2019-05-23 09:15:17.030035', reg_no=1)
# a6=Att(name='a',pa='P',datetime='2019-05-22 09:15:17.030035', reg_no=1)
# a7=Att(name='a',pa='P',datetime='2019-05-21 09:15:17.030035', reg_no=1)
# a8=Att(name='a',pa='P',datetime='2019-05-20 09:15:17.030035', reg_no=1)
# a9=Att(name='a',pa='P',datetime='2019-05-19 09:15:17.030035', reg_no=1)
#
# db.session.add(a1)
# db.session.add(a2)
# db.session.add(a3)
# db.session.add(a4)
# db.session.add(a5)
# db.session.add(a6)
# db.session.add(a7)
# db.session.add(a8)
# db.session.add(a9)
# db.session.commit()
#
# a1=Att(name='a',pa='P',datetime='2019-06-27 09:15:17.030035', reg_no=1)
# a2=Att(name='a',pa='P',datetime='2019-06-26 09:15:17.030035', reg_no=1)
# a3=Att(name='a',pa='P',datetime='2019-06-25 09:15:17.030035', reg_no=1)
# a4=Att(name='a',pa='P',datetime='2019-06-24 09:15:17.030035', reg_no=1)
# a5=Att(name='a',pa='P',datetime='2019-06-23 09:15:17.030035', reg_no=1)
# a6=Att(name='a',pa='P',datetime='2019-06-22 09:15:17.030035', reg_no=1)
# a7=Att(name='a',pa='P',datetime='2019-06-21 09:15:17.030035', reg_no=1)
# a8=Att(name='a',pa='P',datetime='2019-06-20 09:15:17.030035', reg_no=1)
# a9=Att(name='a',pa='P',datetime='2019-06-19 09:15:17.030035', reg_no=1)
#
# db.session.add(a1)
# db.session.add(a2)
# db.session.add(a3)
# db.session.add(a4)
# db.session.add(a5)
# db.session.add(a6)
# db.session.add(a7)
# db.session.add(a8)
# db.session.add(a9)
# db.session.commit()
#
# a1=Att(name='a',pa='P',datetime='2019-07-27 09:15:17.030035', reg_no=1)
# a2=Att(name='a',pa='P',datetime='2019-07-26 09:15:17.030035', reg_no=1)
# a3=Att(name='a',pa='P',datetime='2019-07-25 09:15:17.030035', reg_no=1)
# a4=Att(name='a',pa='P',datetime='2019-07-24 09:15:17.030035', reg_no=1)
# a5=Att(name='a',pa='P',datetime='2019-07-23 09:15:17.030035', reg_no=1)
# a6=Att(name='a',pa='P',datetime='2019-07-22 09:15:17.030035', reg_no=1)
# a7=Att(name='a',pa='P',datetime='2019-07-21 09:15:17.030035', reg_no=1)
# a8=Att(name='a',pa='P',datetime='2019-07-20 09:15:17.030035', reg_no=1)
# a9=Att(name='a',pa='P',datetime='2019-07-19 09:15:17.030035', reg_no=1)
#
# db.session.add(a1)
# db.session.add(a2)
# db.session.add(a3)
# db.session.add(a4)
# db.session.add(a5)
# db.session.add(a6)
# db.session.add(a7)
# db.session.add(a8)
# db.session.add(a9)
# db.session.commit()
#
# a1=Att(name='a',pa='P',datetime='2019-08-27 09:15:17.030035', reg_no=1)
# a2=Att(name='a',pa='P',datetime='2019-08-26 09:15:17.030035', reg_no=1)
# a3=Att(name='a',pa='P',datetime='2019-08-25 09:15:17.030035', reg_no=1)
# a4=Att(name='a',pa='P',datetime='2019-08-24 09:15:17.030035', reg_no=1)
# a5=Att(name='a',pa='P',datetime='2019-08-23 09:15:17.030035', reg_no=1)
# a6=Att(name='a',pa='P',datetime='2019-08-22 09:15:17.030035', reg_no=1)
# a7=Att(name='a',pa='P',datetime='2019-08-21 09:15:17.030035', reg_no=1)
# a8=Att(name='a',pa='P',datetime='2019-08-20 09:15:17.030035', reg_no=1)
# a9=Att(name='a',pa='P',datetime='2019-08-19 09:15:17.030035', reg_no=1)
#
# db.session.add(a1)
# db.session.add(a2)
# db.session.add(a3)
# db.session.add(a4)
# db.session.add(a5)
# db.session.add(a6)
# db.session.add(a7)
# db.session.add(a8)
# db.session.add(a9)
# db.session.commit()
#
# a1=Att(name='a',pa='P',datetime='2019-09-27 09:15:17.030035', reg_no=1)
# a2=Att(name='a',pa='P',datetime='2019-09-26 09:15:17.030035', reg_no=1)
# a3=Att(name='a',pa='P',datetime='2019-09-25 09:15:17.030035', reg_no=1)
# a4=Att(name='a',pa='P',datetime='2019-09-24 09:15:17.030035', reg_no=1)
# a5=Att(name='a',pa='P',datetime='2019-09-23 09:15:17.030035', reg_no=1)
# a6=Att(name='a',pa='P',datetime='2019-09-22 09:15:17.030035', reg_no=1)
# a7=Att(name='a',pa='P',datetime='2019-09-21 09:15:17.030035', reg_no=1)
# a8=Att(name='a',pa='P',datetime='2019-09-20 09:15:17.030035', reg_no=1)
# a9=Att(name='a',pa='P',datetime='2019-09-19 09:15:17.030035', reg_no=1)
#
# db.session.add(a1)
# db.session.add(a2)
# db.session.add(a3)
# db.session.add(a4)
# db.session.add(a5)
# db.session.add(a6)
# db.session.add(a7)
# db.session.add(a8)
# db.session.add(a9)
# db.session.commit()
#
#
# a1=Att(name='a',pa='P',datetime='2019-10-27 09:15:17.030035', reg_no=1)
# a2=Att(name='a',pa='P',datetime='2019-10-26 09:15:17.030035', reg_no=1)
# a3=Att(name='a',pa='P',datetime='2019-10-25 09:15:17.030035', reg_no=1)
# a4=Att(name='a',pa='P',datetime='2019-10-24 09:15:17.030035', reg_no=1)
# a5=Att(name='a',pa='P',datetime='2019-10-23 09:15:17.030035', reg_no=1)
# a6=Att(name='a',pa='P',datetime='2019-10-22 09:15:17.030035', reg_no=1)
# a7=Att(name='a',pa='P',datetime='2019-10-21 09:15:17.030035', reg_no=1)
# a8=Att(name='a',pa='P',datetime='2019-10-20 09:15:17.030035', reg_no=1)
# a9=Att(name='a',pa='P',datetime='2019-10-19 09:15:17.030035', reg_no=1)
#
# db.session.add(a1)
# db.session.add(a2)
# db.session.add(a3)
# db.session.add(a4)
# db.session.add(a5)
# db.session.add(a6)
# db.session.add(a7)
# db.session.add(a8)
# db.session.add(a9)
# db.session.commit()
#
# a1=Att(name='a',pa='P',datetime='2019-11-27 09:15:17.030035', reg_no=1)
# a2=Att(name='a',pa='P',datetime='2019-11-26 09:15:17.030035', reg_no=1)
# a3=Att(name='a',pa='P',datetime='2019-11-25 09:15:17.030035', reg_no=1)
# a4=Att(name='a',pa='P',datetime='2019-11-24 09:15:17.030035', reg_no=1)
# a5=Att(name='a',pa='P',datetime='2019-11-23 09:15:17.030035', reg_no=1)
# a6=Att(name='a',pa='P',datetime='2019-11-22 09:15:17.030035', reg_no=1)
# a7=Att(name='a',pa='P',datetime='2019-11-21 09:15:17.030035', reg_no=1)
# a8=Att(name='a',pa='P',datetime='2019-11-20 09:15:17.030035', reg_no=1)
# a9=Att(name='a',pa='P',datetime='2019-11-19 09:15:17.030035', reg_no=1)
#
# db.session.add(a1)
# db.session.add(a2)
# db.session.add(a3)
# db.session.add(a4)
# db.session.add(a5)
# db.session.add(a6)
# db.session.add(a7)
# db.session.add(a8)
# db.session.add(a9)
# db.session.commit()
#
# a1=Att(name='a',pa='P',datetime='2019-12-27 09:15:17.030035', reg_no=1)
# a2=Att(name='a',pa='P',datetime='2019-12-26 09:15:17.030035', reg_no=1)
# a3=Att(name='a',pa='P',datetime='2019-12-25 09:15:17.030035', reg_no=1)
# a4=Att(name='a',pa='P',datetime='2019-12-24 09:15:17.030035', reg_no=1)
# a5=Att(name='a',pa='P',datetime='2019-12-23 09:15:17.030035', reg_no=1)
# a6=Att(name='a',pa='P',datetime='2019-12-22 09:15:17.030035', reg_no=1)
# a7=Att(name='a',pa='P',datetime='2019-12-21 09:15:17.030035', reg_no=1)
# a8=Att(name='a',pa='P',datetime='2019-12-20 09:15:17.030035', reg_no=1)
# a9=Att(name='a',pa='P',datetime='2019-12-19 09:15:17.030035', reg_no=1)
# a10=Att(name='a',pa='P',datetime='2019-12-18 09:15:17.030035', reg_no=1)
#
# db.session.add(a1)
# db.session.add(a2)
# db.session.add(a3)
# db.session.add(a4)
# db.session.add(a5)
# db.session.add(a6)
# db.session.add(a7)
# db.session.add(a8)
# db.session.add(a9)
# db.session.add(a10)
# db.session.commit()


# SELECT  count(date), reg_no
# 	FROM public.attendance group by reg_no;
#
# SELECT  count(pa), date
# 	FROM public.attendance where reg_no=1 group by date;
#
#
# month = func.date_trunc('month', Att.datetime)
#
# x = db.session.query(func.count(Att.pa).label('Days'), month).group_by(month).first()
#
# db.session.query(func.count(Att.pa).label('Days'),
#                             extract('year', Att.datetime),
#                             extract('month',Att.datetime)).\
#     group_by(extract('year',Att.datetime),
#              extract('month', Att.datetime)).\
#     first()

#
# import pandas as pd
# import datetime
# from IntellFRS import db
# from sqlalchemy import extract
# from sqlalchemy import func
# from sqlalchemy.sql import label
# from IntellFRS.models1 import Att
#
# df= pd.read_sql(sql=db.session.query(Att).filter(Att.reg_no==1, Att.pa=='P').
#                                             with_entities(Att.datetime).statement, con=db.session.bind)
#
# df["datetime"] = pd.to_datetime(df["datetime"])
#
# counts= df.groupby([df['datetime'].dt.year.rename('year'), df['datetime'].dt.month.rename('month')]).agg({'count'})
# counts= df.groupby([df['datetime'].dt.month.rename('month')]).agg({'count'})
#
# c=counts.to_json(orient='columns')
# x=str(c)
# y=x[24:]
# z=jsonify({'data':y})
#

# df= pd.read_sql(sql=db.session.query(Attendance).filter(Attendance.reg_no==1, Attendance.pa=='P').
#                                             with_entities(Attendance.date).statement, con=db.session.bind)

# df["date"] = pd.to_datetime(df["date"])
# df.set_index('date').resample('M').size()
# counts= df.groupby([df['date'].dt.year.rename('year'), df['date'].dt.month.rename('month')]).agg({'count'})
#
#
#
# df['date_minus_time'] = df["date"].apply( lambda df :
# datetime.datetime(year=df.year, month=df.month, day=df.day))
# df.set_index(df["date_minus_time"],inplace=True)

# data = [
#
#         {Date:"1",present:"25"},{Date:"2",present:"26"}, {Date:"3",present:"27"}, {Date:"4",present:"28"},
#         {Date:"5",present:"28"},{Date:"6",present:"28"}, {Date:"7",present:"26"}, {Date:"8",present:"31"},
#         {Date:"9",present:"25"},{Date:"10",present:"21"},{Date:"11",present:"11"},{Date:"12",present:"31"}
# ];

# SELECT  count(date), reg_no
# 	FROM public.attendance group by reg_no;
#
# SELECT  count(pa), date
# 	FROM public.attendance where reg_no=1 group by date;
# import pandas as pd
# import datetime
# from IntellFRS import db
# from IntellFRS.models import Attendance, User
#
# df= pd.read_sql(sql=db.session.query(Attendance).filter(Attendance.reg_no==1, Attendance.pa=='P').
#                                             with_entities(Attendance.date).statement, con=db.session.bind)
# df["date"] = pd.to_datetime(df["date"])
# # df.set_index('date').resample('M').size()
# counts= df.groupby([df['date'].dt.year.rename('year'), df['date'].dt.month.rename('month')]).agg({'count'})
# c=counts.to_json(orient='columns')

#
#
# df['date_minus_time'] = df["date"].apply( lambda df :
# datetime.datetime(year=df.year, month=df.month, day=df.day))
# df.set_index(df["date_minus_time"],inplace=True)



# ///////////////////////////////////////////
# df= pd.read_sql(sql=db.session.query(Att).filter(Att.reg_no==1, Att.pa=='P').
#                                             with_entities(Att.datetime).statement, con=db.session.bind)
#
# df["datetime"] = pd.to_datetime(df["datetime"])
#
# counts= df.groupby([df['datetime'].dt.year.rename('year'), df['datetime'].dt.month.rename('month')]).agg({'count'})
# counts= df.groupby([df['datetime'].dt.month.rename('month')]).agg({'count'})
#
# c=counts.to_json(orient='columns')
# x=str(c)
# y=x[24:-1]
# # return jsonify({'data':y})
# return y
