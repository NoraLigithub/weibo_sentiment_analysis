# -*- coding: utf-8 -*-


import weibo_dict_senti_analysis as wdsa
import matplotlib.pyplot as plt

import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")


def dict_analysis_pot1():
	result_dict = wdsa.main()
	labels = 'Positive:%s' % result_dict['pos_number'], 'Negative:%s' % result_dict['neg_number'], 'Objective:%s' %  result_dict['mid_number'] 
	colors = ('#9999ff','#ff9999', '#CC0000')
	explode = (0, 0.05, 0.05)
	pietitle = "weibo's dict analyis" 
	dic_res=[result_dict['pos_number'], result_dict['neg_number'],result_dict['mid_number'] ]
	weiboPieChart(pielist=dic_res, labels=labels, explode=explode, colors=colors, pietitle=pietitle)


font = {'family' : 'serif',  
        'color'  : 'black',  
        'weight' : 'normal',  
        'size'   : 24,  
        }  
def weiboPieChart(pielist, labels, explode, colors, pietitle):
	# make a square figure and axes
	plt.figure(1, figsize=(8.1,7.5)) # 图形的size，这里图形指的是边界
	ax = plt.axes([0.1, 0.1, 0.8, 0.8]) # 图形的size，指的是里面的内容
	# pielist :# 每一块占得比例，总和为100
	plt.pie(pielist, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, colors=colors)
	plt.title(pietitle,fontdict=font)
	plt.show()

if __name__ == '__main__':
	dict_analysis_pot1()