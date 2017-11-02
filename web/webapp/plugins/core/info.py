#! -*-  coding:utf-8 -*-

import time
import sys
sys.path.append("..")
from webapp.models import dianzan_table

#### 域名信息

host="http://127.0.0.1:8000/"

#### 未开放功能名单

tool_black=["des"] 

#### 工具信息

tool_info={

	"kf":{
		"base64":("base64编码","对字符串进行base64编码，或者进行base64解码","2017.09.12"),
	},

	"sec":{

	},

	"ctf":{

	},

	"yw":{

	},

	"other":{
	},
}

#### 工具类别

tool_type={

	"kf":u"开发类",
	"sec":u"安全类",
	"ctf":u"CTF",
	"yw":u"运维类",
	"other":u"其他",
}

#### 类别对应的颜色

type_color={

	"kf":"list-group-item-info",
	"sec":"list-group-item-danger",
	"ctf":"list-group-item-warning",
	"yw":"list-group-item-success",
	"other":"list-group-item-success",
}



class tools_info(object):
	'''
	工具类别:[(0工具模块名称，1工具显示名称，2功能描述，3对应的url地址，4点赞数 ，5所属类别，6所属类别中文，7颜色，8上线日期，9new_tag，10hot_tag)]
	'''
	
	def __init__(self):
		
		self.tools_dicts={}

		self.get_tool_info()

	
	def get_tool_info(self):

		'''获取全部工具的信息'''

		for t_type in tool_info.keys():
			t_info=tool_info[t_type]
			tu_list=[]
			for t_name in t_info.keys():
				v=t_info[t_name]
				tup=(t_name,v[0],v[1].decode("utf-8")[:35])+self.toolinfo(t_name)+self.typeinfo(t_type)+(v[2],self.con_time(v[2]),self.con_dianzan(t_name))
				tu_list.append(tup)

			self.tools_dicts[t_type]=tu_list


	def typeinfo(self,name):
		'''工具类别的信息'''

		return name,tool_type.get(name),type_color.get(name)


	def toolinfo(self,name):
		'''工具部分信息'''

		return self.url(name),self.search_dianzan(name)


	def url(self,name):
		'''生成url'''

		if name in tool_black:
			return "#myModal"
		else:
			return host+name+"/"

	def con_time(self,date):
		'''计算上线了多长时间'''

		s = time.mktime(time.strptime(date,'%Y.%m.%d'))
		n=time.time()
		c=n-s

		if c>604800:  #一周以内的标记为"新"
			return ""
		else:
			return "新"

	def con_dianzan(self,name):
		'''计算点赞数大于多少后，显示为火热'''

		num=self.search_dianzan(name)

		if num>10:
			return "热"
		else:
			return ""


	def search_dianzan(self,modename):
		'''统计点赞数'''

		d = dianzan_table.objects.filter(tool_name=modename)
		if len(d)==0:
			'''新增字段'''
			response = dianzan_table(tool_name=modename,number=0)
			response.save()
			number = 0
		else:
			number = d[0].number

		return number
