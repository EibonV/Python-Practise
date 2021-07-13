#作业5-8
users=['admin','bro','cat','dog','elephont']
for user in users:
	if user=='admin':
		print('Hello admin,would you like to see a status report?')
	else:
	    print(f'Hello {user},Thank you for loggin in again')

#作业5-9
user2s=[]
if user2s==[]:
    print('\nWe need to find some users!')

#作业5-10
current_users=['Admin','Brone','Lilice','John','Meimei']
new_users=['Alice','JOHN']
current_user2s=[current_user2.lower() for current_user2 in current_users]
new_user2s=[new_user2.lower() for new_user2 in new_users]
for current_user in current_user2s:
    if current_user in new_user2s:
        print('\nenter anather user name')
    else:
        print('\nuser name is unused')

#作业5-10
nums=['1','2','3','4','5','6','7','8','9']
for num in nums:
    if num=='1':
        print('\n1st')
    elif num=='2:':
        print('\n2nd')
    elif num=='3':
    	print('\n3rd')
    else:
    	print(f'\n{num}th')                         	    	