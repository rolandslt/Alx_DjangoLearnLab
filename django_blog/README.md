# Django Blog - User Authentication System

## Objective
Develop a comprehensive user authentication system for the Django blog project.  
This system enables user registration, login, logout, and profile management, providing a personalized user experience.

---

## Features
- **User Registration:** New users can sign up with username, email, and password.  
- **Login/Logout:** Users can log in and out using Django’s built-in authentication views.  
- **Profile Management:** Authenticated users can view and edit their profile (username and email).  
- **Secure Handling:** Passwords are hashed, and CSRF protection is enabled on all forms.  

---

## File Structure & Code

### Forms
- `blog/forms.py`  
  - `CustomUserCreationForm`: Extends Django’s `UserCreationForm` to include email.  
  - `UserProfileForm`: Allows editing username and email in profile.

### Views
- `blog/views.py`  
  - `register_view`: Handles registration and auto-login.  
  - `profile_view`: Allows authenticated users to view/edit profile.

### URLs
- `blog/urls.py`
  - `/register/` → registration page  
  - `/login/` → login page  
  - `/logout/` → logout page  
  - `/profile/` → profile management page

### Templates
- `templates/blog/register.html` → user registration  
- `templates/blog/profile.html` → profile view/edit  
- `templates/registration/login.html` → login  
- `templates/registration/logged_out.html` → logout confirmation  
- `templates/base.html` → base template for all pages

---

## Setup Instructions

1. **Install dependencies** (if not already):
   ```bash
   pip install Django
