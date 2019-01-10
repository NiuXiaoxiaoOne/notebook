### 入门1.1 乘法口诀表

##def Print_shuZi(chengShu, beiChengShu):
##      print(f"{chengShu}*{beiChengShu}={chengShu * beiChengShu}", end =" ")
##
##for beiChengShu in range(1, 10):
##      chengShu = 1
##      if chengShu == beiChengShu:
##            print(f"{chengShu}*{beiChengShu}={chengShu * beiChengShu}")
##      else:
##            while chengShu != beiChengShu + 1:
##                  Print_shuZi(chengShu, beiChengShu)
##                  chengShu += 1
##            print()

# 入门1.2 编写一个函数，可以去除一个列表中重复的元素，并且保持元素的顺序
# 无法解决
##def List_quChong(List=[]):
##      """该函数输入要求输入一个list，并通过一一比较，将重复的元素删除"""
##      try:
##            for i in range(len(List)):
##                  for i1 in range(i + 1, len(List)):
##                        if List[i] == List[i1]:
##                              del List[i1]
##      except IndexError:
##            pass
##
##      print(List)
##
##k = [3, 2, 2, 9, 2, 9, 20]
##List_quChong(k)

# 入门3

##for i in range(1, 21):
##      if i % 3 == 0 and \
##         i % 5 == 0:
##            print("FizzBuzz", end = ' ')
##      else:
##            if i % 3 == 0: print("Fizz", end = ' ')
##            elif i % 5 == 0: print("Buzz", end = ' ')
##            else: print(i, end = ' ')

##import pdb
##k = [2, 3, 2.4, "a", "5"]

##def panDuan(List=[]):
##      for i in range(len(List)):
##            pdb.set_trace()
##            list_yuanSu = List[i]
##            if type(list_yuanSu) != int:
##                  if type(list_yuanSu) == float or \
##                     str(list_yuanSu).isalpha() == 1:
##                        List.remove(list_yuanSu)
##      print(List)
##
##panDuan(k)

# 编13


# 编13
##def shuChu():
##      Int = eval(input("输入一个整数: "))
##      "该函数接收一个整数，返回整数转化为二进制后1的个数"
##      now_Int = bin(Int).replace("b", "") # str.replace()将第一个参数替换为第二个参数
##      jiShuQi = 0 # 计数器
##      for i in now_Int:
##            if i == "1": jiShuQi += 1
##      print(jiShuQi)
##      
##      
##shuChu()

# 人民币变文字
##
##jiShu = {0:"", 1:"壹", 2:"贰", 3:"叁", 4:"肆", 5:"伍",
##         6:"陆", 7:"柒", 8:"捌", 9:"玖"}
##
##xuShu = {1:"圆", 2:"拾", 3:"佰", 4:"仟", 5:"万",
##         6:"拾", 7:"佰", 8:"仟", 9:"亿"}
##
##yongHu = "91678686"
##fanHuiShu = "" # 最终返回的数字
##jiShu_zhiZhen = 0
##xuShu_zhiZhen = len(yongHu)
##
##while jiShu_zhiZhen != len(yongHu):
##      for i in yongHu[jiShu_zhiZhen]:
##            fanHuiShu += jiShu[int(i)] + xuShu[xuShu_zhiZhen]
##            jiShu_zhiZhen += 1
##            xuShu_zhiZhen -= 1
##print(fanHuiShu)
      
