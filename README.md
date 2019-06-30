# Pipeline Project

In this project i will work with a suicides dataset from Kaagle. 

I've generated the following files:
>-acquisition.py
>-clean.py
>-importing.py
>-analysis.py
>-presentation.py
>-sending.py

In this project I have **cleaned the dataset**, I have enriched the database **using an api**, from which I have imported additional data about the language and the continent.
>-The api I've used is *"https://restcountries.eu/#api-endpoints-name"*

I've used the library reportlab to generate a PDF with the sublibrary **canvas**.

Additionally, **an email is sent** ***attaching the generated PDF*** to a user entered in the console. Here i've used the library **mime**.