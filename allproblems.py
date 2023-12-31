def task1():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if 7 <= age <= 17:  # check the age
        school_year = age - 6
        if school_year <= 11:
            course = (school_year - 1) // 2 + 1
            print(
                f"Hello, {name}! You are at {course} course and have {age - 9} years of programming experience. Sounds cool!")
        else:
            print(
                f"Hello, {name}! You are at university and have {age - 17} years of programming experience. Sounds cool!")
    elif 18 <= age <= 21:
        print(f"Hello, {name}! You are at university and have {age - 17} years of programming experience. Sounds cool!")
    else:
        print(f"Hello, {name}! You are entrepreneur. Sounds cool!")


def task2():
    a = int(input())
    b = int(input())
    if a > b:
        a %= b
    else:
        b %= a
    gcd = a + b
    print(gcd)
    a1 = float(input())
    a2 = float(input())
    a3 = float(input())
    a4 = float(input())
    d = float(input())
    p1 = (a1 + a2 + d) / 2
    p2 = (a3 + a4 + d) / 2
    s1 = (p1 * (p1 - a1) * (p1 - a2) * (p1 - d)) ** (1 / 2)
    s2 = (p2 * (p2 - a3) * (p2 - a4) * (p2 - d)) ** (1 / 2)
    s = s1 + s2
    print(s)


def task31():
    n, k = map(int, input('Enter two integers separated by space: ').split())  # Enter the values of n and k separated by a space and convert them to integers
    sum_nums = 0
    count = 0

    for _ in range(n):  # Run a loop to input n elements
        num = int(input())  # Enter a number and convert it to an integer
        if count < k:
            sum_nums += num
            count += 1

    mean1 = sum_nums / k  # Calculate the arithmetic mean

    print("The arithmetic mean:", mean1)  # Output the result


def task32():
    n, k = map(int, input('Enter two integers separated by space: ').split())  # Enter the values of n and k separated by a space and convert them to integers
    sum_nums = 0
    count = 0

    for _ in range(n):  # Run a loop to input n elements
        num = int(input())  # Enter a number and convert it to an integer
        if count < k:
            sum_nums += num
            count += 1

    harmonic_mean = k / sum_nums  # Calculate the harmonic mean

    print("The harmonic mean:", harmonic_mean)  # Output the result


def task33():
    n, k = map(int, input('Enter two integers separated by space: ').split())  # Enter the values of n and k separated by a space and convert them to integers
    max_num = None

    for _ in range(n):  # Run a loop to input n elements
        num = int(input())  # Enter a number and convert it to an integer
        if max_num is None or num > max_num:  # Check if the current number is the largest
            max_num = num

    print("The maximum element:", max_num)  # Output the result


def task34():
    n, k = map(int, input('Enter two integers separated by space: ').split())  # Enter the values of n and k separated by a space and convert them to integers
    max_num = None
    second_max_num = None

    for _ in range(n):  # Run a loop to input n elements
        num = int(input())  # Enter a number and convert it to an integer
        if max_num is None or num > max_num:  # Check if the current number is the largest
            second_max_num = max_num
            max_num = num
        elif second_max_num is None or num > second_max_num:  # Check if the current number is the largest
            second_max_num = num

    print("The second maximum element:", second_max_num)  # Output the result


def task35():
    n, k = map(int, input('Enter two integers separated by space: ').split())  # Enter the values of n and k separated by a space and convert them to integers
    min_num = float('inf')

    for _ in range(k):  # Run a loop to input k elements
        num = int(input())  # Enter a number and convert it to an integer
        if num < min_num:  # Check if the current number is the smallest
            min_num = num

    print(f"The minimum element:", min_num)  # Output the result


