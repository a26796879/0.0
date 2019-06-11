class Phone:
    def price(self):
        print ()
    camera_count = 0
    screen_size = 0


class Google_phone(Phone):

#,camera_count,screen_size
    def __init__(self, price , camera_count, screen_size):
        price = 10
        camera_count = 3
        screen_size = 5

    def special_freature(self):
        userinput = eval(input('Google_phone.special_freature input a list: '))
        num = 1
        for i in list(userinput):
            num *= i
        print(num)


class Taiwan_phone:
    price = 20
    camera_count = 1
    screen_size = 3

    def __init__(self, price, camera_count, screen_size):
        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size

    def special_freature(self):
        userinput = int(input('Taiwan_phone.special_freature input a number: '))

        def fib(n):
            if n <= 2:
                return 1
            else:
                return fib(n-1)+fib(n-2)
        print(fib(userinput))


class Apple_phone:
    price = 30
    camera_count = 2
    screen_size = 10

    def __init__(self, price, camera_count, screen_size):
        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size

    def special_freature(self):
        import ast
        userinput = ast.literal_eval(
            input('Apple_phone.special_freature input 2 numbers: '))
        inputs = []
        for a in range(userinput[0]-userinput[1]+1, userinput[0]+1):
            inputs.append(a)
        num = 1
        for i in inputs:
            num *= i
        print(num)


print (Google_phone.price)
#Taiwan_phone.special_freature()
#Apple_phone.special_freature()
