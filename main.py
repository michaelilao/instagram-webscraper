import login_controller as login
path = "/mnt/c/SE/Github/instagram-webscraper/chromedriver.exe"

username = input("Enter your username: ")
password = input("Enter your password: ")
user_to_find = input("Enter user to be searched: ")
run_headless = input("Run headless 0/1? ")
if(run_headless == 1):
    run_headless = True
elif(run_headless == 0):
    run_headless = False


login.privateuser(username,password,user_to_find,path,run_headless)
