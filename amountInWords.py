one = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ","Nine ", "Ten ", "Eleven ",
       "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "]

ten = ["", "", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]

# n is 1 or 2 digit number
def numToWords(n, s):
    str = ""
    # if n is more than 19, divide it
    if (n > 19):
        str += ten[n // 10] + one[n % 10]
    else:
        str += one[n]
    # if n is not 0
    if (n):
        str += s
    return str

#Driver Code.
n = int(input("Enter the Amount: "))

out = ""
out += numToWords((n // 10000000),"crore ")
out += numToWords(((n // 100000) % 100),"Lakh ")
out += numToWords(((n // 1000) % 100),"Thousand ")
out += numToWords(((n // 100) % 10),"Hundred ")
if (n > 100 and n % 100):
    out += "and "
out += numToWords((n % 100), "")

print(out)

