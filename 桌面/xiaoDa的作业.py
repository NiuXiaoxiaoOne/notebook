#### 第一题
##
##      
##
##
##
##def valid_password(pwd):
##      """
##            判断字符是否符合全部条件
##      """
##
##      if panDuan1(pwd):
##            return False
##      elif panDuan2(pwd):
##            return False
##      elif panDuan3(pwd):
##            return False
##      else:
##            return True
##      
##def panDuan1(pwd1):
##      """
##            判断是否只包含字母、数字、下划线
##      """
##
##      pwd1 = list(pwd1)
##      zhiZhen = 0
##      
##      for i in pwd1:
##            if not i.isalnum():
##                  if i != "_":
##                        zhiZhen += 1
##
##      if zhiZhen >= 1:
##            return True
##
##def panDuan2(pwd2):
##      """
##            判断第一位是否是字母
##            判断是否以字母或数字结尾
##      """
##      pwd2 = list(pwd2)
##      zhiZhen = 0
##
##      if not pwd2[0].isalpha():
##            zhiZhen += 1
##      elif not pwd2[-1].isalnum():
##            zhiZhen += 1
##
##      if zhiZhen >= 1:
##            return True
##
##def panDuan3(pwd3):
##      """
##            判断是否其长度是否在2-10之间
##      """
##
##      pwd3_len = len(pwd3)
##      if pwd3_len < 2 or pwd3_len > 10:
##            return True
##
##
##zhiZhen = 1
##
##while zhiZhen:
##      yongHu = input("输入: ")
##      print(valid_password(yongHu))
##      zhiZhen = int(input("是否继续执行程序,0关闭程序: "))

### 2
##
##def panDuan(suShu):
##      """
##            本函数接受一个参数，若为素数，则不返回
##            否则返回False
##      """
##
##      f = 0
##      for i in range(2, suShu):
##            if suShu % i == 0:
##                  f = 1
##                  break
##      if f == 0:
##            return True
##
##zhiZhen = []
##for i in range(2, 100):
##      if panDuan(i):
##            zhiZhen.append(str(i))
##print(' '.join(zhiZhen))
##            


### 3
##
##
##def shuChu_tuple(Str, letter):
##      """
##            本函数有两个参数，第一个参数接受一个包含letter且每个元素都是字符串的list
##            第二个参数为任意一个属于Str的参数
##      """
##      zhiZhen = 0
##      for i in Str:
##            if i == letter:
##                  zhiZhen += 1
##      return (letter, zhiZhen)
##
##def letter_count():
##
##      k = 1
##      while k:
##            yongHu = list(input("输入一串任意的字符串: "))
##
##            rongQi = []
##            for i in yongHu:
##                  rongQi.append(shuChu_tuple(yongHu, i))
##            print(list(set(rongQi)))
##            k = int(input("输入0终止程序"))
##letter_count()

### 4
##
##Str = input("请输入一个英文句子: ")
##
##def cap_string(a_str):
##      """
##            本函数要求输入一个参数，返回首字母大写，其余字母小写的字符串
##      """
##      print(a_str.title())
##
##cap_string(Str)

# 5

class Queue:

      def __init__(self):
            pass
      
      def enqueue(self, numbers):
            self.numbers = numbers

      def dequeue(self):
            return self.numbers
      
##>>> q = Queue()
##>>> q.enqueue(5)
##>>> q.dequeue()
##5
