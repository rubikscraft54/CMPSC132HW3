#HW3
#Due Date: 11/03/2019, 11:59PM 
'''
Team members:

Collaboration Statement:             

'''

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
        if self.top is None:
            return True
        else:
            return False
        
    def __len__(self): 
        count = 0 
        temp = self.top
        while temp:
            count+= 1
            temp = temp.next
        return count

    def push(self,value):
        if self.top is None:
            self.top = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            print("stack is empty")
            return None
        else:
            popped= self.top.value
            self.top = self.top.next
            return popped 

    def peek(self):
        return self.top.value



#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.expr = None


    def isNumber(self, txt):
 		try:
            float(txt)
            return True
        except ValueError:
            return False
    	


    def postfix(self, txt):

        if not isinstance(txt,str) or len(txt)<=0:
            print("Argument error in postfix")
            return None
        postStack = Stack()
        precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
        output= []
        txt = txt.split()
        for i in txt:
            if i in "0123456789":
                output.append(i)
            elif i == '(':
                postStack.push(i)
            elif i == ')':
                head = postStack.pop()
                while head != '(':
                    output.append(head)
                    head = postStack.pop()
            else:
                while not postStack.isEmpty() and precedence[postStack.peek()]<= precedence[i]:
                    output.append(postStack.pop())
                postStack.push(i)
        while not postStack.isEmpty():
            output.append(postStack.pop())
        return " ".join(output)
        # YOUR CODE STARTS HERE
        


    @property
    def calculate(self):
        '''
            Required: calculate must call postfix
                      calculate must create and use a Stack to compute the final result as shown in the video lecture
            >>> x=Calculator()
            >>> x.expr='    4  +      3 -2'
            >>> x.calculate
            5.0
            >>> x.expr='  -2  +3.5'
            >>> x.calculate
            1.5
            >>> x.expr='4+3.65-2 /2'
            >>> x.calculate
            6.65
            >>> x.expr=' 23 / 12 - 223 +      5.25 * 4    *      3423'
            >>> x.calculate
            71661.91666666667
            >>> x.expr='   2   - 3         *4'
            >>> x.calculate
            -10.0
            >>> x.expr=' 3 *   (        ( (10 - 2*3)))'
            >>> x.calculate
            12.0
            >>> x.expr=' 8 / 4  * (3 - 2.45      * (  4- 2 ^   3)) + 3'
            >>> x.calculate
            28.6
            >>> x.expr=' 2   *  ( 4 + 2 *   (5-3^2)+1)+4'
            >>> x.calculate
            -2.0
            >>> x.expr='2.5 + 3 * ( 2 +(3.0) *(5^2 - 2*3^(2) ) *(4) ) * ( 2 /8 + 2*( 3 - 1/ 3) ) - 2/ 3^2'
            >>> x.calculate
            1442.7777777777778
            >>> x.expr="4++ 3 +2"
            >>> x.calculate
            'error message'
            >>> x.expr="4    3 +2"
            >>> x.calculate
            'error message'
            >>> x.expr='(2)*10 - 3*(2 - 3*2)) '
            >>> x.calculate
            'error message'
            >>> x.expr='(2)*10 - 3*/(2 - 3*2) '
            >>> x.calculate
            'error message'
            >>> x.expr=')2(*10 - 3*(2 - 3*2) '
            >>> x.calculate
            'error message'
        '''

        if not isinstance(self.expr,str) or len(self.expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack=Stack()
        postfix_expr = Calculator().postfix(self.expr)
        for i in postfix_expr:
        
            if i.isdigit():
                calcStack.push(i)
            if i == '^':
                num1= calcStack.pop()
                num2= calcStack.pop()
                result= num2 ** num1
                calcStack.push(result)
            elif i == '*':
                num1= calcStack.pop()
                num2= calcStack.pop()
                result = num1 * num2
                calcStack.push(result)
            elif i == '/':
                num1= calcStack.pop()
                num2= calcStack.pop()
                result = num2 / num1
                calcStack.push(result)
            elif i == '-':
                num1= calcStack.pop()
                num2= calcStack.pop()
                result = num2 - num1
                calcStack.push(result)
            elif i == '+':
                num1= calcStack.pop()
                num2= calcStack.pop()
                result= num2 + num1
                calcStack.push(result)
            return calcstack.pop()
           

       
