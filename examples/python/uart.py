#!/usr/bin/env python

# Author: Manivannan Sadhasivam <manivannan.sadhasivam@linaro.org>
# Copyright (c) 2018 Linaro Ltd.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Example Usage: Sends data through UART

import mraa
import time
import sys

# serial port
port = "/dev/ttyACM0"

data = 'Hello Mraa!'

# initialise UART
uart = mraa.Uart(port)

# send data through UART
uart.write(bytearray(data, 'utf-8'))

# receive data through UART
uart.read(bytearray(rev, 'utf-8'))

print('The received data is:'+rev)
