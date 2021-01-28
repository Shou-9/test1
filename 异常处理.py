
#   except 在捕获错误异常的时候，是要根据具体的错误类型来捕获的

try:
    #print(b)    #捕获逻辑的代码

    li=[1,4,5]
    print(li[10])      #通过下标去访问列表
    pass
# except NameError as msg:                   #NameError 是指一种错误类型
#       #捕获到的错误  才会在这里执行
#     print(msg)
#     pass
# except IndexError as msg:                 #IndexError 是一种错误类型
#     print(msg)
#     pass

except Exception as result:        #用于不知道异常类型的情况下
    print(result)
    pass


print('首次接触错误处理')
print('hhhhhh')