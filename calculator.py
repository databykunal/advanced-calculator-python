# calculator
print("===========================  kunal's advanced calculator ============================")
def calculator():
        ope = 1
        while ope:

                    print("please choose an operation\n 1.addition\n 2.subtraction\n 3.multiplication\n 4.division\n 5.exiting calculator.....Thank you👍 ") 
                    ope = input("select your number to oprate :---  ")
                    if ope == "5":
                        print("EXIT ! PLS try again ")
                        break
                    number = []
                    num = int(input("how many numbes do you want to calculate :----   "))

                    for i in range(num):
                            nums = int(input("entre your numbers by  :----   "))
                            number.append(nums)

                            # n= " ".joi(number)

                        

                    # value1 = int(input("entre your first value :----   "))
                    # value2 = int(input("entre your second value :----    "))

                    if ope == "1":
                           print("sum of these number is :", sum(number))
                            # print(f"Result {value1} + {value2} = {value1+value2}")
                                    
                    elif ope =="2":
                           result = number[0]
                           for n in number[1:]:
                                  result -=n
                                  print("Final Result = :",result)

                
                                    # print(f"Result {value1} - {value2} = {value1 - value2}")
                    elif ope == "3":
                           mul = number[0]
                           for m in number[1:]:
                                  mul *= m
                                  print("Final Result =",mul)


                                        # print(f"Result {value1} * {value2} = {value1 * value2}")

                    elif ope == "4":

                            division = number[0]
                            try:
                                    
                                    for d in number[1:]:
                                        division/=d
                                    print("Final Result =: ",division)
                            except  ZeroDivisionError:
                                    print("ERROE ! DIVISION BY ZERO ARE NOT allow ")
                                
                                # if value2 == 0:
                                #     print("ERROR")
                                # else:
                                #     print(f"Result {value1} / {value2} = {value1 / value2}")
                    else:
                        print("INVALIDED VALUES")



calculator()


