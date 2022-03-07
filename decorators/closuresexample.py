def outer_function(text):
    text=text
    def inner_function():
        print(text)
    return inner_function

myFunction=outer_function('Hello')
myFunction()