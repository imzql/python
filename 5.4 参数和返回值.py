#参数和返回值

#参数：函数执行时需要从外部传入的数据
# def getSum(a,b):  #形参
# 	result=a+b
# 	print("相加的结果是：",result)
# #-------------------------------------
# getSum(4,5)  #实参

#实参个数和形参必须一致

# #返回值：函数执行后返回的结果
# def fun1(lista):
# 	r=sum(lista)/len(lista)
# 	print("平均值：",r)
# 	return r
# #--------------------------------------
# result=fun1([2,3243,43,5,454,65,66,76,6,768,7])  #接收返回值
# print(result)

# #返回多个值
# def fun2():
# 	print("fun2被执行了！")
# 	a=11
# 	b=22
# 	c=33
# 	return a,b,c
# #---------------------------------------
# r1,r2,r3=fun2()
# print(r1,r2,r3)


#榨汁机
def juicer(f1):
	print("榨汁机开始工作.....")
	juice=f1+"汁"
	return juice
#--------------------------------------------
j=juicer("西瓜")
print("榨出一杯：",j)

