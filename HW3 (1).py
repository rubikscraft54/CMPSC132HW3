#HW3
#Due Date: 11/03/2019, 11:59PM 
'''
Team members:

Collaboration Statement:             

'''
import re

class Node:
	def __init__(self, value):
		self.value = value  
		self.next = None 
	
	def __str__(self):
		return "Node({})".format(self.value) 

	__repr__ = __str__
						  

#=============================================== Part I ==============================================

class Stack:
	'''
		>>> x=Stack()
		>>> x.pop()
		>>> x.push(2)
		>>> x.push(4)
		>>> x.push(6)
		>>> x
		Top:Node(6)
		Stack:
		6
		4
		2
		>>> x.pop()
		6
		>>> x
		Top:Node(4)
		Stack:
		4
		2
		>>> len(x)
		2
		>>> x.peek()
		4
	'''
	def __init__(self):
		self.top = None
		self.count=0
	
	def __str__(self):
		temp=self.top
		out=[]
		while temp:
			out.append(str(temp.value))
			temp=temp.next
		out='\n'.join(out)
		return ('Top:{}\nStack:\n{}'.format(self.top,out))

	__repr__=__str__

	def isEmpty(self):
		if self.count == 0:
			return True
		else:
			return False

	def __len__(self): 
		return self.count

	def push(self,value):
		new = Node(value)
		new.next = self.top
		self.top = new
		self.count += 1
	 
	def pop(self):
		if self.isEmpty():
			return None
		else:
			top = self.top
			newTop = top.next
			self.top = newTop
			top.next = None
			self.count -= 1
			return top.value

	def peek(self):
		return self.top.value

#=============================================== Part II ==============================================

class Calculator:
	def __init__(self):
		self.expr = None


	def isNumber(self, txt):
		try:
			txt = float(txt)
			return True
		except ValueError:
			return False


	def postfix(self, txt):
		'''
			Required: postfix must create and use a Stack for expression processing
			>>> x=Calculator()
			>>> x.postfix(' 2 ^        4')
			'2.0 4.0 ^'
			>>> x.postfix('2')
			'2.0'
			>>> x.postfix('2.1*5+3^2+1+4.45')
			'2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
			>>> x.postfix('    2 *       5.34        +       3      ^ 2    + 1+4   ')
			'2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
			>>> x.postfix(' 2.1 *      5   +   3    ^ 2+ 1  +     4')
			'2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
			>>> x.postfix('(2.5)')
			'2.5'
			>>> x.postfix ('((2))')
			'2.0'
			>>> x.postfix ('     -2 *  ((  5   +   3)    ^ 2+(1  +4))    ')
			'-2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
			>>> x.postfix ('  (   2 *  ((  5   +   3)    ^ 2+(1  +4)))    ')
			'2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
			>>> x.postfix ('  ((   2 *  ((  5   +   3)    ^ 2+(1  +4))))    ')
			'2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
			>>> x.postfix('   2 *  (  5   +   3)    ^ 2+(1  +4)    ')
			'2.0 5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'
			>>> x.postfix('2 *    5   +   3    ^ -2       +1  +4')
			'error message'
			>>> x.postfix('2    5')
			'error message'
			>>> x.postfix('25 +')
			'error message'
			>>> x.postfix('   2 *  (  5   +   3)    ^ 2+(1  +4    ')
			'error message'
			>>> x.postfix('2*(5 +3)^ 2+)1  +4(    ')
			'error message'
		'''
		if not isinstance(txt,str) or len(txt)<=0:
			print("Argument error in postfix")
			return None

		postStack=Stack()
		output = []
		precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
		splitTxt = re.split('([-+*/()^])', txt)
		infix = []
		for x in splitTxt:
			x = x.strip()
			if x in '-+*/()^':
				infix.append(x)
			else:
				try:
					y = float(x)
					infix.append(x)
				except ValueError:
					continue
		infix = ' '.join(infix).split()
		for i in infix:
			if self.isNumber(i):
				i = float(i)
				if isinstance(i, int):
					output.append(str(i)+'.0')
				else:
					output.append(str(float(i)))
			elif i == '(':
				postStack.push(i)
			elif i == ')':
				top = postStack.pop()
				while (top != '(') and (not postStack.isEmpty()):
					output.append(top)
					top = postStack.pop()
			elif i == ' ':
				pass
			else:
				try:
					while (not postStack.isEmpty()) and (precedence[i] <= precedence[postStack.peek()]):
						output.append(postStack.pop())
				except KeyError:
					pass
				finally:
					postStack.push(i)
		while not postStack.isEmpty():
			output.append(postStack.pop())
		return " ".join(output)


	@property
	def calculate(self):
		if not isinstance(self.expr,str) or len(self.expr)<=0:
			print("Argument error in calculate")
			return None
		calcStack=Stack()
		return self._calculate

	@calculate.setter
	def calculate(self, value):

		calcStack=Stack()
		postfix_expr = Calculator().postfix(self.expr)
		print(postfix_expr)
		for i in postfix_expr:
			if i in "0123456789":
				calcStack.push(i)
			elif i == '^':
				num1= calcStack.pop()
				num2= calcStack.pop()
				result= float(num2) ** float(num1)
				calcStack.push(result)
			elif i == '*':
				num1= calcStack.pop()
				num2= calcStack.pop()
				result = float(num1) * float(num2)
				calcStack.push(result)
			elif i == '/':
				num1= calcStack.pop()
				num2= calcStack.pop()
				result = float(num2) / float(num1)
				calcStack.push(result)
			elif i == '-':
				num1= calcStack.pop()
				num2= calcStack.pop()
				result = float(num2) - float(num1)
				calcStack.push(result)
			elif i == '+':
				num1= calcStack.pop()
				num2= calcStack.pop()
				result= float(num2) + float(num1)
				calcStack.push(result)
		value =  calcStack.pop()
		self.calculate = value
		

x=Calculator
x.expr='    4  +      3 -2'
x.calculate()

       
