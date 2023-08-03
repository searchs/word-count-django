#  Simple Word count App in Django

Using Django to create web apps quickly.

## Setup

*__Create and activate Python environment__*

```bash
conda create -n djgenv  python=3.10 -y

conda activate djgenv
```

*__Install Django in activated environment__

```bash
pip install DJango==4.2.4

# Create wordcount project
django-admin startproject wordcount

# Change into project directory and initialize git
cd  wordcount
git init

# Before making any commit create a .gitignore file
touch .gitignore

# Run the project to check status
python manage.py runserver


```
