alias runserver='python3 manage.py runserver'
alias makemigrations='python3 manage.py makemigrations'
alias migrate='python3 manage.py migrate'
alias createsuperuser='python3 manage.py createsuperuser'

startproject() {
    if ! command -v django-admin &> /dev/null; then
        echo "Error: 'django-admin' command not found. Make sure Django is installed:"
        echo "pip3 install django"
        return 1
    fi

    if [ -z "$1" ]; then
        echo "Error: Project name argument is missing."
        return 1
    fi

    project_name="$1"
    target_dir="."

    if [ -n "$2" ]; then
        target_dir="$2"
    fi

    django-admin startproject "$project_name" "$target_dir"
    (
        cd "$project_name"
        if [ ! -f "views.py" ]; then
            echo "#!/usr/bin/env python3
# -*- coding: utf-8 -*-" > "views.py"
        fi

        # Add import views to urls.py
        urls_file="urls.py"
        import_line="from . import views"
        if [ -f "$urls_file" ]; then
            if ! grep -q "$import_line" "$urls_file"; then
                sed -i "1i $import_line" "$urls_file"
            fi
        fi
    )
}

startapp() {
	if [ -z "$1" ]; then
        echo "Error: App name argument is missing."
        return 1
    fi
	python3 manage.py startapp "$1"

}