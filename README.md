# cpu_power_reader 
##Task Background
1) Power consumption of a software application is important when made for commercial purposes
2) Products with lower power consumption are viewed more favourably 
3) However, the measurement of power consumption of an application is not straight forward and includes various challenges
 
##Task Description
1) The Intel Power Gadget and similar tools can be used to measure CPU power consumption and GPU power consumption of the computer
2) While this data is useful, it cannot measure the specific power consumption of an application - the data comprises of the energy consumed by all applications (including background applications)
3) Using your preferred language/framework/library, code up a mini-program that can measure the specific power consumption of a single application on the computer. 
## thought process
1. get the cpu power using the intel powerLog3 application <br>
2. get the total cpu usage of the system <br>
3. get all the running application with their coresponding cpu percentage <br>
4. claculate the power comsumption rate of each process and using the total cpu percentage and the total power comsuption of the system. <br>
###formula 
	```running_application_power = (total_cpu_percent *0.01) * total_cpu_power * (running_application_cpu_percent *0.01)``` <br>
**Note that the above formula is an approximation to the true value of the system power consumption as their several factors this value as highlighted in (this article)[h] and secondly the PowerLog3 application does not estimate the right power value for a linus 
environment of which the application is install but runs perfectly well on a window application <br>**
*solution: the second version of the application will perfectly this bug*
4. host the frontend interface on vercel using nextjs and accesable [here](https://cpu-reader-frontend.vercel.app/) <br>
5. the backend API docs is hosted on aws accesable from this link [here](http://54.167.64.55/docs) <br>
 

### Features to be added
1. integrate a better way of calculate power on a linus machine
2. added other features like pagenation 
3. add a graphical interface for each process power consumption
4. add a more detail over view of each application such as user cpu time, system cpu time
5. add an ability to kill a running application when it power reaches certain threshold