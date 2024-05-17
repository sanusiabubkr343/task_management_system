# Task Management System

## Overview

Welcome to the Task Management System! This system allows you to efficiently manage your tasks with ease. Below are the instructions to get started.

## Getting Started

1. **Create an Account**: 
    - Use the `/auth/users/register` endpoint to create your account. Follow the parameters shown in the images provided.

    ![Register Endpoint](https://github.com/sanusiabubkr343/task_management_system/assets/68224344/6a0db9ac-a518-4e1b-aba2-4df6f1128ba2)

2. **Login**: 
    - Use the email and password you used during registration to login. 
    - Copy the access token from the login response.

    ![Login Endpoint](https://github.com/sanusiabubkr343/task_management_system/assets/68224344/ae8cbec1-a474-4867-9515-782fe84e0ec4)


3. **Authentication**: 
    - Paste the copied access token inside the form as shown in the provided images.
    - You don't need to type the authorization header as it is "Bearer" by default. Just paste the access JWT token gotten when login into the Swagger form and click authorize.
    ![Authentication](https://github.com/sanusiabubkr343/task_management_system/assets/68224344/dfaf01df-9371-4007-9dda-23c87b8917b1)

4. **Creating Tasks**: 
    - Once authenticated, proceed to create,update,list,get and delete tasks as illustrated in the image.
    ![Creating a task](https://github.com/sanusiabubkr343/task_management_system/assets/68224344/f000ed98-e7a7-4aae-854e-dc565e2c79f7)

  
5. **Filtering Tasks**: 
    - To get a list of tasks belonging to a particular user, you can use the query option forms. 
    - The responses are paginated for easier navigation.

6. **Task Status**: 
    - Use the `set-task-complete` endpoint to mark a task as complete.
    ![setting task to completed a task](https://github.com/sanusiabubkr343/task_management_system/assets/68224344/014be15e-8d21-4595-bcde-0e0607c7bd85)

    - Use the `set-task-pending` endpoint to mark a task as pending.

7. **Unit Test**
   ![unit test cases for tasks enpoints](https://github.com/sanusiabubkr343/task_management_system/assets/68224344/4537396a-3c3f-4384-bcd1-158295575995)

## Conclusion

This guide covers the basic operations for interacting with the Task Management System API. For more detailed information, refer to the official API documentation (https://task-management-system-aiq2.onrender.com/api/v1/doc/#/).
