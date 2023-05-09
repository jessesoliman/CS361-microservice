# CS361-microservice
----Implementing the microservice----
  I added a user preferences button in your GUI - 
  
user_pref_button = ttk.Button(frame, text="User Preferences", command=run_micro)
user_pref_button.grid(row=4, column=1)

  Additionally, I defined a command run_micro() for button functionality.

def run_micro():
    with open('run-micro.txt', 'w', encoding="utf-8") as file:
        file.write('run')
      


----How to REQUEST data from the microservice----

I'm using the microservice communication method we learned in week 2(?) of class - communication via text files.
To do this, we will need two blank text files to act as the communication pipes.
  1) run-micro.txt
  2) receive-preferences.txt
**Pressing the user preferences button** will cause it to write 'run' to the run-micro.txt file.
The user_pref_microservice.py file will need to be run from terminal, and it will constantly be looking into the run-micro.txt file for the word 'run'
When user_pref_microservice.py sees 'run', it will pop open a new window for the user to fill in their user preferences.


----How to Receive data from the microservice-----

When the user submits their information, the microservice will write the user preferences in the form of a JSON into the receive-preferences.txt


----UML sequence diagram----

![image](https://user-images.githubusercontent.com/107973247/236981829-16b386c4-804e-466c-9ecc-de9818366e1d.png)
