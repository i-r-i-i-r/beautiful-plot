# プロット用関数の使用例

# モジュールのインポート
import os
import numpy as np
from plot.plot import make_plot, make_scatter

main_path   = os.getcwd()
output_path = main_path  + '\\output_plot'
os.makedirs(output_path, exist_ok=True) # ない場合は作る
os.chdir(output_path)

x1_data  = np.linspace(0,10,26)
y1_data = np.sin(x1_data)
y2_data = np.cos(x1_data)
y3_data = x1_data*0.25-1.25
y4_data = -x1_data*0.25+1.25
y5_data = x1_data*0
y6_data = x1_data*0+1
y7_data = x1_data*0-1
x_data01 = np.linspace(0,10,26)
x_data02 = np.linspace(-5,5,26)
x_data03 = np.linspace(0,20,6)
y_data01 = np.sin(x_data01)
y_data02 = np.sin(x_data02)*0.5
y_data03 = np.sin(x_data03)*1.2

# 1
make_plot(x1_data, y1_data, "ex1" )
# 2
make_plot(x1_data, [y1_data,y2_data,y3_data,y4_data,y5_data,y6_data], "ex2" )
# 3
make_plot(x1_data, [y1_data,y2_data,y3_data,y4_data,y5_data,y6_data,y7_data], "ex3" )
# 4
make_plot(x1_data, [y1_data,y2_data], "ex4", color=["green", "deepskyblue"], marker=["+", "None"],
          line_style=["None", "-"], label=["time [s]", "position [m]"], ylim=[-5,3], title="title", 
          grid=True, plot_area=[5, 2], axis_format=["%.0f","%.2f"] )
# 5
make_plot([x_data01, x_data02, x_data03], [y_data01, y_data02, y_data03], "ex5" )
# 6
make_scatter(y1_data, y2_data, "ex6" )
