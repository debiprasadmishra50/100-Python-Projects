## Automatic Birthday Wisher
***

> This project is an Automatic Birthday Wisher. Please follow these steps:
	
1. In ***birthdays.csv*** update the ***Recipient Name, Recipient email, year, month and day*** in respective column

2. Edit ***line 6*** the ***MAIL*** in birthday_wisher.py and put sender/your email in it

3. Edit ***line 7*** the ***APP_PASSWORD*** in birthday_wisher.py and put your password in it

> NOTE:

	For Yahoo mail users please generate a APP Pasword from your account and put the app password in the APP_PASSWORD field

### To run it everyday automatically, you need to put the code in the cloud. For this you can use ***[pythonanywhere.com](https://pythonanywhere.com)***

Follow These steps after creating an account in there

	1. Upload Files accordingly with proper folder names

	2. Consoles --> Bash

	3. Execute this: python3 <file_name>.py

	4. Dashboard --> Tasks --> Set the time in UTC and In RUN field write this: 
	        python3 birthday_wisher.py

	5. Create


<br><br>


### To Test the Project follow first 3 steps and then do this

> Install pandas module first

```
>> pip install pandas
```

> Run the birthday_wisher.py file 
```
>> python birthday_wisher.py

```
