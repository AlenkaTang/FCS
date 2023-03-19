import hashlib

file1 = open('/Users/tangalenka/CS/UID.txt', 'r')
uid = file1.read()
user_id = uid.splitlines()


file2 = open('/Users/tangalenka/CS/Password.txt','r')
pw = file2.read()
password = pw.splitlines()

file3 = open('/Users/tangalenka/CS/Salt.txt','r')
s = file3.read()
salt = s.splitlines()

file4 = open('/Users/tangalenka/CS/Hash.txt', 'r')
h = file4.read()
hash = h.splitlines()

#MD5hash implementation
def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

'''verification:
Going through the list and combine the password and salt value from the txt file
then put the concatenation result though the MD5hash function
if the output of the hash function match the hash value in the hash txt file
print "The input password and salt matches the hash value in the database" 
else print "The input password and salt DOES NOT match the hash value in the database"'''

ver = []
for n in range(len(hash)):
    concatenation = password[n] + salt[n]
    output = computeMD5hash(concatenation)
    if(output == hash[n]):
        ver.append("user_id: " + user_id[n] + " The input password and salt matches the hash value in the database")
    else:
        ver.append("user_id: " + user_id[n] + " The input password and salt DOES NOT match the hash value in the database")
for line in ver:
    print(line)

'''cracker system:
for each user_id, it goes through all the possible password and salt value with the correct format
and then do the concatenation of all the possible password and salt value
it then put the concatenation result as an input through the hash function
compare the output of the hashfunction to the hashvalue stored for that user
if it matches, store the passward and salt value associate to that user
at the end there will be a list with user_if and the password and salt value that matches it
'''
result = []
for index in range(len(user_id)):
    for i in range (1001):
        pw_temp = str(i).zfill(4)
        for j in range (101):
            salt_temp = str(j).zfill(3)
            s = pw_temp + salt_temp
            temp = computeMD5hash(s)
            if(temp == hash[index]):
                result_temp = "user id: " + user_id[index] + " password: " + pw_temp + " salt: " + salt_temp
                result.append(result_temp)

for line in result:
    print(line)
