# Final Project

## What I learnt in this course.
Throughout this course, I've gained invaluable knowledge and practical skills that are indispensable for modern software development. Here's a comprehensive overview of what I've learned:

### 1. Docker:
I've mastered the use of Docker, revolutionizing deployment by packaging applications and their environments into containers that can run consistently across various development and production environments.

### 2. Nginx:
I've learned to effectively utilize Nginx for web server configuration and load balancing, ensuring optimal performance and scalability of applications.

### 3. Git:
Deepening my understanding of Git for version control has been essential for managing changes to project codebases, collaborating with team members, and maintaining a robust workflow.

### 4. Python:
I've enhanced my Python skills, focusing on writing clean, well-documented code that adheres to industry standards. Python's versatility has been showcased through its applications in web development and data analysis.

### 5. Testing Using Python:
I've gained proficiency in writing reliable tests using Python frameworks like PyTest, ensuring code works as intended before deployment and improving overall code quality.

### 6. GitHub Actions:
Exploring GitHub Actions has allowed me to automate workflows such as running tests, linting code, and managing deployments directly from GitHub repositories, streamlining the development process and enhancing collaboration.

### 7. Dockerhub:
Utilizing DockerHub for storing and managing Docker images has simplified deployments by enabling easy sharing and version control of images with my team.

### 8. APIs:
Delving into API development has been fundamental for building modern software applications, facilitating seamless communication between different components and services.

### 9. Minio:
Learning to use Minio has provided me with efficient solutions for storing and retrieving large amounts of unstructured data, ensuring reliability and scalability in applications.

### 10. REPL (Read-Eval-Print Loop):
Understanding REPL environments has been a valuable addition to my skill set, providing immediate feedback, facilitating experimentation, enhancing debugging capabilities, and serving as a learning and teaching aid.


#### a. Instant Feedback Loop:
REPL environments like Python's IDLE or interactive shells for languages like Node.js offer immediate feedback on code snippets. This fosters a deeper understanding of functions and operations, enhancing the learning experience.

#### b. Playground for Exploration:
REPL serves as an ideal platform for experimenting with new libraries or language features and testing small code snippets. It allows for quick troubleshooting of specific functionalities before integrating them into larger projects.

#### c. Streamlined Debugging Process:
REPL significantly improves debugging skills by enabling the isolation of problematic code sections and interactive testing of solutions. This reduces the time needed to identify and fix bugs.

#### d. Enhanced Learning and Teaching Tool:
REPL is a valuable learning and teaching tool, reinforcing concepts learned in class by providing real-time practice and immediate feedback. This aids in understanding coding concepts and assisting peers in grasping them effectively.

#### In Summary:
This course has equipped me with a comprehensive toolkit for modern software development, covering essential technologies and methodologies such as Docker, Git, Python, testing, API development, Minio, and REPL. I'm confident that these skills will enable me to contribute effectively to real-world projects and continue my growth as a software developer.

## Challenges Faced During Project Execution

Throughout the development of the project, several challenges arose, each requiring careful analysis and resolution to ensure the smooth progress of the application. Here's an overview of the key challenges encountered and the steps taken to address them:

### 1. Editing production.yml File:
The production.yml file presented issues that were causing GitHub Actions to fail. To rectify this, I made changes to the GitHub username and Docker image name. Additionally, I added environment variables, including GITHUB_USERNAME and GITHUB_TOKEN, which successfully resolved the issues.

### 2. Email Verification Issue:
One of the challenges involved email verification, where the structure was not organized correctly. By rearranging a few lines of code and adding additional test cases, I ensured that the email verification process functioned properly.

### 3. Creation of auth_routes.py:
To maintain a clean and manageable codebase, I created a new file, auth_routes.py. This file handles routes related to authentication, such as login, logout, and password management. By separating authentication routes from user profile routes (handled in user_routes.py), the codebase became more organized and maintainable.

### 4. Duplicate Email and Nickname Issue:
An issue arose with duplicate emails and nicknames, where certain test cases were passing despite the failure related to error code 400. I addressed this by updating routes in user_routes.py and making changes to several files, including user_service.py, common.py, test_users_api.py, and test_user_service.py.

### 5. Issues with Unverified and Locked Users:
There were issues with the verification process for new and locked users. To resolve this, I updated code in user_routes.py and user_service.py. Additionally, I added new test cases in test_users_api.py to ensure the proper functioning of the verification process for new users.

Each of these challenges presented opportunities for learning and growth, and by addressing them effectively, the project moved forward smoothly towards completion.
