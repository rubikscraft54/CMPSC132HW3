#HW3
#Due Date: 11/03/2019, 11:59PM 
'''
Team members: Sean Seol, Kaite Pighini

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
		#retruns True if count is zero, False otherwise
		if self.count == 0:
			return True
		else:
			return False

	def __len__(self):
		#returns count of the Stack 
		return self.count

	def push(self,value):
		#new Node created from input and assigned as top of the Stack. Count also increases by 1.
		new = Node(value)
		new.next = self.top
		self.top = new
		self.count += 1
	 
	def pop(self):
		#returns nothing if Stack is already empty
		if self.isEmpty():
			return None
		else:
		#If Stack is not empty, top of the stack is returned, next Node is assigned as a new top.
		#old top loses connection to the Stack and count also decreases by 1.
			top = self.top
			newTop = top.next
			self.top = newTop
			top.next = None
			self.count -= 1
			return top.value

	def peek(self):
		#returns top of the Stack and does not modify the Stack itself
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
		if not isinstance(txt,str) or len(txt)<=0:
			print("Argument error in postfix")
			return 'error message'

		postStack=Stack()
		output = []
		#assigns priority index of the operators.
		precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
		#split the input string by operators/parentheses
		splitTxt = re.split('([-+*/()^])', txt)
		#Create a new list with only numbers/operators/parentheses ie. delete spaces
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
		#extra step to delete item('') in the list.
		infix = ' '.join(infix).split()
		#checks for valid infix expression, no double operators
		num_oprnd = 0
		num_oprtr = 0
		prnts = ''
		for n in infix:
			if self.isNumber(n):
				num_oprnd += 1
			elif n in '-+*/^':
				num_oprtr += 1
			elif n in '()':
				prnts += n
			else:
				continue
		#checks for matching parentheses
		for l in range(len(prnts)):
			prnts = prnts.replace('()', '')
		#extra step for handling expressions starting with negative sign
		if len(infix) > 0 and infix[0] == '-':
			num_oprtr -= 1
		#if expression is valid, then we convert to postfix expression.
		if prnts == '' and (num_oprnd == num_oprtr + 1):
			if infix[0] == '-':
				infix[1] = '-' + infix[1]
				infix = infix[1:]
			#add all numbers to the 'output' list in floating point format
			for i in infix:
				if self.isNumber(i):
					i = float(i)
					#add .0 to integers for consistency
					if isinstance(i, int):
						output.append(str(i)+'.0')
					else:
						output.append(str(float(i)))
				#right parentheses get pushed in to stack and waits until left parentheses appear in the expression
				elif i == '(':
					postStack.push(i)
				#left parentheses append items in the stack to the output list until its matching right parenthese shows up from stack.
				#then both parentheses are discarded and only numbers/operators are added to the output.
				elif i == ')':
					top = postStack.pop()
					while (top != '(') and (not postStack.isEmpty()):
						output.append(top)
						top = postStack.pop()
				#operators are handled here.
				#if current operator is not of higher priority than the top of the stack,
				#items on the top of the stack are fed into output until it is higher priority.
				else:
					try:
						while (not postStack.isEmpty()) and (precedence[i] <= precedence[postStack.peek()]):
							output.append(postStack.pop())
					#this part handles any parentheses that appear in the middle
					except KeyError:
						pass
					#then operand  itself is pushed to stack.
					finally:
						postStack.push(i)
			#after iterating over expression, stack is emptied and items are passed onto output list
			while not postStack.isEmpty():
				output.append(postStack.pop())
			#list is joined to return a string
			return " ".join(output)
		#error message for invalid expressions.
		else:
			return 'error message'


	@property
	def calculate(self):
		if not isinstance(self.expr,str) or len(self.expr)<=0:
			print("Argument error in calculate")
			return None
		#initalize statck
		calcStack=Stack()
		#converts infix expr to postfix notation and seperate values in expression into a list
		postfix_expr = self.postfix(self.expr)
		postfix_expr = postfix_expr.split()
		for i in postfix_expr:
			#if value is a number, push to stack
			if self.isNumber(i):
				calcStack.push(i)
			#if value is one of the following operators, pop 2 recent digits
			#then perform calucation, then push result to stack
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
		#returns final calcuated result 
		return calcStack.pop()
