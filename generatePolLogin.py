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

#We'll need to generate a password for a user, taking it from the domain is not reliable, user input would be better for this
def generatePassword(prefix, indexSuffix):
	password = str(prefix) + str(indexSuffix)	#convert both to string and concatenate - in runtime the indexSuffix would be incremented
	return password

def generateRandomPassword(size=8,chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def createLoginFileWithLikePaswords(emailFile,POLLogins,testPrefix,testIndexSuffix):
	file = open(emailFile,'r')
	logins = open(POLLogins,'w')
	for line in file:
		testIndexSuffix = testIndexSuffix + 1
		testAddress = line.strip()
		logins.write(getUserName(testAddress) + "\t" + generatePassword(testPrefix,testIndexSuffix) + "\t" + testAddress + "\n")
	return logins

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