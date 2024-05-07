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

##### LINK: [https://github.com/Akarsh0809/user_management/pull/10](https://)

### 2. Email Verification Issue:
One of the challenges involved email verification, where the structure was not organized correctly. By rearranging a few lines of code and adding additional test cases, I ensured that the email verification process functioned properly.

##### LINK: [https://github.com/Akarsh0809/user_management/pull/8](https://)

### 3. Creation of auth_routes.py:
To maintain a clean and manageable codebase, I created a new file, auth_routes.py. This file handles routes related to authentication, such as login, logout, and password management. By separating authentication routes from user profile routes (handled in user_routes.py), the codebase became more organized and maintainable.

##### LINK: [https://github.com/Akarsh0809/user_management/pull/16](https://)

### 4. Eradicating Null Values for LinkedIn and GitHub URLs

In this update, I focused on rectifying the issue of returning null values for LinkedIn and GitHub URLs. I made necessary changes in user_routes.py to address the errors causing the null values. Additionally, I updated production.yml to ensure the smooth deployment of the application.

By diligently reviewing and updating the code, I successfully eradicated the errors, ensuring that LinkedIn and GitHub URLs are retrieved and displayed accurately within the application. This enhancement enhances user experience and data integrity.

##### LINK: [https://github.com/Akarsh0809/user_management/pull/12](https://)

### 5. Inclusion of Minio Integration

Under this heading, I made crucial updates to the codebase to incorporate Minio integration into our application. Specifically, I made modifications to user_routes.py and user_services.py by adding necessary lines of code to enable Minio functionality. Additionally, I updated config.py to accommodate the changes.

These updates empower our application to utilize Minio for efficient handling of storage and retrieval of large volumes of unstructured data. By seamlessly integrating Minio, we enhance our application's scalability and reliability, providing users with a more robust storage solution.

##### LINK: [https://github.com/Akarsh0809/user_management/pull/6](https://)

### 6. Password validation.
I changed the code in user_schemas.py to tightly check passwords and added a few lines of code to user_routes.py. I even included a few test cases in test_user_api.py and test_user_schemas.py to validate passwords.

##### LINK: [https://github.com/Akarsh0809/user_management/pull/5](https://)

Each of these challenges presented opportunities for learning and growth, and by addressing them effectively, the project moved forward smoothly towards completion.

## New Feature: Profile Picture Upload with Minio Integration

In this update, a new feature has been introduced to allow users to personalize their accounts by uploading and updating their profile pictures. To achieve this, an API endpoint has been implemented to facilitate the upload of profile pictures. These pictures are securely stored in Minio, ensuring data integrity and privacy.

### Key enhancements include:

API Endpoint for Profile Picture Upload:
Implemented an API endpoint that enables users to upload their profile pictures.
Minio Integration for Secure Storage:
Integrated Minio for secure storage of uploaded profile pictures. This ensures that user data remains protected and accessible only to authorized users.
Update User Profile API Endpoints:
Updated the user profile API endpoints to include the profile picture URL. This enables users to retrieve and update their profile pictures seamlessly.
Retrieving Profile Picture URL from Minio:
Implemented functionality to retrieve the profile picture URL from Minio when displaying user profiles. This ensures that users' profile pictures are displayed accurately and securely.
This new feature enhances user experience by allowing users to personalize their accounts with profile pictures while ensuring data security through Minio integration.

##### LINK: [https://github.com/Akarsh0809/user_management/pull/15](https://)

## Test Cases: Expanding Coverage
In total, 16 test cases have been added to address various issues and verify their resolution. These test cases are designed to ensure the robustness and reliability of the application. Details of these new test cases can be found in the links provided in the "Problems Faced While Doing This Project" section.

The new test cases cover a range of scenarios, including:

1)Password strength validation.

2)Email address verification.

3)Eradicating Null Values for LinkedIn and GitHub URLs

4)User authentication and authorization verification.

5)Inclusion of Minio Integration

By incorporating these additional test cases, we aim to comprehensively validate the functionality of our application, ensuring it meets the highest standards of quality and reliability.

## DockerHub Repository and Image:

My project is successfully running, and its Docker image is stored in DockerHub for easy access and deployment. Below are the details of my DockerHub repository:

##### Repository Link: [https://hub.docker.com/repositories/ak2856](https://)

Image: ![WSD_FINAL](https://github.com/Akarsh0809/user_management/assets/157727440/0dda63ab-803e-42d0-a350-49d58fd36ed7)


By hosting my Docker image on DockerHub, I ensure seamless deployment and distribution of our application. This allows users and collaborators to access the latest version of our application image with ease.

These skills set me up to handle complex software projects with ease, contribute effectively to top-notch teams, and keep up with the latest in tech. They make me a great fit for various roles in the tech industry, whether it's coding, systems engineering, or something else. Plus, they show that I'm always ready to learn and grow—essential traits for moving up in the tech world!



