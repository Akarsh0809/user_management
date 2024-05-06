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