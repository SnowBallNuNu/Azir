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


class FilePack(object):
    """Components of decomposed target file.

    Users must supply a str which includes the target file's full name when
        creating a 'FilePack' class instantiation.
    After creating a 'FilePack' class instantiation, the target file will be
        opened.
    LineBuffer will be updated automatically after calling 'ReadNewLine' method.
    
    Args:
        FileName: A str includes the target file's full name.
            example: FileName = "CANBusLog.txt"

    Attributes:
        DocName: Current file's name.
        DocBuffer: Opened file object.
        LineBuffer: str's buffer by ReadNewLine function.
    """

    def __init__(self, FileName) -> None:
        """Components of decomposed target file.

        Users must supply a str which includes the target file's full name
            when creating a 'FilePack' instantiation.
        After creating a 'FilePack' instantiation, the target file will be
            opened.
        LineBuffer will be updated automatically after calling 'ReadNewLine'
            method.
        
        Args:
            FileName: A str includes the target file's full name.
                example: FileName = "CANBusLog.txt".

        Attributes:
            DocName: Current file's name.
            DocBuffer: Opened file object.
            LineBuffer: str's buffer by ReadNewLine function.
        """
        self.DocName = FileName
        print("Analyse file:", self.DocName)
        self.DocBuffer = open(self.DocName, mode='r', encoding='utf-8')
        self.LineBuffer = self.DocBuffer.readline()

    def ReadNewLine(self) -> str:
        """Read a new line from DocBuffer saving to 'LineBuffer' and return a str.
        
        Args: None.

        Returns: A str of reading's result.
        """
        self.LineBuffer = self.DocBuffer.readline()
        return self.LineBuffer

    def Close(self) :
        """Close Target file which opended by create a 'FilePack' instantiation.
        
        Args: None.

        Returns: None.
        """
        self.DocBuffer.close()
