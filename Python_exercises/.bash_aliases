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
}

startapp() {
	if [ -z "$1" ]; then
        echo "Error: App name argument is missing."
        return 1
    fi
	python3 manage.py startapp "$1"

}