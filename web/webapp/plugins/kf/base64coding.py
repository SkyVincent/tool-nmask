#! -*- coding:utf-8 -*-

'''base64 coding '''

import base64


def base64encode(content):
	try:
		content = base64.b64encode(content)
	except TypeError:
		pass

	return content



def base64decode(content):
	try:
		content = base64.b64decode(content)
	except TypeError:
		pass

	return content



if __name__=="__main__":
	content=base64encode("http://www.baidu.com/<><>")
	print content
	content=base64decode(content)
	print content