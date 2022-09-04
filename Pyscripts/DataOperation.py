"""Copyright [2022] [Li, Yong Xin], [Li, Zi Yan]

   Author: Li, Yong Xin (li.yongxin@foxmail.com)

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


class StrOperation(object):
    """Several operation methods of str.
    
    Args: None

    Attributes: None
    """
    def __init__(self) -> None:
        """Several operation methods of str.
        
        Args: None

        Attributes: None
        """
        pass

    def StrToHex(self, HexStr ) -> bytes:
        """Convert str to hex.

        Blanks are allowed exist any where in 'HexStr'.
        Header '0x' is allowed because it will be ignored automatically.
        
        Args:
            HexStr: A hex str which will be converted to dec bytes.
                examples: "ABC", "0x  ABC",  " 0x A B C", " 0x AB C"
                All above examples will be seen as "ABC".

        Returns: A bytes type convertion result.

        Raises:
            ValueError: Your input includes intolerable characters.
                The entire program will print a hint string and exit.
        """
        HexStr = HexStr.strip()
        HexStr = HexStr.strip('0x')
        HexStr = HexStr.strip('0X')
        NoBlankString = HexStr.replace(" ","")

        OddFlag = len(NoBlankString) % 2

        if(OddFlag == 1):
            ExecutedString = '0' + NoBlankString
        else:
            ExecutedString = NoBlankString
        try:
            hexBytes = bytes.fromhex(ExecutedString)
        except ValueError:
            print("\n\n\ValueError: 'StrOperation.StrToHex' method.")
            print("There exits intolerable characters in your input.")
            return ValueError
        else:
            return hexBytes
        pass

    def StrToDec(self, HexStr , Endianness = 'big', CANCompanyFormat="") -> int:
        """Convert str to dec.

        Blanks are allowed exist any where in 'HexStr'.
        A header '0x' is allowed because it will be ignored automatically.
        
        Args:
            HexStr: A hex str which will be converted to dec bytes.
                examples: "ABC", "0x  ABC",  " 0x A B C", " 0x AB C"
                All above examples will be seen as "ABC".
            Endianness: <optional> default="big", ["big" | "little"]
            CANCompanyFormat: <optional>, ["intel" | "motolora"],
                When you wanna analyse a CAN message, you can set
                'CANCompanyFormat' to coresponding company, the 'Endianness'
                will change to right value forcelly.

        Returns: A int type convertion result.

        Raises:
            ValueError: Your input includes intolerable characters.
                The entire program will print a hint string and exit.
        """
        if(CANCompanyFormat.lower() == 'intel'):
            Endianness = 'little'
        elif(CANCompanyFormat.lower() == 'motolora'):
            Endianness = 'big'
        HexBytes = self.StrToHex( HexStr )
        DecResult = int.from_bytes( HexBytes, byteorder = Endianness )
        return DecResult
        pass
pass


def main():
    print(StrOperation().StrToHex("CAE"))
    print(StrOperation().StrToHex("CAE"))
    print(StrOperation().StrToHex("  C AE"))
    print(StrOperation().StrToHex("0x  C AE"))
    print(StrOperation().StrToDec("CAE", Endianness="big"))
    print(StrOperation().StrToDec("  C AE", CANCompanyFormat="Motolora"))
    print(StrOperation().StrToDec("CAE", Endianness="little"))
    print(StrOperation().StrToDec("0x  C AE", CANCompanyFormat="Intel"))
    pass

if __name__ == "__main__":
    main()