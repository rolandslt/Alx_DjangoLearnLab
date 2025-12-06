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


# Django Blog – Blog Post Management

## Features
This Django blog allows users to **create, read, update, and delete (CRUD) blog posts** with proper access control.

- **List all posts** – accessible to all users.  
- **View individual post** – accessible to all users.  
- **Create a post** – only authenticated users.  
- **Edit/delete a post** – only the author of the post.

---

## Permissions & Access Control (Step 5)
- `LoginRequiredMixin` ensures only logged-in users can create, edit, or delete posts.  
- `UserPassesTestMixin` ensures only the author of a post can edit or delete it.  
- List and detail views are accessible to everyone.

---

## Testing Guidelines (Step 6)
- Test that **authenticated users** can create new posts.  
- Test that **authors can edit/delete their posts**, and **others cannot**.  
- Verify list and detail pages are accessible to non-logged-in users.  
- Check that **form submissions** work correctly.  
- Ensure all links (list, detail, create, edit, delete) are functional.

---

## Templates
- `post_list.html` – displays all posts with links to details.  
- `post_detail.html` – shows full content of a post with edit/delete links for authors.  
- `post_form.html` – form for creating/editing posts.  
- `post_confirm_delete.html` – confirmation page before deleting a post.

---

## Usage
1. Run migrations:  
```bash
python manage.py makemigrations
python manage.py migrate
