class Stack:
    def __init__(self):       
        self.items = []
                
    def push(self, item):     
        self.items.append(item)
                
    def empty(self):        
        return not self.items
                
    def size(self):              # 스택에 있는 데이터 수를 반환합니다.
        return len(self.items)
        
    def pop(self):               # 스택의 가장 위에 있는 데이터를 반환하고 제거합니다.
        if self.empty():
            raise Exception("Stack is empty")
            
        return self.items.pop()
                
    def top(self):               # 스택의 가장 위에 있는 데이터를 제거하지 않고 반환합니다.
        if self.empty():
            raise Exception("Stack is empty")
                        
        return self.items[-1]

str = input()

def sol(text):
    s = Stack()

    for ch in text:
        if ch == '(':
            s.push('(')
        else:
            if s.empty():
                return False
            s.pop()

    return s.empty()

if sol(str) :
  print("Yes")
else :
  print("No")