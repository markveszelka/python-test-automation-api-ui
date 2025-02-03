<!-- PROJECT SHIELDS -->

<!-- PROJECT LOGO -->
<br />
<div style="text-align: center;">
  <a href="https://github.com/markveszelka/python-test-automation-api-ui">
  </a>

<h1 style="text-align: center;">API + UI Test Automation Framework</h1>

## About The Project

Test Automation Framework, written in Python using Pytest, Behave and Selenium.
Contains API and UI test cases.
BDD approach is used to write UI tests, with Gherkin syntax.

## Built With

[![Python][Python]][Python-url]
[![PyTest][PyTest]][PyTest-url]
[![Selenium][Selenium]][Selenium-url]
[![Behave][Behave]][Behave-url]
[![Allure][Allure]][Allure-url]
[![Docker][Docker]][Docker-url]
[![Makefile][Makefile]][Makefile-url]

## Allure Reports

[![Allure][Allure]][Allure-Report-url]

Allure is a lightweight, multi-language tool that provides concise,
web-based test reports to help teams gain insights from test results.
Click the badge to view an Allure report of a build from 1/14/2025.
It contains 12 test cases, of which 11 passed and 1 failed.
Test failure screenshot also included.

</div>

### Run the API tests locally with Python:

#### 1. Git clone the repository:

```sh
   git clone https://github.com/markveszelka/python-test-automation-api-ui.git
```

#### 2. Make sure that Python 3 is installed on the system.

#### 3. Create isolated virtual environment:

```sh
   python3 -m venv venv
   ```

#### 4. Make sure that the Fund Transfer API is running locally on the system.

#### 5. Run the project in Python VENV using Makefile command:

```sh
   make run-api-tests
```

### Run the UI tests locally with Python:

#### 1. Git clone the repository:

```sh
   git clone https://github.com/markveszelka/python-test-automation-api-ui.git
```

#### 2. Make sure that Python 3 is installed on the system.

#### 3. Create isolated virtual environment:

```sh
   python3 -m venv venv
   ```

#### 4. Run the project in Python VENV using Makefile command:

```sh
   make run-local-all
```

### Run the UI tests locally with Docker:

#### 1. Git clone the repository:

```sh
   git clone https://github.com/markveszelka/python-test-automation-api-ui.git
```

#### 2. Make sure that Docker is installed on the system.

#### 3. Run the project in Docker container using Makefile command:

Be sure that in 'environment.py' file headless mode is set to True, then run.

```python
context.driver = ChromeDriver(headless=True).get_driver()
```

```sh
   make run-docker-all
```

<!-- CONTACT -->
<div style="text-align: center;">

## Contact

Mark Veszelka - [github](https://github.com/markveszelka) - [linkedin](https://www.linkedin.com/in/mark-veszelka/) -
mark.veszelka@gmail.com

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- STACKS -->
</div>

[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54

[Python-url]: https://www.python.org/

[PyTest]: https://img.shields.io/badge/pytest-red?style=for-the-badge&logo=python&logoColor=ffdd32

[PyTest-url]: https://docs.pytest.org/en/stable/

[Selenium]: https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white

[Selenium-url]: https://www.selenium.dev

[Behave]: https://img.shields.io/badge/Behave-802045?style=for-the-badge&logo=python&logoColor=white

[Behave-url]: https://behave.readthedocs.io/en/latest/

[Allure]: https://img.shields.io/badge/Allure-ff5000?style=for-the-badge&logo=allure&logoColor=white

[Allure-url]: https://allurereport.org/

[Allure-Report-url]: https://output.circle-artifacts.com/output/job/1bed4c4a-a075-4ead-8d5d-e0da5fe08d3e/artifacts/0/allure-report/index.html

[Docker]: https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white&labelColor=1D63ED&color=1D63ED

[Docker-url]: https://www.docker.com/

[Makefile]: https://img.shields.io/badge/Makefile-ff5000?style=for-the-badge&logo=make&logoColor=white

[Makefile-url]: https://www.gnu.org/software/make/manual/make.html

```

```



