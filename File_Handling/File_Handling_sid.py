f_r = open('Natural_Language_Processing_sid2.py', 'r')
f_w = open('abc', 'w')
f_a = open('abc', 'a')

# Reading and writing a text file
for i in f_r:
    f_w.write(i)
    
# Reading and writing a jpg
f_rb = open('475526.jpg', 'rb')
f_wb = open('abc', 'wb')
for i in f_rb:
    f_wb.write(i)