def task36():
    n, k = map(int, input('Enter two integers separated by space: ').split())  # Enter the values of n and k separated by a space and convert them to integers
    min_num = float('inf')
    second_min_num = float('inf')

    for _ in range(k):  # Run a loop to input k elements
        num = int(input())  # Enter a number and convert it to an integer
        if num < min_num:  # Check if the current number is the smallest
            second_min_num = min_num
            min_num = num
        elif num < second_min_num and num != min_num:  # Check if the current number is the smallest
            second_min_num = num

    print("The second minimum element:", second_min_num)  # Output the result


def task4():
    n = int(input('Enter a natural number: '))  # input of a natural number
    if n < 0:
        print('This number is not natural.')
    else:
        k = 1
        summ1 = 0
        while k <= n:
            summ1 += k ** 3  # sum of cubes of all numbers up to n (n included)
            k += 1
        print('a:', summ1)  # output of the total sum of cubes

        def sfact(n):  # determination of the sum of factorials depending on n
            summ2 = 0
            fact = 1
            for i in range(1, n + 1):
                fact *= i
                summ2 += fact  # sum of factorials of all numbers up to n (n included)
            return summ2

        print('b:', sfact(n))  # output of the total sum of factorials


def task5():
    n = int(input())  # Enter a natural number n
    expected_sum = n * (n + 1) // 2  # Calculate the expected sum of numbers from 1 to n
    actual_sum = 0
    for _ in range(n - 1):  # Run a loop to enter n - 1 numbers
        num = int(input())  # Enter a number
        actual_sum += num
    missing_num = expected_sum - actual_sum
    print(f"The missing number:", missing_num)  # Output of the result


def task6():
    n = int(input('Enter a number: '))  # input of a number of an integer in row

    def f(n):  # determination of Fibonacci number depending on n
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n >= 2:
            return f(n - 1) + f(n - 2)

    print(f(n))  # output of the desired Fibonacci number


def task7():
    sequence = input().split()  # a sequence of numbers is entered

    current_number = None
    current_count = 0

    max_number = None
    max_count = 0

    for number in sequence:
        if number == current_number:  # If the number is equal to the current number, increase the current number
            current_count += 1
        else:  # Otherwise, update the current number and quantity, and compare with the maximum
            current_number = number
            current_count = 1

            if current_count > max_count:
                max_number = current_number
                max_count = current_count

    print(max_number, max_count)  # output of the result


def task8():
    n = int(input("Enter a number: "))

    power = 1
    while power <= n:
        power <<= 1

    power >>= 1
    print("The greatest integer power of two not exceeding", n, ":", power)


def task9():
    vvod = input('Enter height, meters up per day, meters down per night, separated by spaces: ')
    numbers = list(map(int, vvod.split()))  # create a list of entered numbers
    h = numbers[0]
    a = numbers[1]
    b = numbers[2]
    for i in range(1, a + 1):
        days = (h - i) // (a - b) + 1  # calculation of the number of the days
    print('Number of days:', days)  # output of the number of the days


def task10():
    a = float(input('Enter a fractional number of degrees: '))
    # calculation of an integer number of seconds, minutes and hours
    s = int(a / 720 * 86400)
    m = s // 60
    h = m // 60
    if h >= 24 or h <= 0:
        h -= 24 * (h // 24)
        m -= 1400 * (m // 1440)
        s -= 86400 * (s // 86400)
    print('Hours, minutes, seconds: ', h, ', ', m, ', ', s,
          sep='')  # output of the resulting number of hours, minutes and seconds


while True:
    task = int(input('Enter the task number (if you want to stop the program, enter zero): '))
    if task == 1:
        task1()
    if task == 2:
        task2()
    if task == 31:
        task31()
    if task == 32:
        task32()
    if task == 33:
        task33()
    if task == 34:
        task34()
    if task == 35:
        task35()
    if task == 36:
        task36()
    if task == 4:
        task4()
    if task == 5:
        task5()
    if task == 6:
        task6()
    if task == 7:
        task7()
    if task == 8:
        task8()
    if task == 9:
        task9()
    if task == 10:
        task10()
    if task == 0:
        break
