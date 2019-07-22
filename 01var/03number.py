number1 = 15
number2 = 15.8
result = number1/number2
print(result)

number3 = 15
number4 = 5
#这里为啥3.0 下面75啊？
print(number3/number4)
print(number3*number4)

age = 18
#这里的数字和字符串的拼接问题  解释型语言不会先全转成str处理的吗。。
#message = "Happy " + age + "rd Birthday!"
message = "Happy " + str(age) + "rd Birthday!"
print(message)

