# Pipeline Project

In this project I will work with a suicides dataset from Kaagle. 

I've generated the following files:
>-acquisition.py<br>
>-clean.py<br>
>-importing.py<br>
>-analysis.py<br>
>-presentation.py<br>
>-sending.py

In this project I have **cleaned the dataset**, I have enriched the database **using an api**, from which I have imported additional data about the language and the continent.
>-The api I've used is *"https://restcountries.eu/#api-endpoints-name"*

I've used the library reportlab to generate a PDF with the sublibrary **canvas**.

Additionally, **an email is sent** ***attaching the generated PDF*** to a user entered in the console. Here I've used the library **mime**.