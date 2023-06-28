import os
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, Boolean, event
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import Session, relationship, backref
import time

# 获取当前时间戳
start_time = time.time()

# 检查数据库是否存在
if os.path.exists('stgy.db'):
    # 如果存在，删除数据库文件
    os.remove('stgy.db')

# 创建数据库引擎
engine = create_engine('sqlite:///stgy.db', echo=True)

# 创建 Session 对象
Session = sessionmaker(bind=engine)
session = Session()

# 创建基类
Base = declarative_base()


# 曲线模板 数据表
class PlanCurveTmpl(Base):
    __tablename__ = 'plan_curve_tmpl'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    # inst = relationship('PlanCurveInst', back_populates=backref('inst'))
    # detail = relationship('PlanCurveDetail', back_populates=backref('detail'))

    def insert_data(self, db: Session):
        db.add(self)
        db.commit()
        db.refresh(self)
        return self


# 曲线实例 数据表
class PlanCurveInst(Base):
    __tablename__ = 'plan_curve_inst'

    id = Column(Integer, primary_key=True)
    enable = Column(Boolean, default=False)
    curve_id = Column(Integer)
    start_date = Column(DateTime, default=datetime.now().date())
    end_date = Column(DateTime, default=datetime.now().date())

    def insert_data(self, db: Session):
        db.add(self)
        db.commit()
        db.refresh(self)
        return self

# # 创建触发器
# @event.listens_for(PlanCurveInst.enable, 'set')
# def set_enable(target, value, oldvalue, initiator):
#     if value == 1:
#         session.query(PlanCurveInst).filter(PlanCurveInst.enable == 1).update({PlanCurveInst.enable: 0})
#         session.commit()


# 曲线详情 数据表
class PlanCurveDetail(Base):
    __tablename__ = 'plan_curve_detail'

    curve_id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, default=datetime.now().date())
    end_time = Column(DateTime, default=datetime.now().date())
    power = Column(Float, default=0.0)

    def insert_data(self, db: Session):
        db.add(self)
        db.commit()
        db.refresh(self)
        return self


Base.metadata.create_all(engine)

# 关闭 Session 对象
session.close()

# 获取当前时间戳
end_time = time.time()

# 计算执行时间
elapsed_time = end_time - start_time

print("代码执行时间：{:.2f} 秒".format(elapsed_time))
