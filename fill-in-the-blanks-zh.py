# -*- coding: utf-8 -*-

# IPND Stage 2 Final Project

quiz_easy = {'题目': '白日依___1___尽，黄河入___2___流。欲___3___千里目，___4___上一层楼。',
'___1___': '山',
'___2___': '海',
'___3___': '穷',
'___4___': '更'}
quiz_medium = {'题目': '红豆生___1___，___2___发几枝。愿君多___3___，此物最___4___。',
'___1___': '南国',
'___2___': '春来',
'___3___': '采撷',
'___4___': '相思'}
quiz_hard = {'题目': '岐王宅里___1___见，崔九___2___几度闻。正是江南___3___，___4___又逢君。',
'___1___': '寻常',
'___2___': '堂前',
'___3___': '好风景',
'___4___': '落花时节'}

quiz_all = {}
quiz_all['简单'] = quiz_easy
quiz_all['中等'] = quiz_medium
quiz_all['困难'] = quiz_hard

#让玩家输入题目难度，限定格式
while True:
	level = raw_input('请选择题目难度：简单、中等、困难\n')
	if level not in ['简单','中等','困难']:
		print '您输入的难度格式不正确！:(\n'
	else:
		break
#让玩家输入错误次数，限定格式
while True:
	error_max_input = raw_input('请选择答错次数上限（1-9），超过上限答题失败！\n')
	error_max = int(error_max_input)
	if error_max not in [1,2,3,4,5,6,7,8,9]:
		print '您输入的格式不正确！:(\n'
	else:
		break


def replace(quiz, blank):
	#输入当前题目和答案序号，将题目对应空白处替换为正确答案，
	#并返回替换答案后的题目
	quiz_old = quiz['题目']
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
	quiz['题目'] = quiz_new
	return quiz


#题目中的填空
blank = ['___1___','___2___','___3___','___4___']
#答错次数
error_num = 0
#玩家所选难度的对应题目
quiz_current = quiz_all[level]

#对 blank 中的每一个空位编号处理：
for e in blank:
	#展示当前题目
	print '当前题目：\n' + quiz_current['题目']
	#错误次数上限内，使玩家输入答案，判断是否答对
	while error_num <= error_max:
		answer = raw_input('\n请输入'+ e +'可能的词：\n')
		if answer != quiz_current[e]:
			print '很遗憾你答错了！\n'
			error_num += 1
		else:
			#答对后退出while循环，进行下一个空位答题
			print '恭喜你答对了！\n'
			break
	#while 循环结束后，判断是因为答对还是错误达到上限
	if error_num <= error_max:
		#答对则用答案替换掉空位
		quiz_current = replace(quiz_current, e)
	else:
		#答错次数上限，退出程序
		print '错误次数已达上限，答题失败T__T\n'
		break
