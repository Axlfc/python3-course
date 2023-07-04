alias django-createsuperuser='python3 manage.py createsuperuser'
alias django-remove_stale_contenttypes='python3 manage.py remove_stale_contenttypes'
alias django-check='python3 manage.py check'
alias django-compilemessages='python3 manage.py compilemessages'
alias django-createcachetable='python3 manage.py createcachetable'
alias django-dbshell='python3 manage.py dbshell'
alias django-diffsettings='python3 manage.py diffsettings'
alias django-flush='python3 manage.py flush'
alias django-inspectdb='python3 manage.py inspectdb'
alias django-makemigrations='python3 manage.py makemigrations'
alias django-migrate='python3 manage.py migrate'
alias django-sendtestemail='python3 manage.py sendtestemail'
alias django-shell='python3 manage.py shell'
alias django-showmigrations='python3 manage.py showmigrations'
alias django-sqlflush='python3 manage.py sqlflush'
alias django-clearsessions='python3 manage.py clearsessions'
alias django-collectstatic='python3 manage.py collectstatic'
alias django-runserver='python3 manage.py runserver'


django-startproject() {
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

django-startapp() {
	if [ -z "$1" ]; then
        echo "Error: App name argument is missing."
        return 1
    fi
	python3 manage.py startapp "$1"

}

django-changepassword() {
    if [ -z "$1" ]; then
        echo "Error: User name argument is missing."
        return 1
    fi
    python3 manage.py changepassword "$1"
}

django-dumpdata() {
    if [ -z "$1" ]; then
        echo "Error: App label argument is missing."
        return 1
    fi
    python3 manage.py dumpdata "$1"
}

django-loaddata() {
    if [ -z "$1" ]; then
        echo "Error: Fixture file argument is missing."
        return 1
    fi
    python3 manage.py loaddata "$1"
}

django-makemessages() {
    if [ -z "$1" ]; then
        echo "Error: Language code argument is missing."
        return 1
    fi
    python3 manage.py makemessages -l "$1"
}

django-sqlmigrate() {
    if [ -z "$1" ] || [ -z "$2" ]; then
        echo "Error: App name and migration name arguments are required."
        return 1
    fi
    python3 manage.py sqlmigrate "$1" "$2"
}

django-sqlsequencereset() {
    if [ -z "$1" ]; then
        echo "Error: App name argument is missing."
        return 1
    fi
    python3 manage.py sqlsequencereset "$1"
}

django-squashmigrations() {
    if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
        echo "Error: App name, start migration, and end migration arguments are required."
        return 1
    fi
    python3 manage.py squashmigrations "$1" "$2" "$3"
}

django-test() {
    if [ -z "$1" ]; then
        python3 manage.py test
    else
        python3 manage.py test "$1"
    fi
}

django-testserver() {
    if [ -z "$1" ]; then
        echo "Error: Fixture file argument is missing."
        return 1
    fi
    python3 manage.py testserver "$1"
}

django-findstatic() {
    if [ -z "$1" ]; then
        echo "Error: File name argument is missing."
        return 1
    fi
    python3 manage.py findstatic "$1"
}