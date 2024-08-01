# import statistics
# monthly_failed_attempts = [20, 17, 178, 33, 15, 21, 19, 29, 32, 15, 25, 19]

# mean_failed_attempt = statistics.mean(monthly_failed_attempts)
# print("mean:",mean_failed_attempt)

# mean_failed_attempt1 = statistics.median(monthly_failed_attempts)
# print("median:",mean_failed_attempt1)



# new_string = str(123)
# print(type(new_string))

# print("hello"+"world")

# print("hello".upper())


# # slicing substring from string
# print('HELLO'[1:4])
# print("HELLO".index('E'))
# print("HELLO".index('L'))


# my_list = [1,2,3,"A","b", "c","d"]
# # insert method is used to insert element in list
# my_list[1] = "aayush"
# my_list.insert(1,99)
# my_list.remove('A')
# my_list.append(100)
# print(my_list)




# IP = ['198.223.xx.xx', "198.101.xx.xx",'180.064.xx.xx','184.090.xx.xx']

# networks = []
# for address in IP:
#     networks.append(address[0:3])
# print(networks)



# number_list = []
# print("before appending")
# for i in range(7):
#     number_list.append(i)
# print(number_list)
# print("after appending")


# import re
# email_log = '''email recieved on 2nd june from user1@gmail.com. email recieved on 3nd june from user2@gmail.com.email recieved on 5nd june from user3@gmail.com.'''

# print(re.findall("\W+@\W+\.\W+",email_log))


with open("demofile.txt",'r') as file:
    file_text = file.read()
data  = file_text.split(',')


def login_check(user_list, current_user):
    counter = 0
    for i in user_list:
        if i == current_user:
            counter = counter+1
    if counter >= 3:
        print("you have tried to login 3 times")
    else:
        print("you can login !")

login_check(data, "bmoreno")



# approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
# print(",".join(approved_users))




