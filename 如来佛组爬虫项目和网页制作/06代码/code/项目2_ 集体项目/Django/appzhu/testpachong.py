# -*- encoding:utf-8 -*-
# @Time : ${08} ${08}
# @Author : 朱冰
# @Site : ${Xi‘an}
# @File : ${What to by}.py
# @Software: ${PRODUCT_NAME
# 面向函数编程
# 存入excel的

import re, requests, xlwt, lxml
import time
from collections import Counter

from lxml import etree
import logging
import xlrd
from xlutils.copy import copy
import sys
import pymysql
import traceback
from appzhu import zhubingpachong

# a=zhubingpachong.getlistmain()
# b=a[1]
# c=dict(b)
# print(a[1])
# print(type(b))
# print(type(c))
# print(c)
# m=c.keys()
# print(type(m))
data=['GUERLAIN','DIOR','ESTEELAUDER','GIVENCHY','MAKEUPFOREVER','LANCOME','BENEFIT','Fresh','LOEWE','SEPHORACOLLECTION','SK-II','GUCCI','BOBBIBROWN','FOREO','MIUMIU','SHUUEMURA','CAUDALIE','WEI','BURBERRY','SHISEIDO'],
print(len(data))



# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"  # 日志格式化输出
# DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"  # 日期格式
# fp = logging.FileHandler('zhu-debug-log.txt', encoding='utf-8')
# fs = logging.StreamHandler()
# logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])  # 调用
#
# try:
#     def fun_crawler(website):
#
#         while True:  # 一直循环，直到访问站点成功
#             try:
#                 url1 = website
#                 headers = {
#                     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
#                 }
#                 response_1 = requests.get(url1, headers=headers, timeout=10)  # 通过捕获然后等待网络情况的变化，以此来保护程序的不间断运行
#                 break
#                 # 以下except都是用来捕获当requests请求出现异常时，
#             except requests.exceptions.ConnectionError:
#                 print('ConnectionError -- please wait 3 seconds')
#                 time.sleep(3)
#             except requests.exceptions.ChunkedEncodingError:
#                 print('ChunkedEncodingError -- please wait 3 seconds')
#                 time.sleep(3)
#             except:
#                 print('Unfortunitely -- An Unknow Error Happened, Please wait 3 seconds')
#                 time.sleep(3)
#         response_1.encoding = 'utf-8'
#         # print(response_1.text)
#         return response_1.text
# # 函数出现错误时显示输出
# except Exception as e:
#     logging.error('执行函数fun_crawler', exc_info=True)
#
# # 获得requests得到网页参数；解析网页获取商品名称，价格；将名称与价格作为返回值作为输出参数
# try:
#     def fun_web_analyse(webcontent):
#
#         response_1 = webcontent  # 获取网页list
#         res_xpath = etree.HTML(response_1)  # 获得xpath，开始解析网页
#         var_html_namesource_text = res_xpath.xpath('//div[@class="p_productCN"]//a[@target="_blank"]/text()')  # 获取商品名字
#         var_html_price_text = res_xpath.xpath('//div [@class="p_discount commonFontPrice"]/text()')  # 获取商品价格
#         var_html_website = res_xpath.xpath('//div[@class="p_productCN"]//a[@target="_blank"]/@href')  # 获取商品链接
#         var_html_imgsrc = res_xpath.xpath('//div[@class="p_img"]//a[@target="_blank"]//img/@src')
#         var_html_brand = res_xpath.xpath('//div[@class="p_brandEn"]/text()')
#
#         # var_html_brand = res_xpath.xpath('//li[@class="brands_li"]//img/@src')
#
#         return var_html_namesource_text, var_html_price_text, var_html_website,var_html_imgsrc,var_html_brand  #var_html_brand # 返回价格,名称
#         # print(var_html_namesource_text)
#         # print(var_html_brand)
#
# except Exception as e:
#     logging.error('fun_web_analyse', exc_info=True)
#     # logging.error('fun_web_analyse')
#
# # 使用循环爬取多个网页的内容
# var_webnum = 4
# list_01 = var_webnum * [0]
# list_webenum = var_webnum * [0]
# list_web_content = var_webnum * [0]
# list_web_price = []
# list_web_name = []
# var_list_data = []
# var_list_coll = []
# var_list_brands = []
# list_web_brand = []
#
# # 大循环：向多个website请求，并获得网页内容，并将其作为的解析网页的输入
# def getlistmain():
#     for i in range(len(list_01)):
#         list_webenum[i] = 'https://www.sephora.cn/hot/?k=%E7%95%85%E9%94%80%E6%A6%9C%E5%8D%95&hasInventory=0&sortField=1&sortMode=desc&currentPage=' + str(
#         i + 1) + '&filters='
#         website = list_webenum[i]  # 调用爬取网页的函数前将参数赋值
#         list_web_content[i] = fun_crawler(website)  # 调用爬取网页的函数,调用之后变量list_web_content中以列表的形式保存多个网页
#         webcontent = list_web_content[i]  # 准备调用网页解析函数,在调用网页解析函数之前将list中每个元素(代表每个网页的内容)保存
#         f_web_analys = fun_web_analyse(webcontent)  # 将解析出的结果保存
#         sublist_web_name = f_web_analys[0]  # 得到变量
#         sublist_web_price = f_web_analys[1]
#         sublist_web_website = f_web_analys[2]
#         sublist_web_imgsrc = f_web_analys[3]
#         sublist_web_brand=f_web_analys[4]
#         # list_web_brand.append(sublist_web_brand)
#         # print(list_web_brand)
#
#
#         var_normhtml_price_text = []
#         var_normprice=[]
#         for j in range(len(sublist_web_price)):  # 与产品名称类似
#             result = '~' in sublist_web_price[j]
#             if result == False:
#                 var_normhtml_price_text.append(sublist_web_price[j])
#                 # a = var_normhtml_price_text
#             else:
#                 var_normhtml_price_text.append(sublist_web_price[j - 1] + sublist_web_price[j])
#                 var_normprice = var_normhtml_price_text
#                 del var_normprice[len(var_normprice) - 2]  # 在新列表中删除重复元素
#      # 存入excel
#         for j in range(len(sublist_web_name)):
#             var_list_coll.append([i*len(sublist_web_name)+j+1,sublist_web_brand[j],sublist_web_name[j], var_normprice[j],sublist_web_website[j],sublist_web_imgsrc[j]])
#             var_list_brands.append(sublist_web_brand[j])
#     # print(var_list_brands)
#     # print(var_list_coll)
#
#     var_dict_brandsRST=Counter(var_list_brands)
#     print(var_dict_brandsRST)
#
#     return var_list_coll#切记return是一个函数结束的标志
#
#
#
# # getlistmain()
# #
#
#
#
#
#
#
