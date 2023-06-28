from datetime import datetime

from sqlalchemy.orm import sessionmaker
import create_stgydb
import csv
import time
import sys

# 获取当前时间戳
start_time = time.time()

# 创建 Session 对象
Session = sessionmaker(bind=create_stgydb.engine)
session = Session()

# 向 曲线模板 数据表插入数据
tmpl1 = create_stgydb.PlanCurveTmpl(
    name='曲线模板1',
)
tmpl2 = create_stgydb.PlanCurveTmpl(
    name='曲线模板2',
)
tmpl3 = create_stgydb.PlanCurveTmpl(
    name='曲线模板3',
)
tmpl4 = create_stgydb.PlanCurveTmpl(
    name='曲线模板4',
)
tmpl5 = create_stgydb.PlanCurveTmpl(
    name='曲线模板5',
)
session.bulk_save_objects([tmpl1, tmpl2, tmpl3, tmpl4, tmpl5])

# 向 曲线实例 数据表插入数据
inst1 = create_stgydb.PlanCurveInst(
    enable=True,
    curve_id=1,
    start_date=datetime.strptime('2023-06-22', '%Y-%m-%d'),
    end_date=datetime.strptime('2023-06-22', '%Y-%m-%d'),
)
inst2 = create_stgydb.PlanCurveInst(
    enable=False,
    curve_id=2,
    start_date=datetime.strptime('2023-06-23', '%Y-%m-%d'),
    end_date=datetime.strptime('2023-06-23', '%Y-%m-%d'),
)
inst3 = create_stgydb.PlanCurveInst(
    enable=False,
    curve_id=3,
    start_date=datetime.strptime('2023-06-24', '%Y-%m-%d'),
    end_date=datetime.strptime('2023-06-24', '%Y-%m-%d'),
)
inst4 = create_stgydb.PlanCurveInst(
    enable=False,
    curve_id=4,
    start_date=datetime.strptime('2023-06-25', '%Y-%m-%d'),
    end_date=datetime.strptime('2023-06-25', '%Y-%m-%d'),
)
inst5 = create_stgydb.PlanCurveInst(
    enable=False,
    curve_id=5,
    start_date=datetime.strptime('2023-06-26', '%Y-%m-%d'),
    end_date=datetime.strptime('2023-06-26', '%Y-%m-%d'),
)
session.bulk_save_objects([inst1, inst2, inst3, inst4, inst5])

# 向 曲线详情 数据表插入数据
detail1 = create_stgydb.PlanCurveDetail(
    curve_id=1,
    start_time=datetime.strptime('00:00', '%H:%M').time(),
    end_time=datetime.strptime('23:59', '%H:%M').time(),
    power=111,
)
detail2 = create_stgydb.PlanCurveDetail(
    curve_id=2,
    start_time=datetime.strptime('00:00', '%H:%M').time(),
    end_time=datetime.strptime('23:59', '%H:%M').time(),
    power=222,
)
detail3 = create_stgydb.PlanCurveDetail(
    curve_id=3,
    start_time=datetime.strptime('00:00', '%H:%M').time(),
    end_time=datetime.strptime('23:59', '%H:%M').time(),
    power=333,
)
detail4 = create_stgydb.PlanCurveDetail(
    curve_id=4,
    start_time=datetime.strptime('00:00', '%H:%M').time(),
    end_time=datetime.strptime('23:59', '%H:%M').time(),
    power=444,
)
detail5 = create_stgydb.PlanCurveDetail(
    curve_id=5,
    start_time=datetime.strptime('00:00', '%H:%M').time(),
    end_time=datetime.strptime('23:59', '%H:%M').time(),
    power=555,
)
session.bulk_save_objects([detail1, detail2, detail3, detail4, detail5])

# 提交事务
session.commit()

# 关闭 Session 对象
session.close()

# 获取当前时间戳
end_time = time.time()

# 计算执行时间
elapsed_time = end_time - start_time

print("代码执行时间：{:.2f} 秒".format(elapsed_time))
