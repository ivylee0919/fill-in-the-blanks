# -*- coding: utf-8 -*-

# IPND Stage 2 Final Project

quiz_easy = {'topic': '''So now we know some ways to make comparisons. We want
to use them to make decisions, to make our code do something different,
depending on the result of a comparison. The way to do that is to use an
"___1___" statement. The structure of an "___1___" statement is: we have the
keyword, "___1___", followed by a comparison, we\'ll call that the ___2___
expression, followed by a ___3___. And then, inside the "___1___", we have the
___4___, and the ___4___ is the code that will run when the ___2___ expression
is True.''',
'___1___': 'if',
'___2___': 'test',
'___3___': 'colon',
'___4___': 'block'}
quiz_medium = {'topic': '''The construct we are gonna introduce is called a
___1___. It's a way to do things over and over again. The kind of ___1___ that
we are gonna introduce first is called the ___2___ ___1___. The syntax for the
___2___ ___1___ is this. We have the key word "___2___", followed by a test
expression and the "block" is a sequence of instructions. With a "___2___", we
also start by checking the test expression if it's "___3___", we go to the
block, after the block, we go back to try the test expression again, if it's
"___3___", we go back to the block. we can keep going around as many times as
we need as long as the test expression is "___3___". At some point, maybe the
test expression is "___4___", we go to the next instruction.''',
'___1___': 'loop',
'___2___': 'while',
'___3___': 'True',
'___4___': 'False'}
quiz_hard = {'topic': '''Python provides a simpler way to loop through elements of the ___2___, and that's called a ___1___-loop. The structure of a ___1___-loop is like this. We have the keyword ___1___ followed by a name, and this is a new name ___1___ a variable that we can introduce, then the keyword in followed by a ___2___, and this is any expression which evaluates to a ___2___ followed by a ___3___. So this is quite similar to what we've seen ___1___ the structure of a while loop and an if statement with a ___4___ inside the ___1___. What a ___1___-loop like this means is that ___1___ each element in the ___2___ we're going to assign that element to the name and evaluate the ___4___.''',
'___1___': 'for',
'___2___': 'list',
'___3___': 'colon',
'___4___': 'block'}

quiz_all = {}
quiz_all['easy'] = quiz_easy
quiz_all['medium'] = quiz_medium
quiz_all['hard'] = quiz_hard

#让玩家输入题目难度，限定格式
while True:
	level = raw_input('Please select the topic of difficulty: easy, medium or hard\n')
	if level not in ['easy','medium','hard']:
		print 'Your input is not correct!:(\n'
	else:
		break
#让玩家输入错误次数，限定格式
while True:
	error_max_input = raw_input('Please select the maximum number of wrong answers: 1-9\n')
	error_max = int(error_max_input)
	if error_max not in [1,2,3,4,5,6,7,8,9]:
		print 'Your input is not correct!:(\n'
	else:
		break


def replace(quiz, blank):
	#输入当前题目和答案序号，将题目对应空白处替换为正确答案，
	#并返回替换答案后的题目
	quiz_old = quiz['topic']
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
	quiz['topic'] = quiz_new
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
	print 'The question is: \n\n' + quiz_current['topic']
	#错误次数上限内，使玩家输入答案，判断是否答对
	while error_num <= error_max:
		answer = raw_input('\nPlease type in '+ e +' possible words:\n')
		if answer != quiz_current[e]:
			error_num += 1
			print 'I\'m sorry you got it wrong!\n'
		else:
			#答对后退出while循环，进行下一个空位答题
			if e == '___4___':
				print 'Congratulations! You have finished the quiz!\n'
			else:
				print 'Great job!\n'
			break
	#while 循环结束后，判断是因为答对还是错误达到上限
	if error_num <= error_max:
		#答对则用答案替换掉空位
		quiz_current = replace(quiz_current, e)
		error_num = 0
	else:
		#答错次数上限，退出程序
		print 'You have reached the maximum number of mistakes!T__T\n'
		break
