num=int(input("\nEnter the number"))

def function(num):
 if num==0 or num==1:
        return 1
 else:
        return num*factorial(num-1)

result=factorial(num)
print("the factorial of given number",num,"is", result)
          