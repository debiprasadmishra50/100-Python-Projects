## 
<h2 style="font-family: Times New Roman, sans-serif; font-size: 40">Workout Tracking App</h2>

***

> This is a Automated Application Which will help you track your Workout. 

> Please follow these steps to get your application working, you will need a ***Google spreadsheet*** and ***API KEY*** for NAtural Language Queries

> 1. Go to [THIS LINK](https://docs.google.com/spreadsheets/d/19mXz3dF6Z4mlIemn0QMIIm-zDYz0aQcQJxhfjYboaoc/edit?usp=sharing) and create a copy of the My Workouts Spreadsheet. You may need to login/register.

> 2. Go to the [Nutritionix API](https://www.nutritionix.com/business/api) website and select "Get Your API Key" to sign up for a free account. Double check your spam folder (and/or your gmail "promotions" tab) for the Nutritionix verification email.

> 3. Once logged in, you should be able to access your ***API KEY and App ID***

> 4. Edit ***APP_ID*** and ***API_KEY*** field with your ***API KEY and App ID***:       ***line 6, 7***

> 5. [Log into Sheety](https://sheety.co/) with your Google Account (the same account that owns the Google Sheet you copied in step 1). Make sure the email matches between your Google Sheet and Sheety Account.

> 6. In your project page, click on **"New Project"** and create a new project in Sheety with the name **"Workout Tracking"** and paste in the **URL** of your own **"My Workouts" Google Sheet**.

> 7. In **Authentication** field Select **Basic** and provice your **Account Username and Password** and Save the changes

> 8. The Program will ask for your ***Gender, Weight(Kg), Height(cm), and Age*** and your ***Username and Password*** for Security Validation and it will be stored in your ***Local Machine*** to Ease up your work 

> 9. When asking for **What Exercises/Workouts did you do today:**: You can write your daily workouts, Sample:
```
	Today I ran for 3 kilometers are cycled for 5 kilometers
	I ran for 3 miles 
	walked 10 kms
	Lifted weights and did jogging for 2 hours
	Today I ran and hit the gym for 2 hours and lifted dumbells and benchpress for 1hr
	... etc
```

> 10. The program will calculate your calories burned and date,time duration, exercise and save into the spreadsheet automatically *which you can also view from the Application itself*.

#### Enjoy Working Out and Keep Track of your data

<br><br>


#### Requirements
> Install requests, and prettytable module first

```
>> pip install requests
>> pip install prettytable
```

> Run the track_workout.py file 
```
>> python track_workout.py

```
