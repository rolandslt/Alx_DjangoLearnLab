# Django Permissions and Groups Setup

This Django project demonstrates how to manage permissions and groups to control access to different parts of the application.

## Models

The `Article` model in `bookshelf/models.py` has custom permissions:

- `can_view` — Allows viewing articles
- `can_create` — Allows creating articles
- `can_edit` — Allows editing articles
- `can_delete` — Allows deleting articles

These are defined in the model's `Meta` class.

## Groups

The following groups are created:

- **Viewers**: Can only view articles
- **Editors**: Can view, create, and edit articles
- **Admins**: Can view, create, edit, and delete articles

Permissions are assigned to groups via the Django admin or shell.

## Views

Views are protected using the `@permission_required` decorator:

- `article_list` → requires `can_view`
- `article_create` → requires `can_create`
- `article_edit` → requires `can_edit`
- `article_delete` → requires `can_delete`

Example:

```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def article_edit(request, id):
    ...
