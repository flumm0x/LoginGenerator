'''
Generate a tab-delimited POL login file that will be of the format:

userId	password	emailAddress

For now we will have common password types 'someLoginxxx' where x's are numbers. We will strip the domain name from the address and just keep the username left behind.
'''

from string import digits
import sys
import random
import string
#Generate username by removing any numerals from the account name and removing the domain
def getUserName(emailAddress):
	userName = emailAddress.split("@")[0]	#leave the domain off	
	return userName

'''
We'll generate a strict password based off of a basic input. Make both a string
@param prefix:	The prefix for the password.
@param indexSuffix:	The numerical index to generate.
'''
def generatePassword(prefix, indexSuffix):
	password = str(prefix) + str(indexSuffix)	#convert both to string and concatenate - in runtime the indexSuffix would be incremented
	return password
'''
Generate a password using a random seed generator.
@param size:	Set to eight characters, can be increased with impunity
@param chars:	Set the chars variable to strict ASCII and to uppercase only, concatenate with numbers. Both set as a string
'''
def generateRandomPassword(size=8,chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
'''
We'll create the login file with strictly formed passwords, as requested by the user.
@param emailFile:	The file of just email addresses to be processed.
@param POLLogins:	The complete output file.
@param testPrefix:	The formatted password for the user to adhere to (will be passed in on the command line)
@param testIndexSuffix:	The numerical index to append to the passwords that will be generated. Usually you would start at 1
'''
def createLoginFileWithLikePaswords(emailFile,POLLogins,testPrefix,testIndexSuffix):
	file = open(emailFile,'r')
	logins = open(POLLogins,'w')
	for line in file:
		testIndexSuffix = testIndexSuffix + 1
		testAddress = line.strip()
		logins.write(getUserName(testAddress) + "\t" + generatePassword(testPrefix,testIndexSuffix) + "\t" + testAddress + "\n")
	return logins

'''
We'll create the login file with random passwords if that is what's requested by the user.
@param emailFile:	The file of just email addresses to be processed.
@param POLLogins:	The completed output file.
'''
def createLoginFileWithRandomPasswords(emailFile,POLLogins):
	file = open(emailFile,'r')
	logins = open(POLLogins,'w')
	for line in file:
		testAddress = line.strip()
		logins.write(getUserName(testAddress) + "\t" + generateRandomPassword() + "\t" + testAddress + "\n")
	return logins

def main():
	emailFile = sys.argv[1]
	POLLogins = sys.argv[2]
	passwordRequirements = sys.argv[3]
	if (passwordRequirements.lower() == "random"):
		createLoginFileWithRandomPasswords(emailFile,POLLogins)	
	else: 
		createLoginFileWithLikePaswords(emailFile,POLLogins,passwordRequirements,0)
main()