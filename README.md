
STEPS
-------------
-------------

##The Project
The "escalators" at Stuy are pretty atrocious. In fact, they should probably be renamed "occasionally moving stairs." When they are on, it's nice to know. That's where we come in.  

We (hope) to install a tiny device next to each escalator bank to detect movement. That device will communicate with a computer, which will ping to a webservice built to show and log the current status of the escalators in stuy.  

We're starting with just one escalator, but if we're successful, we can implement it on more.


##Team
| ![](https://avatars2.githubusercontent.com/u/5422397?&s=150) | ![](https://avatars0.githubusercontent.com/u/5421231?&s=150) | ![](https://avatars2.githubusercontent.com/u/1449704?3&s=150) |     ![](http://i.imgur.com/rBULNDu.png)    |
|:----------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------:|:---------------------------------------------------------------:|:------------------------------------------:|
|                                [Andrew Fischer](https://github.com/afischer)                               |        [Aaron Mortenson](https://github.com/trunkatedpig)       |     [Philipp Steinmann](https://github.com/PhilippSteinmann)    | [Daniel Zabari](https://github.com/Zabari) |
| Front-End Design, Hardware Programming & Design                                                         | Front-End Programming, Javascripting                         | Back-End Design                                               | *Group Organizer,* Database Programming |


##Video
[![YouTube Video](http://img.youtube.com/vi/xoU7kB2jkI8/0.jpg)](https://www.youtube.com/watch?v=apEwjlbcmhs)

##Instalation

####Requirements
- Python with modules `Flask`, `Flask-RESTFul`
- A RaspberryPi (or clone)
- An Arduino (or clone)

####Instalation
1. Download and unpack files by either downloading zip or cloning using `git clone https://github.com/Zabari/STEPS.git`
2. Insure you have the latest version of python installed
3. Use pip to install `Flask`, `Flask-restful`
4. Run server.py to create an instance of the database
5. Run `python __init__.py` to run an instance of the website. You may need to change the location of the server in both `server.py` and `__init__.py`.
6. If you want to have arduino and raspi modules to track, you will have to build those. More information on that later.
7. To see the full site in action, check out [stuysteps.nyc](http://www.stuysteps.nyc)

##Timeline
*See [TODO.md](https://github.com/Zabari/EscalatorHaus/blob/master/TODO.md).*

