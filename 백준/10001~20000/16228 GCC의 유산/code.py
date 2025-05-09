class nt(int):
    def __mul__(self,other):
        return min(self,other)
    def __mod__(self,other):
        return max(self,other)
def main():
    infix_notation=input().replace('<?','*').replace('>?','%')
    stack=[]
    result=[]
    num_q=[]
    property_operator={'+':2,'-':2,'(':1,')':1,'*':3,'%':3}
    for token in infix_notation:
        if token.isalnum():
            num_q.append(token)
        else:
            if num_q:
                result.append(nt(''.join(num_q)))
                num_q=[]
            
            if token=='(':
                stack.append(token)
            elif token==')':
                while stack[-1]!='(':
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and property_operator[stack[-1]]>=property_operator[token]:
                    result.append(stack.pop())
                    
                stack.append(token)
    if num_q:
        result.append(nt(''.join(num_q)))
    while stack:
        result.append(stack.pop())

    for token in result:
        if type(token)==nt:
            stack.append(token)
        
        else:
            v1,v2=stack.pop(),stack.pop()
            stack.append(eval(f'nt({v2}){token}nt({v1})'))
    print(stack.pop())
            
main()