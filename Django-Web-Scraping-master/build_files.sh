# build_files.sh
pip install virtualenv
virtualenv newenv
source newenv/bin/activate
python3.9 -m pip install -r requirement.txt
python3.9 manage.py collectstatic  --noinput --clear