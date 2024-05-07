# Final Project

## 6 issues resolved.

### 1. Editing produciton.yml file.
Production.yml file had issues that were causing the github actions to fail. I changed github username an d docker image name. I added GITHUB_USERNAME and GITHUB_TOKEN that helped in resolving the issues successfully.

link : [https://github.com/Kiran-Ramisetti-kr483/user_management/pull/2/files](https://)

### 2. Emain verification issue
The user verification structure was not in order. So, I had to change order of few lines of code and added few test cases to check if the emain verification was working well or not.

link : [https://github.com/Kiran-Ramisetti-kr483/user_management/pull/5/files](https://)

### 3. Creating the auth_routhes.py
created a new file auth_routes.py to keep codebase clean and maintainable. In user_routes.py we handle routes related to user profile management like creating, updating, retrieving and deletign user profiles. In auth_routes.py we handle routes related to authenticationa such as login, logout and password management.

link : [https://github.com/Kiran-Ramisetti-kr483/user_management/pull/7/files](https://)

### 4. duplicate email amd nickname issue.
In this issue I notices that few test cases were passing even when the test case was failing related to error code 400 and saw few issues with dupicate emains and nickname. I had to update new routes in user_routes.py and change few lines of code in user_service.py, common.py, test_users_api.py and test_user_service.py.

link : [https://github.com/Kiran-Ramisetti-kr483/user_management/pull/9/files](https://)

### 5. Issue with unverified users and locked users.
There were few issues with verification process for a new user and locked  user. I updated code in user_routes.py and user_service.py. I added new test cases in test_users_api.py to ensure that the verification process for new user is working properly.

link : [https://github.com/Kiran-Ramisetti-kr483/user_management/pull/11/files](https://)

### 6. Password validation.
I updated the code in user_schemas.py to strictly validate the password and added few lines of code in user_routes.py. I even added few test cases to in test_user_api.py and test_user_schemas.py to verify validation of password.

link : [https://github.com/Kiran-Ramisetti-kr483/user_management/pull/16/files](https://)

## New Feature - upload pictures using minio.
To be able to upload and update profile picture to personalize the suer account. For this I implemented an API endpoint for users to upload their profile picture, store the uploaded profile pictures securly in Minio, updating the user profile API endpoints to include the profile picture URL and retriving the profile picture URL from Minio when displaying user profiles.

link : [https://github.com/Kiran-Ramisetti-kr483/user_management/pull/20/files](https://)

