"""Copyright [2022] @[Li, Yong Xin], [Li, Zi Yan]

   Author: Li, Yong Xin (li.yongxin@foxmail.com)
           Li, Zi Yan (ziyan.li-cn@foxmail.com)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""


import sys
import os

sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'\\Pyscripts')
import Pyscripts.FileOperation as FO
import Pyscripts.DataOperation as DO

def main():
    CANDoc1 = FO.FilePack( FileName="CANBusLog.txt" )

    if(os.path.exists("C1Recording.txt") == True):
        os.remove("C1Recording.txt")
    if(os.path.exists("C5Recording.txt") == True):
        os.remove("C5Recording.txt")

    CANC1RecordingDoc = open("C1Recording.txt", mode='w', encoding='utf-8' )
    CANC5RecordingDoc = open("C5Recording.txt", mode='w', encoding='utf-8' )

    while(CANDoc1.LineBuffer != '') :
        KeyWordFlag = -1

        KeyWordFlag = CANDoc1.LineBuffer[14:19].find(" C1 ")
        if(KeyWordFlag != -1):
            dec_extracted_LN = DO.StrOperation().StrToDec(
                                CANDoc1.LineBuffer[41:45], "big")
            
            dec_extracted_RN = DO.StrOperation().StrToDec(
                                CANDoc1.LineBuffer[53:57], "big")

            print("%s,%d,%d\n" % (CANDoc1.LineBuffer[:11], dec_extracted_LN
                             ,dec_extracted_RN), file = CANC1RecordingDoc)


        
        KeyWordFlag = CANDoc1.LineBuffer[14:19].find(" C5 ")
        if(KeyWordFlag != -1):
            dec_extracted_LN = DO.StrOperation().StrToDec(
                                CANDoc1.LineBuffer[41:45], "big")
            
            dec_extracted_RN = DO.StrOperation().StrToDec(
                                CANDoc1.LineBuffer[53:57], "big")

            print("%s,%d,%d,%d\n" % (CANDoc1.LineBuffer[:11], dec_extracted_LN,
                                 dec_extracted_RN), file = CANC5RecordingDoc)
        
        CANDoc1.ReadNewLine()
        
    print("Progress End...")
    CANDoc1.DocBuffer.close()
    CANC1RecordingDoc.close()
    CANC5RecordingDoc.close()
    pass


if __name__ == "__main__":
    main()
    pass