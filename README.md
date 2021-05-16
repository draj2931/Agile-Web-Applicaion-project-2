# Education Camp


Education Camp is an educational web appplication to make online classes easy for students. Its current main features are the following:



    * Courses based on new and upcoming technologies.
    * Proper and thorough understanding of the concepts.
    * Short quizzes to evaluate students' understanding.
    * Feedback option for students to make necessary changes.



*Dashboard: Landing Page of a logged-in user*
![Education Camp dashboard](https://github.com/draj2931/Agile-Web-Applicaion-project-2/blob/master/Dashboard.png)

*Course: Agile Software development*
![Agile Course Sofftware Engineering](https://github.com/draj2931/Agile-Web-Applicaion-project-2/blob/master/Course1.png)

*Course Content*
![Course Content](https://github.com/draj2931/Agile-Web-Applicaion-project-2/blob/master/Agile.png)



# Quick Start Guide


## How to execute a demo

To get Education Camp working in te easiest way, you just have to download the folder above and create a virtual environment using python <code>python3 -m venv venv_name</code>. Now activate the virtual environment using <code>Source venv_name/bin/activate</code>. Set the Flask with start point as run.py and set up the environment.

Run the python file using flask, this will set up a local server at localhost and copy paste the link to a web browser. This will load the landing page of the website.

*Landing Page*
![Landing Page](https://github.com/draj2931/Agile-Web-Applicaion-project-2/blob/master/Landingpage.png)

# Web App Architecture

The login, course details are stored in a database, that is accessed everytime te user tries to access the web resources. The database used here is sqlite. The storage of user and course details can be categorised as the 'Model' of the MVC architecture. 

Once the user logs in, he is directed to the website dashboard where he gets to choose among wide variety of courses. The user selects a course and a short video of the course appears, to give the genral idea on how the course is directed at learning and gives him a brief idea of the technology. The courses are intended for a short and crisp knowledge regarding to a particular technology. At the end of the course, a short quiz is evaluated to know the user knowledege. The quiz is evaluated and user receives the results and also shows the area where the user needs more work on, a small feedback from the user is asked so as to make changes regarding the course material. This whole flow control and logic mechanism is a small part known as the 'Control' of the whole Web App MVC Architecture. 


The 'View' of the MVC Architecture can be categorised as the User Interface that holds components that ae visible on the screen. Moreover, it provides the visualisation of the data stored in the modek and offers interaction to the user.


*Example of MVC Architecture*
![MVC Architecture](https://github.com/draj2931/Agile-Web-Applicaion-project-2/blob/master/MVC.png)



