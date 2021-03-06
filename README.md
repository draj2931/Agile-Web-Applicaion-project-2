# Education Camp


Education Camp is an educational web appplication to make online classes easy for students. Its current main features are the following:


    * Courses based on new and upcoming technologies.
    * List of courses available where user will be able to choose the course( Only one course available right now)
    * Proper and thorough understanding of the concepts.
    * Short quizzes to evaluate students' understanding.
    * Feedback option for students to make necessary changes.


*Dashboard: Landing Page of a logged-in user*
![Education Camp dashboard](https://github.com/draj2931/Agile-Web-Applicaion-project-2/blob/master/Dashboard.png)

*Course: Agile Software development*
![Agile Course Sofftware Engineering](https://github.com/draj2931/Agile-Web-Applicaion-project-2/blob/master/Course1.png)

*Course Content*
![Course Content](https://github.com/draj2931/Agile-Web-Applicaion-project-2/blob/master/Agile.png)
<<<<<<< HEAD



# Quick Start Guide


# Running application

Step1: Download the source code file which include Project Folder,README.md,requirements.txt,run.py,test_unittest.py file

Step2: Create a virtual enviroment with the requirement.txt file

step3: The project file will contain static folders with CSS,JS and Images. Template folder will contain all the html files
 the Database will be inside the project folder name agile.db( Where two tables will be preloaded with data) there will be models.py contains all the models and routes.py contain all the route path and an __init__.py file for the project

Step4: Once venv is created the application can be run using python run.py file

step5: The web server 127.0.0.1 will open with port  5000 that can be run in chrome to see the home page


# Running the testfile

step1: Once the required requirement is installed the test file will be visible in test lab
step2: The test file contains 3 test case for 3 diffrent features Login,Register and user navigation
step3:  **** The chromedriver webdriver for google chrome need to be placed in the folder where the testfile is located   ***
step4: The flask webserver should be running while running the testcase




## How to execute a demo

To get Education Camp working in te easiest way, you just have to download the folder above and create a virtual environment using python <code>python3 -m venv venv_name</code>. Now activate the virtual environment using <code>Source venv_name/bin/activate</code>. Set the Flask with start point as run.py and set up the environment.

Run the python file using flask, this will set up a local server at localhost and copy paste the link to a web browser. This will load the landing page of the website.


*Landing Page*
![Landing Page](https://github.com/draj2931/Agile-Web-Applicaion-project-2/blob/master/Landingpage.png)

# Web App Architecture

The login, course details are stored in a database, that is accessed everytime te user tries to access the web resources. The database used here is sqlite. The storage of user and course details can be categorised as the 'Model' of the MVC architecture. 

Once the user logs in, he is directed to the website dashboard where he gets to choose among wide variety of courses. The user selects a course and a short video of the course appears, to give the genral idea on how the course is directed at learning and gives him a brief idea of the technology. The courses are intended for a short and crisp knowledge regarding to a particular technology. The user will be able to save the progress of the course to keep track of the progress completed. At the end of the course, a short quiz is evaluated to know the user knowledege. The quiz is evaluated and user receives the results and also shows the area where the user needs more work on, a small feedback from the user is asked so as to make changes regarding the course material. Appart from the user's view the admin also will be able to log in to the application and view the descripte statisctics and details of assessment This whole flow control and logic mechanism is a small part known as the 'Control' of the whole Web App MVC Architecture. 


The 'View' of the MVC Architecture can be categorised as the User Interface that holds components that ae visible on the screen. Moreover, it provides the visualisation of the data stored in the modek and offers interaction to the user.


*Example of MVC Architecture*
![MVC Architecture](https://github.com/draj2931/Agile-Web-Applicaion-project-2/blob/master/MVC.png)


# Git logs

commit 48ae665711b63ff1250fccf78181027224eac1e9
Author: draj2931 <draj293@gmail.com>
Date:   Mon May 17 15:28:44 2021 +0800

    Testing file update

commit a648ad4e41f2d234b8ab17e5974379091a56e4eb
Author: draj2931 <draj293@gmail.com>
Date:   Mon May 17 13:45:14 2021 +0800

    TESTING CHANGE

commit b09d034289ae6bd1cf04176619f9548808441b4e
Author: draj2931 <draj293@gmail.com>
Date:   Mon May 17 10:18:18 2021 +0800

    Final changes

commit a5efb5d69b7635b9eab7168c227cbf243d181aba
Merge: 56db3bb 4c66984
Author: draj2931 <draj293@gmail.com>
Date:   Mon May 17 06:49:10 2021 +0800

    Merge branch 'master' of https://github.com/draj2931/Agile-Web-Applicaion-project-2

commit 56db3bb615b2e7a17a4163962a537d327e969b4d
Author: draj2931 <draj293@gmail.com>
Date:   Mon May 17 06:48:28 2021 +0800

    result page changes

commit 6e58a20f61311d92b40995395e56139669537f5d
Author: draj2931 <draj293@gmail.com>
Date:   Mon May 17 04:58:44 2021 +0800

    adding testing changes

commit 4c66984612ae5cd8777f51c14d0a6b4c5780855a
Author: Raj Joshi <43139255+rajjoshi96@users.noreply.github.com>
Date:   Sun May 16 17:51:33 2021 +0800

    Update README.md

commit 326aa75ca250355e13f638d1b4895f3549d39eb0
Merge: 406db69 28ab894
Author: rajjoshi96 <rajjoshi1501@gmail.com>
Date:   Sun May 16 17:50:01 2021 +0800

    Readme.md added

commit 406db69c7817800b3256d9872301955de876d421
Author: rajjoshi96 <rajjoshi1501@gmail.com>
Date:   Sun May 16 17:49:08 2021 +0800

    Readme.md added

commit 28ab894d41fd87b49bd06a1693f19e6f6ad191cb
Author: Raj Joshi <43139255+rajjoshi96@users.noreply.github.com>
Date:   Sun May 16 13:38:53 2021 +0800

    Update README.md

commit 4f4c1d78fa71b0a609d9f0c288f4fc429f0af1a8
Merge: f74d0d1 7d1881a
Author: rajjoshi96 <rajjoshi1501@gmail.com>
Date:   Sun May 16 13:35:22 2021 +0800

    Adding images and content

commit f74d0d1b7238c5ba78133169076b20fe1ccb0deb
Author: rajjoshi96 <rajjoshi1501@gmail.com>
Date:   Sun May 16 13:34:34 2021 +0800

    Adding images and content

commit 7d1881a895336bc210014214121860b746abaae0
Author: Raj Joshi <43139255+rajjoshi96@users.noreply.github.com>
Date:   Sun May 16 13:26:16 2021 +0800

    Update README.md

commit ef9fb3ede6e2caae8d2ad455c252c87b73671c5d
Author: Raj Joshi <43139255+rajjoshi96@users.noreply.github.com>
Date:   Sun May 16 13:25:11 2021 +0800

    Update README.md

commit 17d7f6ce1cd1797dd897a4ac46a3b61fa426bcc3
Author: rajjoshi96 <rajjoshi1501@gmail.com>
Date:   Sun May 16 13:19:27 2021 +0800

    Added Readme file

commit 3e24f586a1371a98b8a256cb9af9ec1428dc4ead
Author: Raj Joshi <43139255+rajjoshi96@users.noreply.github.com>
Date:   Sun May 16 12:56:40 2021 +0800

    Create README.md
    
    Added a Readme.md file

commit 108ad45c189d4a2363aee6134c75731f0a0a8c4a
Author: draj2931 <draj293@gmail.com>
Date:   Sun May 16 05:06:31 2021 +0800

    EDITING feedback and quiz page

commit 3cf652f53b80cf9f8b7bf4f5331f8e89b8368c12
Merge: 502dba4 9dd98b2
Author: draj2931 <draj293@gmail.com>
Date:   Sat May 15 19:35:41 2021 +0800

    Merge branch 'master' of https://github.com/draj2931/Agile-Web-Applicaion-project-2

commit 9dd98b2e24e50dce40c254baf81d54fac9710f4f
Author: rajjoshi96 <rajjoshi1501@gmail.com>
Date:   Sat May 15 17:13:31 2021 +0800

    css change - color change on navbar

commit 30ff97f01e8c1cfdecac3041257c3e73a688f06b
Author: rajjoshi96 <rajjoshi1501@gmail.com>
Date:   Sat May 15 16:47:38 2021 +0800

    All course materials added

commit f9465c72cadaccb4667a5b8fdbe5e632540fb2cc
Author: rajjoshi96 <rajjoshi1501@gmail.com>
Date:   Sat May 15 15:54:49 2021 +0800

    Changed The content material and added style to course materials

commit 502dba4550f7da8b2d935769c1690cad8be24ffc
Author: draj2931 <draj293@gmail.com>
Date:   Sat May 15 12:35:55 2021 +0800

    Adding questions

commit 55a61a49b0402e2b9947a0bf727d69bf0850ae8b
Merge: 1740048 429b08d
Author: draj2931 <draj293@gmail.com>
Date:   Fri May 14 23:13:28 2021 +0800

    Merge branch 'master' of https://github.com/draj2931/Agile-Web-Applicaion-project-2

commit 17400486ed14569daf6ac5512dc468794e5f267a
Author: draj2931 <draj293@gmail.com>
Date:   Fri May 14 23:11:21 2021 +0800

    Changes to styles and js

commit 429b08de52a4fdf284d6a0750582433b27e4fb2b
Author: rajjoshi96 <rajjoshi1501@gmail.com>
Date:   Fri May 14 18:42:59 2021 +0800

    removing unnecessary content

commit e9415c3904473f51fd2ff0e4192b54d140254e62
Author: rajjoshi96 <rajjoshi1501@gmail.com>
Date:   Fri May 14 18:41:09 2021 +0800

    removed unnecessary content

commit dd1af469c4175d676895bbd3419ee55c709a2214
Author: rajjoshi96 <rajjoshi1501@gmail.com>
Date:   Fri May 14 18:30:13 2021 +0800

    Changing user front end

commit 61015c6b9850c90792a8e927c3a71d41e7940ea8
Author: rajjoshi96 <rajjoshi1501@gmail.com>
Date:   Thu May 13 19:50:02 2021 +0800

    removed unnecessary styling on register page

commit d82de7b8676805eec3ebf161e6c960c6d4997275
Author: rajjoshi96 <rajjoshi1501@gmail.com>
Date:   Thu May 13 19:43:22 2021 +0800

    minor technical change

commit d9d8c331fcba25652b981942edfb8d156e997034
Merge: d62093d d9a2d48
Author: draj2931 <draj293@gmail.com>
Date:   Thu May 13 19:36:39 2021 +0800

    Merge branch 'master' of https://github.com/draj2931/Agile-Web-Applicaion-project-2

commit d62093d443534a57a001b5cfa7c90ef77716344e
Author: draj2931 <draj293@gmail.com>
Date:   Thu May 13 19:35:08 2021 +0800

    BACKEND FUNCTIONs

commit d9a2d48bcc07b4b983f77e0ad4793d4037027025
Author: draj2931 <draj293@gmail.com>
Date:   Thu May 13 19:34:21 2021 +0800

    Create main.yml

commit ae9433cb5b7eb0f4ea5d41df7cf499031f0b0b91
Author: draj2931 <draj293@gmail.com>
Date:   Thu May 13 02:11:51 2021 +0800

    HTML templates

commit 19b0f2eeda02df48d59f05b6983f3eebf6e549b4
Author: draj2931 <draj293@gmail.com>
Date:   Wed May 12 12:21:17 2021 +0800

    Material changes

commit 591c1406db5a8497f1849da6e8150c48ffb728a4
Author: draj2931 <draj293@gmail.com>
Date:   Wed May 12 09:04:36 2021 +0800

    Changes to content page

commit c0b6594bac2195eabb87d8ed43cfd9f09f8fb715
Author: draj2931 <draj293@gmail.com>
Date:   Tue May 11 11:41:21 2021 +0800

    changes

commit 8e72e86cd654535b031b2f6892938e40f7bd9269
Author: draj2931 <draj293@gmail.com>
Date:   Mon May 10 11:47:45 2021 +0800

    updating

commit e012ec8f29e5b7726e956d2f952a592b6f1c42b8
Author: draj2931 <draj293@gmail.com>
Date:   Mon May 10 11:09:59 2021 +0800

    Adding login/register content

commit 92aee024144a1343a76e084d8ca11f7901ea0ea8
Author: draj2931 <draj293@gmail.com>
Date:   Sun May 9 10:43:24 2021 +0800

    Functions till login and register page

commit 955cb20fafcdccaee2d6f82b26fda2af1a7488ba
Author: draj2931 <draj293@gmail.com>
Date:   Fri May 7 12:09:49 2021 +0800

    general change

commit 86198bdf1d2c4973491d7d66bef1cdebf882b6ef
Author: draj2931 <draj293@gmail.com>
Date:   Fri May 7 11:55:49 2021 +0800

    adding pages

commit 5ba13b16857c0480932c7d79a37eb5abdac243b6
Author: draj2931 <draj293@gmail.com>
Date:   Thu May 6 22:08:29 2021 +0800

commit 94bef49c2562042a4123d2d429292e0711e9911c
Author: draj2931 <draj293@gmail.com>
Date:   Thu May 6 22:02:32 2021 +0800

commit 3008665715547405d9f609b53b8550ac6e6a59aa
Author: draj2931 <draj293@gmail.com>
Date:   Thu May 6 22:01:41 2021 +0800

commit 81b46ea1bdc055ff59d644e700226a0465a64eae
Author: draj2931 <draj293@gmail.com>
Date:   Thu May 6 21:51:56 2021 +0800

    adding db

commit d8b4326a66488b97cd03603883e4708f46b0d1b1
Author: draj2931 <draj293@gmail.com>
Date:   Thu May 6 21:41:25 2021 +0800

    Adding Database

commit b90da563a1cd869ac4e0506a80359c5fc9cf4666
Author: draj2931 <draj293@gmail.com>
Date:   Thu May 6 21:21:33 2021 +0800

    Adding the intial code

commit f2b3c563a5d7717bfa76bb465d47c86a3960fe29
Author: draj2931 <draj293@gmail.com>
Date:   Thu May 6 21:17:15 2021 +0800

    pip

commit 098a010ce1c2441f0a4d3b31d03c5cd7d8c93660
Author: draj2931 <draj293@gmail.com>
Date:   Thu May 6 21:15:47 2021 +0800

    Adding Virtual env

commit 7234d6f2fd1cf34268815b89e217cd007527670e
Author: draj2931 <draj293@gmail.com>
Date:   Thu May 6 21:06:20 2021 +0800

    Project 2 initial setup





