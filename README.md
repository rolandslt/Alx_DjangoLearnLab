###Social Media API

A robust backend API for a Social Media platform built with Django and Django REST Framework (DRF). This project includes custom user authentication, content management (posts and comments), and built-in security permissions.

🛠 Features
1. User Authentication (accounts app)

Custom User Model: Extended from AbstractUser with added fields for bio, profile_picture, and a self-referencing followers Many-to-Many field.

Token-Based Auth: Uses DRF's TokenAuthentication. Users receive a unique token upon registration or login to authenticate subsequent requests.

2. Posts & Comments (posts app)
CRUD Operations: Full Create, Read, Update, and Delete capabilities for posts and comments.

Smart Filtering: Search through posts using ?search=keyword on the title or content.

Pagination: Global pagination is enabled to manage large datasets efficiently.

📖 API Documentation
Authentication Endpoints

    Endpoint,            Method,          Description
/accounts/register/,      POST        Register a new user. Returns user details and Token.
/accounts/login/,         POST,       Exchange username/password for an Auth Token.

Post Endpoints

Endpoint        Method    Auth Required      Description
/posts/         GET        No            List all posts (paginated). Filter with ?search=.
/posts/         POST       Yes           Create a new post.
/posts/{id}/    GET        No            Retrieve a specific post and its comments.
/posts/{id}/    PUT        Author Only   Update a post.
/posts/{id}/    DELETE     Author Only   Delete a post.

Comment Endpoints

Endpoint         Method      Auth Required      Description
/comments/        GET           No            List all comments.
/comments/        POST          Yes           Add a comment to a specific post.
/comments/{id}/   PATCH         Author Only   Partially update a comment.


User Connections & Feed

Endpoint                           Method  Auth,      Description
/api/accounts/follow/{user_id}/     POST   Token       Follow a user by their ID.
/api/accounts/unfollow/{user_id}/   POST   Token       Unfollow a user by their ID.
/api/posts/feed/                    GET    Token       View posts from users you follow (Recent first).