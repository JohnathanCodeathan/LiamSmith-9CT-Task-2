import time
import uasync as uas
from machine import PWM, Pin

HATE = PWM(Pin(18))
JohnKneaded = False
JaneKneaded = False
A2 = 110
B2 =123
b5 = 988
g5 = 784
e6 = 1318
c6 = 1047
d3 = 147
f6 = 1397
b4 = 494
a3 = 220
B1 = 62
e5 = 659
c4 = 262
C3 = 131
f5 = 698
a4 = 440
d6 = 1175
d5 = 587
a5 = 880
e3 = 165
d2 = 73
mod = 0
maxscore = 0
async def SOUND:
  HATE.duty_u16(1000)
  HATE.freq(B2) #Bar 1
  await uas.sleep(0.26 + mod)
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.13+ mod)
  HATE.freq(A2)
  await uas.sleep(0.13+ mod)
  HATE.freq(B2)
  await uas.sleep(0.26+ mod)
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.13+ mod)
  HATE.freq(A2)
  await uas.sleep(0.13+ mod) #Bar 2
  HATE.freq(B2)
  await uas.sleep(0.26+ mod)
  HATE.freq(B1)
  await uas.sleep(0.26+ mod)
  HATE.freq(B2)
  await uas.sleep(0.26+ mod)
  HATE.freq(C3)
  await uas.sleep(0.13+ mod)
  HATE.freq(d3)
  await uas.sleep(0.39+ mod) #Bar 3
  HATE.freq(d2)
  await uas.sleep(0.26+ mod)
  HATE.freq(d3)
  await uas.sleep(0.26+ mod)
  HATE.freq(d2)
  await uas.sleep(0.26+ mod) #Bar 4
  HATE.freq(d3)
  await uas.sleep(0.26+ mod)
  HATE.freq(d2)
  await uas.sleep(0.26+ mod)  
  HATE.freq(d3)
  await uas.sleep(0.13+ mod)
  HATE.freq(e3)
  await uas.sleep(0.13+ mod)
  HATE.freq(d3)
  await uas.sleep(0.13+ mod)
  HATE.freq(C3)
  await uas.sleep(0.39+ mod) #Bar 5
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.26+ mod)
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.13+ mod)
  HATE.freq(c4)
  await uas.sleep(0.13+ mod)
  HATE.freq(C3)
  await uas.sleep(0.26+ mod) #Bar 6
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.26+ mod)
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.13+ mod)
  HATE.freq(c4)
  await uas.sleep(0.13+ mod)
  HATE.freq(C3)
  await uas.sleep(0.26+ mod) #Bar 7
  HATE.freq(B2)
  await uas.sleep(0.26+ mod)
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.13+ mod)
  HATE.freq(A2)
  await uas.sleep(0.13+ mod)
  HATE.freq(B2)
  await uas.sleep(0.26+ mod)
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.13+ mod)
  HATE.freq(A2)
  await uas.sleep(0.13+ mod) #Bar 8
  HATE.freq(B2)
  await uas.sleep(0.26+ mod)
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.13+ mod)
  HATE.freq(A2)
  await uas.sleep(0.13+ mod)
  HATE.freq(B2)
  await uas.sleep(0.13+ mod)
  HATE.freq(e3)
  await uas.sleep(0.13+ mod)
  HATE.freq(d3)
  await uas.sleep(0.13+ mod)
  HATE.freq(B2)
  await uas.sleep(0.39+ mod) #Bar 9
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.13+ mod)
  HATE.freq(A2)
  await uas.sleep(0.13+ mod)  
  HATE.freq(B2)
  await uas.sleep(0.26+ mod)
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.13+ mod)
  HATE.freq(A2)
  await uas.sleep(0.13+ mod) #Bar 10
  HATE.freq(B2)
  await uas.sleep(0.26+ mod)
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.13+ mod)
  HATE.freq(A2)
  await uas.sleep(0.13+ mod)
  HATE.freq(e3)
  await uas.sleep(0.13+ mod)
  HATE.freq(d3)
  await uas.sleep(0.13+ mod)
  HATE.freq(A2)
  await uas.sleep(0.26+ mod) #Bar 11
  HATE.freq(d3)
  await uas.sleep(0.26+ mod)
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.13+ mod)
  HATE.freq(B2)
  await uas.sleep(0.13+ mod)
  HATE.freq(d3)
  await uas.sleep(0.26+ mod)
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.13+ mod)
  HATE.freq(B2)
  await uas.sleep(0.13+ mod) #Bar 12
  HATE.freq(d3)
  await uas.sleep(0.26+ mod)
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.13+ mod)
  HATE.freq(B2)
  await uas.sleep(0.13+ mod)
  HATE.freq(d3)
  await uas.sleep(0.13+ mod)
  HATE.freq(a3)
  await uas.sleep(0.13+ mod)
  HATE.freq(d3)
  await uas.sleep(0.13+ mod)
  HATE.freq(C3)
  await uas.sleep(0.39+ mod) #Bar 13
  HATE.duty_u16(0)
  await uas.sleep(0.05+ mod)
  HATE.duty_u16(1000)
  await uas.sleep(0.26+ mod)
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.13+ mod)
  HATE.freq(C3)
  await uas.sleep(0.13+ mod)
  HATE.freq(a3)
  await uas.sleep(0.13+ mod)
  HATE.freq(C3)
  await uas.sleep(0.13+ mod)
  HATE.freq(C3)
  await uas.sleep(0.39+ mod) #Bar 14
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.26+ mod)
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.13+ mod)
  HATE.freq(C3)
  await uas.sleep(0.13+ mod)
  HATE.freq(a3)
  await uas.sleep(0.13+ mod)
  HATE.freq(C3)
  await uas.sleep(0.13+ mod)
  HATE.freq(B2)
  JohnKneaded = True
  await uas.sleep(0.39+ mod) #Bar 15
  JaneKneaded = True
  JohnKneaded = True
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.13+ mod)
  HATE.freq(A2)
  await uas.sleep(0.13+ mod)
  JaneKneaded = True
  HATE.freq(B2)
  await uas.sleep(0.26+ mod)
  JohnKneaded = True
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  await uas.sleep(0.13+ mod)
  HATE.freq(A2)
  await uas.sleep(0.13+ mod) #Bar 16
  JaneKneaded = True
  HATE.freq(B2)
  await uas.sleep(0.26+ mod)
  JohnKneaded = True
  HATE.duty_u16(0)  
  await uas.sleep(0.26+ mod)
  JaneKneaded = True
  HATE.duty_u16(1000)
  HATE.freq(f5)
  maxscore += 2
  await uas.sleep(0.13 +mod)
  HATE.freq(a5)
  maxscore += 2
  await uas.sleep(0.13+mod)
  JohnKneaded = True
  HATE.duty_u16(0)
  await uas.sleep(0.13 +mod)
  JaneKneaded = True
  HATE.duty_u16(1000)
  HATE.freq(b5)
  maxscore += 2
  await uas.sleep(0.39+ mod) #Bar 17
  JohnKneaded = True #11
  HATE.freq(f5)
  maxscore += 2
  await uas.sleep(0.26+mod)
  JaneKneaded = True
  HATE.freq(e5)
  maxscore+= 2
  await uas.sleep(0.26 + mod)
  JohnKneaded = True
  HATE.freq(d5)
  maxscore += 2
  await uas.sleep(0.13 +mod) #Bar 18
  JaneKneaded = True
  await uas.sleep(0.13 +mod)
  maxscore += 2
  JohnKneaded = True #15
  HATE.freq(e5)
  await uas.sleep(0.26 + mod)
  maxscore += 2
  HATE.freq(d5)
  await uas.sleep(0.26 +mod)
  maxscore += 2
  HATE.freq(d6)
  await uas.sleep(0.13 + mod)
  maxscore += 2
  HATE.freq(a5)
  await uas.sleep(0.13 + mod)
  HATE.duty_u16(0)
  await uas.sleep(0.13 + mod)
  HATE.duty_u16(1000)
  HATE.freq(b5) #11
  maxscore += 2
  await uas.sleep(0.39 + mod) #Bar 19
  JaneKneaded = True
  HATE.freq(f5)
  maxscore += 2
  await uas.sleep(0.13 + mod)
  JohnKneaded = True
  await uas.sleep(0.13 + mod)
  JaneKneaded = True
  HATE.freq(e5)
  maxscore += 2
  await uas.sleep(0.13 + mod)
  JohnKneaded = True
  await uas.sleep(0.13 + mod)
  HATE.freq(d5)
  maxscore += 2
  await uas.sleep(0.13 + mod)
  HATE.freq(f5) #15
  maxscore += 2
  await uas.sleep(0.26 + mod) #Bar 20
  JaneKneaded = True #20
  await uas.sleep(0.13 + mod)
  JohnKneaded = True
  await uas.sleep(0.26 + mod)
  JaneKneaded = True
  HATE.duty_u16(0)#Bar 21
  await uas.sleep(0.39 + mod)
  JohnKneaded = True
  await uas.sleep(0.13 + mod)
  await uas.sleep(0.13+ mod)
  JaneKneaded = True
  HATE.duty_u16(1000)
  HATE.freq(f5)
  maxscore += 2
  await uas.sleep(0.26 + mod)
  HATE.freq(e5)
  maxscore +=2
  await uas.sleep(0.13 + mod)
  HATE.freq(d5)
  maxscore += 2
  await uas.sleep(0.13 + mod)
  HATE.duty_u16(0)
  await uas.sleep(0.13 + mod)
  HATE.duty_u16(1000)
  maxscore += 2
  HATE.freq(e5)
  await uas.sleep(0.13 + mod) #Bar 22
  HATE.duty_u16(0)
  await uas.sleep(0.13 + mod)
  HATE.duty_u16(1000)
  HATE.freq(a4) #20
  maxscore += 2
  await uas.sleep(0.13 + mod)
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  maxscore +=2
  await uas.sleep(0.13 + mod)
  HATE.freq(a5)
  maxscore += 2
  await uas.sleep(0.39 + mod)
  JohnKneaded = True #25
  HATE.freq(g5)
  maxscore +=2
  await uas.sleep(0.13 + mod) #Bar 23
  JaneKneaded = True
  await uas.sleep(0.13 + mod)
  HATE.freq(f5)
  maxscore += 2
  await uas.sleep(0.13 + mod) #Bar 24
  JohnKneaded = True
  await uas.sleep(0.39 + mod)
  JaneKneaded = True
  await uas.sleep(0.26)
  JohnKneaded = True
  await uas.sleep(0.26)
  JaneKneaded = True #30
  HATE.duty_u16(0)
  await uas.sleep(0.26 + mod)
  JohnKneaded = True
  await uas.sleep(0.26 + mod)
  JaneKneaded = True
  HATE.duty_u16(1000) # 25
  maxscore += 2
  await uas.sleep(0.13 +mod)
  HATE.freq(a5)
  maxscore += 2
  await uas.sleep(0.13+mod)
  JohnKneaded = True
  HATE.duty_u16(0)
  await uas.sleep(0.13 +mod)
  JaneKneaded = True
  HATE.duty_u16(1000)
  HATE.freq(b5)
  maxscore += 2
  await uas.sleep(0.26+ mod)
  JohnKneaded = True # 35
  await uas.sleep(0.13 + mod)#Bar 25
  HATE.freq(f5)
  maxscore += 2
  await uas.sleep(0.26+mod)
  JaneKneaded = True
  HATE.freq(e5)
  maxscore+= 2
  await uas.sleep(0.26 + mod)
  JohnKneaded = True
  HATE.freq(d5) #30
  maxscore += 2
  await uas.sleep(0.13 +mod) #Bar 26
  await uas.sleep(0.13 +mod)
  JaneKneaded = True
  maxscore += 2
  HATE.freq(e5)
  await uas.sleep(0.13 + mod)
  JohnKneaded = True
  await uas.sleep(0.13 + mod)
  maxscore += 2
  HATE.freq(d5)
  await uas.sleep(0.26 +mod)
  maxscore += 2
  HATE.freq(d6)
  await uas.sleep(0.13 + mod)
  maxscore += 2
  HATE.freq(a5)
  await uas.sleep(0.13 + mod)
  HATE.duty_u16(0)
  await uas.sleep(0.13 + mod)
  HATE.duty_u16(1000)
  HATE.freq(b5) #35
  maxscore += 2
  await uas.sleep(0.39 + mod) #Bar 27
  HATE.freq(f5)
  maxscore += 2
  await uas.sleep(0.13 + mod)
  JaneKneaded = True #40
  await uas.sleep(0.13 + mod)
  HATE.freq(e5)
  maxscore += 2
  await uas.sleep(0.13 + mod)
  JohnKneaded = True
  await uas.sleep(0.13 + mod)
  JaneKneaded = True
  HATE.freq(d5)
  maxscore += 2
  await uas.sleep(0.13 + mod)
  JohnKneaded = True
  HATE.freq(f5)
  maxscore += 2
  await uas.sleep(0.13) #Bar 28
  await uas.sleep(0.26) #Bar 29
  JaneKneaded = True
  await uas.sleep(0.26)
  JohnKneaded = True #45
  await uas.sleep(0.13 + mod)
  JaneKneaded = True
  await uas.sleep(0.26)
  JohnKneaded = True
  await uas.sleep(0.13)
  HATE.duty_u16(0)
  await uas.sleep(0.13 + mod)
  HATE.duty_u16(1000)
  HATE.freq(f5) #40
  maxscore += 2
  await uas.sleep(0.26 + mod)
  HATE.freq(e5)
  maxscore +=2
  await uas.sleep(0.13 + mod)
  HATE.freq(d5)
  maxscore += 2
  await uas.sleep(0.13 + mod)
  HATE.duty_u16(0)
  await uas.sleep(0.13 + mod)
  HATE.duty_u16(1000)
  HATE.freq(e5)
  maxscore += 2
  await uas.sleep(0.39 + mod) #Bar 30
  maxscore += 2
  HATE.freq(d5)
  await uas.sleep(0.26 + mod)
  HATE.freq(a4) #45
  maxscore += 2
  await uas.sleep(0.13 + mod)
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  maxscore += 2
  await uas.sleep(0.26 + mod)
  HATE.freq(b4)
  maxscore +=2
  await uas.sleep(0.26 + mod) #Bar 31
  JaneKneaded = True
  await uas.sleep(0.26)
  JohnKneaded = True
  await uas.sleep(0.13)
  JaneKneaded = True #50
  HATE.duty_u16(0)
  await uas.sleep(0.26 + mod) #Bar 32
  JohnKneaded = True
  await uas.sleep(0.26)
  await uas.sleep(0.13)#Bar 33
  JaneKneaded = True
  await uas.sleep(0.26 + mod)
  JohnKneaded = True
  await uas.sleep(0.13)
  JaneKneaded = True
  await uas.sleep(0.26)
  JohnKneaded = True
  await uas.sleep(0.26)
  await uas.sleep(0.13 + mod)
  HATE.duty_u16(1000)
  HATE.freq(f6)
  maxscore += 2
  await uas.sleep(0.26 + mod)
  HATE.freq(e6)
  maxscore += 2
  await uas.sleep(0.13 + mod)
  HATE.freq(d5) #50
  maxscore += 2
  await uas.sleep(0.13 + mod)
  HATE.duty_u16(0)
  await uas.sleep(0.13 + mod)
  HATE.duty_u16(1000)
  HATE.freq(e6)
  maxscore += 2
  await uas.sleep(0.39 + mod) #Bar 34
  HATE.freq(d6)
  maxscore += 2
  await uas.sleep(0.26 + mod)
  HATE.freq(a5)
  maxscore += 2
  await uas.sleep(0.13 + mod)
  HATE.duty_u16(0)
  await uas.sleep(0.05)
  HATE.duty_u16(1000)
  maxscore += 2
  await uas.sleep(0.26 + mod)
  HATE.freq(b5)
  maxscore += 2
  await uas.sleep(0.65 + mod) #Bar 35
  HATE.duty_u16(0)
  await uas.sleep(0.52 + mod) #Bar 36
  await uas.sleep(1.04 + mod)