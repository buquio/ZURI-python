print("bukola")

# /////////
boy = 12
girl = 13
print(girl)

# /////////
print("Hello World")


# ////////
name = "Mike"

print("His name is %s" % name)

# /////////
name = "Mike"
age = 55  # number -d

print("His name is %s and he is %d years old" % (name,age))

# //////
sampleList = ['mike','love', 'dove']

print("some text %s % sampleList")

# //////REVERSE
string = 'UPPERCASE STRING'

print(string.lower())
print(string[::-1])  # reversing string

# ///////
voice = "shout "

print(voice * 5)

# ///////
age = 18
if(age >= 18):
    print("Customer can purchase ticket for movie")
    if (age < 18):
        print("customer is not allowed to watch this movie")

# /////////
age = 18
height = 4
if(age >= 18 and height >=5):
    print("Person can get on this ride")
    elif (age < 18 or height < 5):
        print("Person cannot get on this ride")
        else:
            print("Error, something went wrong with your inputs")



# ///////
my_name = 'popoola'

print(welcome my_name)
# ans: welcome my_name

print('welcome {}'.format(my_name))
# ans: welcome popoola




I'm sure you have seen the videos on Classes. If you haven't, please do. It will make this a whole lot easier.
1. Create a budget class.
2. In it, create a balance list for the categories ("Food, Data, Healthcare..."). Maybe something like this, balance=[0, 0, 0].
3. Then initialize the class with arguments 'self and category'. Set self.category = category.
4. Create an operations method that calls the deposit, withdraw, transfer and check balance methods inside the class all with the 'self' arguments. Just as the ATM project.
5. In these methods from number 4, write functions that would be able to get input from user and manipulate the balance list. 6. For example, the deposit function can take a certain amount, say 200 as input from user and then you access the balance list  (budget.balance) at the index of the category chosen. (Note that the balance list is zero-index based). Then you add the 200 to it.
7. The balance list should now be able to read something like this [200, 0, 0] after the manipulation.
8. Dealing with transfer just means you add the user input to one category and minus it from another category.
9. There should be an init() function outside the budget that can ask which category the user wants. It can be 1. Food, 2. Data, 3. Healthcare. So anything the user chooses, you can instantiate the class based on it.
10. If the user chooses 1(Food), then create an instance as such;
budget_food = budget(0) because it is zero index based. Then call the operation method as such;
budget_food.operation().
Everything should work well, I believe:hugging_face:
Hope this helps.

//////////////////
the Naira symbol is a hex value of 20A6, to be able to parse this, you need to understand ASCII and UTF8. what you can do is convert hex to int and then find the ascii value of it, from yesterday's class, we did functions, so we can write a simple function for this. I won't include exception handling because we haven't learnt it.
def convert_hex_to_symbol(hex_string: str) -> chr:
    return chr(int(hex_string, 16))
# call it
naira_symbol = convert_hex_to_symbol("20A6")
or use a lambda to do this
symbol_processed = lambda value: chr(int(value, 16))
# call your lambda
naira_symbol = symbol_processed("20A6")
then you can print naira_symbol or use it the way you want
the cool thing is, we can also process other symbols not just naira, as long as you know the hex values, now here is a link of hex values for the symbols you need:
currency symbols -> https://www.w3schools.com/charsets/ref_utf_currency.asp
letter like symbols -> https://www.w3schools.com/charsets/ref_utf_letterlike.asp
General punctuation -> https://www.w3schools.com/charsets/ref_utf_letterlike.asp
(edited)
w3schools.comw3schools.com
HTML Unicode UTF-8
Well organized and easy to understand Web building tutorials with lots of examples of how to use HTML, CSS, JavaScript, SQL, PHP, Python, Bootstrap, Java and XML.
w3schools.comw3schools.com
HTML Unicode UTF-8
Well organized and easy to understand Web building tutorials with lots of examples of how to use HTML, CSS, JavaScript, SQL, PHP, Python, Bootstrap, Java and XML.


///////////
I have a question and its about the str methods; str formatting basically.
Please are the methods different/ which is the best practice between the two?
name = 'Seyi'
print ('His name is %s '  % name)
#and
print ('His name is {}' .format(name))
# and
print(f” his name is {name}”)

