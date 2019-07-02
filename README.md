# Pipeline Project

In this project I will work with a suicides dataset from Kaagle. 

I've generated the following files:
***-acquisition.py***<br>
***-clean.py***<br>
***-importing.py***<br>
***-analysis.py***<br>
***-presentation.py***<br>
***-sending.py***<br>
***-main.py***

In this project I have **cleaned the dataset**, I have enriched the database **using an api**, from which I have imported additional data about the language and the continent of each country.
>-The api I've used is ***"https://restcountries.eu/#api-endpoints-name"***

To generate a PDF I've used the library **reportlab**.

Additionally, **an email is sent** ***attaching the generated PDF*** to a user entered in the console. Here I've used the library **mime**.

Finally, we had to use the **argpars method** to enter the variables from the console. I've defined two arguments to enter from the console:<br>
<p> **-y** to identify the year from which you want to filter the dataset.<br>
<p> **-i** to identify the type of inform you want to send by email.
