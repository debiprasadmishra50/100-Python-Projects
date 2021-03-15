## Data Entry Automation
***

> This application is an example of automated data entry operation, i.e, it will take a Real-Estate Website link, search it and from which it will collect data about all the properties and their addresses, prices and the links to visit respective property. 
> Then it will fill out a google form submitting all the property values and at last you will have a spreadsheet of your own with all the properties listed from which you can search and decide which one's to rent/buy.


#### Please follow these steps to get your application working

#### Requirements
> Install requests, bs4, lxml selenium module

```
>> pip install requests bs4 lxml selenium
```

#### Configure your Application

> 1. Go to [https://docs.google.com/forms/](https://docs.google.com/forms/) and create your own form:

![google form image](https://img-a.udemycdn.com/redactor/raw/2020-08-25_15-17-58-d30a61ad923994f10cb01b2d3c9c0d48.png?8zl29cMHI8OrnwKqeRVeXsdjtAmzon61BfdIOf9mJMBzN9f6e7g3aFVFCzvA3DkMZp_5eiB8LpSjnbA7fUToKfhqAVFtFBdZK-PE4dtzjSxNNnLuk5KJlhHvAb0eNgB-hlpk9_mO6VykhcFe1XfdAaFv46_vH-3EW0L3kTVpjzzFSk5b)

> 2. Add 3 questions to the form, make all questions "short-answer":

<img src="https://img-a.udemycdn.com/redactor/raw/2020-08-25_15-20-27-e452a75ff00354982fbac16869f59e1d.png?cwDNe-jcVTv5Tg_xXma2ei418HTOZbnZM4J1yffrwCkxm7-KBkxkvXCrmisZKE73G2nTxjoRbdMbam-DlCjsrzVhxLtVXt9KSDET9BRlPP98pHvWHLkCvu-3F53Bp51eTZULQpBEW7LnlWXU1looYodgijO9lx-Dtard0a54yMrhXyMs" align="center" alt="form image" height="600px" width=100%>

<!-- ![form image](https://img-a.udemycdn.com/redactor/raw/2020-08-25_15-20-27-e452a75ff00354982fbac16869f59e1d.png?cwDNe-jcVTv5Tg_xXma2ei418HTOZbnZM4J1yffrwCkxm7-KBkxkvXCrmisZKE73G2nTxjoRbdMbam-DlCjsrzVhxLtVXt9KSDET9BRlPP98pHvWHLkCvu-3F53Bp51eTZULQpBEW7LnlWXU1looYodgijO9lx-Dtard0a54yMrhXyMs) -->
<br><br>

> 3. Click send and copy the link address of the form and edit the **line 7** which is `GOOGLE_FORM` field

> 4. Go to [this web address on Zillow](https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.96573106092596%2C%22east%22%3A-121.90092693907404%2C%22south%22%3A37.44662455612617%2C%22north%22%3A38.10250370518128%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D) and apply filters as per your requirement, and paste the URL in **line 10** which is `ZILLOW_URL` field


> Run the data_entry_automation.py file 
```
>> python data_entry_automation.py

```
