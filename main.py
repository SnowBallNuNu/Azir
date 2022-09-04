#    Copyright [2022] [Li, Yong Xin], [Li, Zi Yan]
#
#    Author: Li, Yong Xin (li.yongxin@foxmail.com)
#            Li, Zi Yan (ziyan.li-cn@foxmail.com)
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from cgitb import text
import sys
import os
import pandas as pd
from xmlrpc.client import NOT_WELLFORMED_ERROR

sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'\\Pyscripts')
import Pyscripts.FileOperation as FO
import Pyscripts.DataOperation as DO
from ast import Import
from http.client import CONTINUE

if __name__ == "__main__":
    CANDoc1 = FO.FilePack( FileName="BusLogging_2022-09-01_16-09-55.asc" )

    Last_time_C1 = 0 
    Pre_time_C1 = 0
    Last_time_C5 = 0 
    Pre_time_C5 = 0
    dec_extracted_LN_Last_Data_C1 = 0 
    dec_extracted_LN_Pre_Data_C1 = 0
    dec_extracted_RN_Last_Data_C1 = 0
    dec_extracted_RN_Pre_Data_C1 = 0
    dec_extracted_LN_Last_Data_C5 = 0 
    dec_extracted_LN_Pre_Data_C5 = 0
    dec_extracted_RN_Last_Data_C5 = 0
    dec_extracted_RN_Pre_Data_C5 = 0

    Time_Index = 0
    text_line_index = 0
    text_line0_flag =  -1

    if(os.path.exists("C1Recording.txt") == True):
        os.remove("C1Recording.txt")
    if(os.path.exists("C5Recording.txt") == True):
        os.remove("C5Recording.txt")
    if(os.path.exists("CANC1RecordingDoc.csv") == True):
        os.remove("CANC1RecordingDoc.csv")
    if(os.path.exists("CANC5RecordingDoc.csv") == True):
        os.remove("CANC5RecordingDoc.csv")
    if(os.path.exists("C1.txt") == True):
        os.remove("C1.txt")
    if(os.path.exists("C5.txt") == True):
        os.remove("C5.txt")

    CANC1RecordingDoc = open("C1Recording.txt", mode='w', encoding='utf-8' )
    CANC1R = open("C1.txt", mode='w', encoding='utf-8' )
    CANC5RecordingDoc = open("C5Recording.txt", mode='w', encoding='utf-8' )
    CANC5R = open("C5.txt", mode='w', encoding='utf-8' )

    while(CANDoc1.LineBuffer != '') :
        KeyWordFlag = -1

        #C1
        KeyWordFlag = CANDoc1.LineBuffer[14:19].find(" C1 ")
        if(KeyWordFlag != -1):
            dec_extracted_LN = DO.StrOperation().StrToDec(
                                CANDoc1.LineBuffer[41:45], "big")
            
            dec_extracted_RN = DO.StrOperation().StrToDec(
                                CANDoc1.LineBuffer[53:57], "big")


            #calculate ave_spd
            Time_Str_Value = CANDoc1.LineBuffer[:11]

            for site in Time_Str_Value:
                # print("time_Decade: %s",site)
                if(site == ' '):
                    Time_Index = Time_Index + 1
                    CONTINUE                                
                else:
                    time = float(Time_Str_Value[Time_Index:11])
                    Time_Index = 0
                    CONTINUE

            Last_time_C1 = Pre_time_C1 
            Pre_time_C1 = time
            dec_extracted_LN_Last_Data_C1 = dec_extracted_LN_Pre_Data_C1
            dec_extracted_LN_Pre_Data_C1 = dec_extracted_LN
            dec_extracted_RN_Last_Data_C1 = dec_extracted_RN_Pre_Data_C1
            dec_extracted_RN_Pre_Data_C1 = dec_extracted_RN

            dt = float(round((Pre_time_C1 - Last_time_C1)/0.02)*0.02)

            dec_extracted_LN__dy = dec_extracted_LN_Pre_Data_C1 - dec_extracted_LN_Last_Data_C1
            if(dec_extracted_LN__dy < 0):
                dec_extracted_LN__dy = dec_extracted_LN_Pre_Data_C1 + 1024 - dec_extracted_LN_Last_Data_C1
                
            dec_extracted_RN__dy = dec_extracted_RN_Pre_Data_C1 - dec_extracted_RN_Last_Data_C1
            if(dec_extracted_RN__dy < 0):
                dec_extracted_RN__dy = dec_extracted_RN_Pre_Data_C1 + 1024 - dec_extracted_RN_Last_Data_C1

            ave_spd_LDrvnWhlRotlDistPlsCtr = float(3.6*0.04239*dec_extracted_LN__dy/dt)
            ave_spd_RDrvnWhlRotlDistPlsCtr = float(3.6*0.04239*dec_extracted_RN__dy/dt)

            print("%s,%d,%d\n" % (
                CANDoc1.LineBuffer[:11], dec_extracted_LN ,dec_extracted_RN,), file = CANC1RecordingDoc)	

            print("%f,%d,%d,%d,%d,%f,%f,%f\n" % (
                Last_time_C1, 
                dec_extracted_LN ,dec_extracted_RN,
                dec_extracted_LN__dy,
                dec_extracted_RN__dy,
                dt,
                ave_spd_LDrvnWhlRotlDistPlsCtr,
                ave_spd_RDrvnWhlRotlDistPlsCtr), file = CANC1R)		




                
                						            
        
        #C5
        KeyWordFlag = CANDoc1.LineBuffer[14:19].find(" C5 ")
        if(KeyWordFlag != -1):
            dec_extracted_LN = DO.StrOperation().StrToDec(
                                CANDoc1.LineBuffer[41:45], "big")
            
            dec_extracted_RN = DO.StrOperation().StrToDec(
                                CANDoc1.LineBuffer[53:57], "big")


            #calculate ave_spd
            Time_Str_Value = CANDoc1.LineBuffer[:11]
            for site in Time_Str_Value:
                # print("time_Decade: %s",site)
                if(site == ' '):
                    Time_Index = Time_Index + 1
                    CONTINUE                                
                else:
                    time = float(Time_Str_Value[Time_Index:11])
                    Time_Index = 0
                    CONTINUE

            Last_time_C5 = Pre_time_C5 
            Pre_time_C5 = time
            dec_extracted_LN_Last_Data_C5 = dec_extracted_LN_Pre_Data_C5
            dec_extracted_LN_Pre_Data_C5 = dec_extracted_LN
            dec_extracted_RN_Last_Data_C5 = dec_extracted_RN_Pre_Data_C5
            dec_extracted_RN_Pre_Data_C5 = dec_extracted_RN

            dt = float(round((Pre_time_C5 - Last_time_C5)/0.02)*0.02)
            dec_extracted_LN__dy = dec_extracted_LN_Pre_Data_C5 - dec_extracted_LN_Last_Data_C5
            if(dec_extracted_LN__dy < 0):
                dec_extracted_LN__dy = dec_extracted_LN_Pre_Data_C5 + 1024 - dec_extracted_LN_Last_Data_C5
            dec_extracted_RN__dy = dec_extracted_RN_Pre_Data_C5 - dec_extracted_RN_Last_Data_C5
            if(dec_extracted_RN__dy < 0):
                dec_extracted_RN__dy = dec_extracted_RN_Pre_Data_C5 + 1024 - dec_extracted_RN_Last_Data_C5
            
            ave_spd_LNonDrvnWhlRotlDistPC = float(3.6*0.04239*dec_extracted_LN__dy/dt)
            ave_spd_RNonDrvnWhlRotlDistPC = float(3.6*0.04239*dec_extracted_RN__dy/dt)

            print("%s,%d,%d\n" % (CANDoc1.LineBuffer[:11], dec_extracted_LN,
                                 dec_extracted_RN), file = CANC5RecordingDoc)	
            print("%f,%d,%d,%d,%d,%f,%f,%f\n" % (
                Last_time_C5, 
                dec_extracted_LN ,dec_extracted_RN,
                dec_extracted_LN__dy,
                dec_extracted_RN__dy,
                dt,
                ave_spd_LNonDrvnWhlRotlDistPC,
                ave_spd_RNonDrvnWhlRotlDistPC), file = CANC5R)	

        text_line0_flag =  0
        # print("%d" % (text_line0_flag))
        CANDoc1.ReadNewLine()
        
    print("Progress End...")
    CANDoc1.DocBuffer.close()
    CANC1RecordingDoc.close()
    CANC5RecordingDoc.close()

    # C1_CSV = pd.read_csv("C1Recording.txt",delimiter="\t")
    # C1_CSV.to_csv("CANC1RecordingDoc.csv", encoding='utf-8', sep=';', index=False)
    # C5_CSV = pd.read_csv("C5Recording.txt",delimiter="\t")
    # C5_CSV.to_csv("CANC5RecordingDoc.csv", encoding='utf-8', sep=';', index=False)
    C1_CSV = pd.read_csv("C1.txt",delimiter="\t")
    C1_CSV.to_csv("CANC1RecordingDoc.csv", encoding='utf-8', sep=';', index=False)
    C5_CSV = pd.read_csv("C5.txt",delimiter="\t")
    C5_CSV.to_csv("CANC5RecordingDoc.csv", encoding='utf-8', sep=';', index=False)
    
    pass