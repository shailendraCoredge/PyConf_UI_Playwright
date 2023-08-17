Steps:
Add a Local Interpreter

Install below package
> - Pytest
> - pytest-playwright
> - playwright
> - allure-pytest
> - On Command line run 'playwright install'

pytest ./Tests:  will execute all cases

Generating allure-report 
>-  pytest ./Tests --alluredir=./TestReport
>- To see report in HTML form in Webpage :
>- - allure serve ./TestReport
