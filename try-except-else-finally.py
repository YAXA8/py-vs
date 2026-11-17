try:
    num1 = input("please ejsdkhsdkjf: ")
    num2 = input("sdljfsdlfkds")
    num1_c = float(num1)
    num2_c = float(num2)
    res = num1_c / num2_c
    print(res)
except ZeroDivisionError:
    print("bar sefr taqsim nemishe")
except ValueError:
    print("string dari")
else:
    print("salam")
    print(res + 10)
finally:
    print("end of program")