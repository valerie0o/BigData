# Yiwen Zhang Lab3
# Part A
urls = ['https://www.yelp.com/biz/levain-bakery-new-york']

i=0
while i < 5:
    nextPageStart = 20*(i+1)
    nextString = 'https://www.yelp.com/biz/levain-bakery-new-york?start=' + str(nextPageStart)
    urls.append(nextString)
    i +=1     
print(urls)

#Part B
print('Welcome to the palindrome finder, my friend')

attempt = input('Enter a word or phrase:\n>>')
while attempt != '':
    
    cleanedAttempt = attempt.replace(',', '').replace(' ','').replace('\'', '').replace('.','')
    reverseAttempt = cleanedAttempt[::-1]
    if cleanedAttempt.lower() == reverseAttempt.lower():
        print('Yes, that is a Palindrome')
    else:
        print('No, it is not a palindorme')
   
    attempt = input('Enter a word or phrase or press ENTER to end:\n>>')
print('Thank you for playing')