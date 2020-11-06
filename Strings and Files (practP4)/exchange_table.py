# Write a function exchangeTable that gives a table of euros values and their equivalent
# values in pounds, using an exchange rate of 1.10 euros to the pound. The euros values
# should be 0, 1, 2, . . . , 20, and should be right justified. The pounds values should be
# 6
# right justified and given to two decimal places (i.e. with decimal points lined up and
# with pence values after the points).

def exchangeTable(pounds):
    return round(pounds * 1.1, 2)

print(exchangeTable(6))