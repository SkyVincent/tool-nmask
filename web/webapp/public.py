#! -*- coding:utf-8 -*-

import json
from models import dianzan_table
from django.http import HttpResponse
from django.shortcuts import render
from plugins.core.info import tools_info
from django.core.paginator import Paginator



def fenye(objects,page):
	'''数据表分页'''
	try:
		page=int(page)
	except:
		page=1

	p = Paginator(objects, 12)

	page_range=p.page_range

	last_page=len(page_range)

	if page>last_page:
		page=1

	page1 = p.page(page)

	object_list=page1.object_list

	return object_list,page_range,last_page


def get_request_method(request,method,*args):
	'''解析GET、POST参数'''

	if method=="GET":
		re_p=request.GET
	else:
		re_p=request.POST

	result=[re_p.get(i,"") for i in args]

	return result

def dianzan(request):
	'''点赞功能'''

	modename=get_request_method(request,"POST","modename")[0]

	# print "modename is ",modename

	response = dianzan_table.objects.filter(tool_name=modename)

	if len(response)>0:

		''' 更新表 '''
		response = dianzan_table.objects.get(tool_name=modename)
		response.number+=1
		response.save()
	
	return HttpResponse(json.dumps(response.number), content_type='application/json')


def search(request):
	'''搜索工具'''
	
	tools_list=[]
	cur=tools_info()

	toolname=request.POST.get("toolname","")

	toolname=toolname.lower().encode("utf-8")
	
	if toolname:
		for i in cur.tools_dicts.values():
			for n in i:
				name=n[1].lower()
				command=n[2].lower()
				if toolname in name or toolname in command:
					tools_list.append(n)

	tools_list=sorted(tools_list, key=lambda number: number[4],reverse=True) #依据点赞数排序

	return render(request,"index.html",{"tools_list":tools_list})

