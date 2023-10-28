# assignHub&#46;io

**Table of Contents:**
1. About assignhub.io
1. Login page
1. Manager dashboard page
    1. Top bar section
    1. Schedule calendar section
    1. Task assign section
1. How the algorithm works

#### About assignhub&#46;io
---
```
This website is used to assign tasks efficiently to employees by their managers.

It uses many criteria to determine which employee should the task be assigned to based on:
1. Whether they are available within the near future before the deadline
2. Their current workload and
3. Their domain of work
```

#### Log in Page
---
Managers can login to their respective account. As this is a prototype only one manager exists, and username and password are pre-filled.

#### Manager Dashboard
---
*It contains 3 sections*<br><br>
**Top bar section:**<br>
Here you can go back to the home page, visit the about page, the contact page, manager profile settings page and logout from account.<br><br>

**Schedule calendar section:**<br>
Here you have employee names their respective domain of work and their task schedule for the next week.<br>
*If an employee has a task on some day, it is provided under that day for that employee.<br>
"--" means they are free that day.*<br>
You can only see schedules for next 7 days from today.<br><br>

**Task assign section:**
Here you can assign tasks.<br>
Details provided by the manager for assigning a task:<br>
1. Name of the task
1. Domain required for that task
1. Deadline for the task
1. Details on the task

#### How the algorithm works?
As mentioned above, it uses factors such as availability, workload and domain to find the right employee for that task. Therefore, it maintains an even workload for all employees.<br><br>

Algorithm:
```
1. Find all employees who works in the same task domain
2. Arrange them by their workload in the acsending order
3. For each day starting from today till the task deadline,
4.     If any employee among them is free on that day,
5.         Assign the task to that employee
6. Report to manager, if any employee is found or not.
```

**Made by: Jeev Jacob George, Jacob B Stephen, Rosh Cherian, G Venkateswar**
