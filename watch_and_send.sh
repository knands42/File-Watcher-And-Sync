# cat ".env.local.$PROFILE" > .env.back
# cat .env | xargs printf -- 'export %s\n'

export PYTHONPATH=$(pwd)
python3 src/main.py