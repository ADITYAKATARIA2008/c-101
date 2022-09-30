import time 
second = int(input("enter the time in seconds : "))
def CountDown(second):
   while second>0:
     mins=second//60
     secs=second%60
     timer=f'{mins} : {secs}'
     print(timer,end='\r')
     time.sleep(1)
     second-=1
CountDown(second)
