__author__ = 'kleung'

# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"

pos = text.find(':')
str_num = text[pos + 1:]  # the colon here means extract text starting from pos + 1 to the end
num = float(str_num)
print num


