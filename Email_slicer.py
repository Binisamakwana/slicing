#collect email from user
#split the email using the @,(The first part as the user name, second part is gonna be saved as domain)
#split domain using (.)
def main():
    print("welcome to the email slicer")
    print (" ")
    
    email_input = input("input your email address : ")
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    
    print("username :" , username)
    print("domain :" , domain)
    print("extension :" , extension)
    
while True :
    main() 