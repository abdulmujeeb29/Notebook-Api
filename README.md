# Notebook API with Authentication and Permissions
This project is a notebook API built using Django Rest Framework (DRF) that mimics the functionality of a mobile app notebook. It provides a robust platform for users to create, update, and delete their notes securely. The API has been designed with proper implementation to ensure that each user can only access and modify the notes they have created.

Using DRF, the API offers a user-friendly interface for interacting with the notebook resources through standard HTTP methods. By employing token-based authentication, the API verifies the identity of users, preventing unauthorized access to sensitive data. Users obtain a unique token upon successful authentication, which they include in subsequent requests to access their own notes.

Additionally, the API implements fine-grained permissions to enforce access restrictions. With the proper permission classes in place, users are only allowed to view, edit, and delete the notes they have created. This ensures data privacy and maintains the integrity of each user's personal notes.
