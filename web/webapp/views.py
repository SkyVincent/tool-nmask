# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json
from public import *
from django.shortcuts import render
from django.http import HttpResponse
from plugins.core.info import tools_info
from plugins.kf import base64coding as bs64


class html(object):
	'''
	创建html页面
	'''
	def index(self,request):
		'''主页'''

		cur=tools_info()

		tool_type=request.GET.get("tool_type","")
		page=request.GET.get("page","1")

		if tool_type:
			tools_list=cur.tools_dicts.get(tool_type,[])
		else:
			tools_list=[]
			for i in cur.tools_dicts.values():
				tools_list+=i

		tools_list=sorted(tools_list, key=lambda number: number[8],reverse=True) #依据点赞数排序


		object_list,page_list,last_page=fenye(tools_list,page)


		return render(request,"index.html",{"tools_list":object_list,"page_list":page_list,"last_page":last_page})

	def about(self,request):
		'''关于我'''

		return render(request,"about.html")

	def comment(self,request):
		'''留言'''

		return render(request,"comment.html")

	def not_page(self,request):
		'''404 page '''

		return render(request,"404.html")

	def base64(self,request):
		'''base64 page'''

		return render(request,"base64.html")


class ajax_request(object):
	'''
	ajax请求工具功能
	'''

	def base64_ajax(self,request):
		'''base64 page'''

		content,c_type=get_request_method(request,"POST","content","type")

		if content and c_type=="encode":
			result=bs64.base64encode(content)
		elif content and c_type=="decode":
			result=bs64.base64decode(content)
		else:
			result=content

		return HttpResponse(json.dumps(result), content_type='application/json')



		