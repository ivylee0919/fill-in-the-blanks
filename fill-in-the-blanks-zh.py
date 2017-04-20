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

quiz_all = {'简单': quiz_easy,
			'中等': quiz_medium,
			'困难':quiz_hard}
blank = ['___1___','___2___','___3___','___4___']

#让玩家输入题目难度，限定格式
def choose_level():
	'''让玩家输入题目难度，限定格式，返回难度'''
	while True:
		level = raw_input('请选择题目难度：简单、中等、困难\n')
		if level not in ['简单','中等','困难']:
			print '您输入的难度格式不正确！:(\n'
		else:
			return level

#让玩家输入错误次数，限定格式
def error_times_max():
	'''让玩家输入错误次数，限定格式，格式正确则返回'''
	while True:
		error_max_input = raw_input('请选择答错次数上限（1-9），超过上限答题失败！\n')
		error_max = int(error_max_input)
		if error_max not in [1,2,3,4,5,6,7,8,9]:
			print '您输入的格式不正确！:(\n'
		else:
			return error_max


def replace(quiz, blank):
	'''输入当前题目和答案序号，将题目对应空白处替换为正确答案，
	并返回替换答案后的题目'''
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

def guess(quiz, blank_num, error_max):
	'''传入题目，空位，最大答错次数，玩家输入答案，判断对错
	返回玩家答错次数。'''
	error_num = 0
	while error_num <= error_max:
		answer = raw_input('\nn请输入'+ blank_num +'可能的词：\n')
		if answer != quiz_current[blank_num]:
			error_num += 1
			print '很遗憾你答错了！再试一下！\n'
		else:
			if blank_num == '___4___':
				print '恭喜你完成所有填空！撒花！\n'
			else:
				print '恭喜你答对了！继续下一空！\n'
			break
	return error_num


#开始游戏
quiz_current = quiz_all[choose_level()]
error_max = error_times_max()

for e in blank:
	#展示当前题目
	print '当前题目：\n\n' + quiz_current['topic']
	#输入答案判断对错，记录错误次数
	error_num = guess(quiz_current, e, error_max)
	#判断是否达到最大错误次数，没有达到就是回答正确
	if error_num <= error_max:
		#回答正确，替换空位
		quiz_current = replace(quiz_current, e)
		
	else:
		#回答错误，结束游戏
		print '错误次数已达上限，答题失败T__T\n'
		break
