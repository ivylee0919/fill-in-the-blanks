
# IPND Stage 2 Final Project

import locale
_, code = locale.getdefaultlocale()

quiz_easy = {u'题目': u'白日依___1___尽，黄河入___2___流。欲___3___千里目，___4___上一层楼。',
'___1___': u'山',
'___2___': u'海',
'___3___': u'穷',
'___4___': u'更'}
quiz_medium = {u'题目': u'红豆生___1___，___2___发几枝。愿君多___3___，此物最___4___。',
'___1___': u'南国',
'___2___': u'春来',
'___3___': u'采撷',
'___4___': u'相思'}
quiz_hard = {u'题目': u'岐王宅里___1___见，崔九___2___几度闻。正是江南___3___，___4___又逢君。',
'___1___': u'寻常',
'___2___': u'堂前',
'___3___': u'好风景',
'___4___': u'落花时节'}

quiz_all = {u'简单': quiz_easy,
			u'中等': quiz_medium,
			u'困难': quiz_hard}
blank = ['___1___','___2___','___3___','___4___']

#让玩家输入题目难度，限定格式
def choose_level():
	u'''让玩家输入题目难度，限定格式，返回难度'''
	while True:
		level = raw_input(u'\n请选择题目难度：简单、中等、困难\n'.encode(code)).decode(code)
		if level not in [u'简单',u'中等',u'困难']:
			print u'\n您输入的难度格式不正确！(#`O′)\n'.encode(code)
		else:
			return level

#让玩家输入错误次数，限定格式
def error_times_max():
	u'''让玩家输入错误次数，限定格式，格式正确则返回'''
	while True:
		error_max_input = raw_input(u'\n请选择答错次数上限（1-9），超过上限答题失败！⊙﹏⊙∥\n'.encode(code)).decode(code)
		error_max = int(error_max_input)
		if error_max not in [1,2,3,4,5,6,7,8,9]:
			print u'\n您输入的格式不正确！(#`O′)\n'.encode(code)
		else:
			return error_max


def replace(quiz, blank):
	u'''输入当前题目和答案序号，将题目对应空白处替换为正确答案，
	并返回替换答案后的题目'''
	quiz_old = quiz[u'题目']
	quiz_new = ''
	i = 0
	while i<=(len(quiz_old)-7):
		if quiz_old[i:i+7] == blank:
			quiz_new += quiz[blank]
			i += 7
		else:
			quiz_new += quiz_old[i]
			i += 1
	quiz_new += quiz_old[i:]
	quiz[u'题目'] = quiz_new
	return quiz

def guess(quiz, blank_num, error_max):
	u'''传入题目，空位，最大答错次数，玩家输入答案，判断对错
	返回玩家答错次数。'''
	error_num = 0
	while error_num <= error_max:
		answer = raw_input((u'\n请输入'+ blank_num +u'可能的词：\n').encode(code)).decode(code)
		if answer != quiz[blank_num]:
			error_num += 1
			print u"\n很遗憾你答错了！::>_<::\n剩余答题次数为：".encode(code) + str(error_max - error_num + 1)
		else:
			if blank_num == '___4___':
				print u'\n恭喜你完成所有填空！*★,°*:.☆(￣▽￣)/$:*.°★* 。\n'.encode(code)
			else:
				print u'\n恭喜你答对了！继续下一空！\^o^/\n'.encode(code)
			break
	return error_num


#开始游戏
def main():
	quiz_current = quiz_all[choose_level()]
	error_max = error_times_max()

	for e in blank:
		#展示当前题目
		print (u'\n当前题目：\n\n' + quiz_current[u'题目']).encode(code)
		#输入答案判断对错，记录错误次数
		error_num = guess(quiz_current, e, error_max)
		#判断是否达到最大错误次数，没有达到就是回答正确
		if error_num <= error_max:
			#回答正确，替换空位
			quiz_current = replace(quiz_current, e)
			error_max = error_max - error_num

		else:
			#回答错误，结束游戏
			print u'\n错误次数已达上限，答题失败/(ㄒoㄒ)/~~\n'.encode(code)
			break
	
	print (u'\n你最终完成的题目如下：\n\n' + quiz_current[u'题目']).encode(code)

if __name__ == '__main__':
	main()

