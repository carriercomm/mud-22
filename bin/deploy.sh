BASEDIR=$(dirname $0)

if [ -e $BASEDIR/../pid.txt ]; then
  kill -15 $(cat $BASEDIR/../pid.txt) | true
  rm $BASEDIR/../pid.txt
fi

pip install -r $BASEDIR/../requirements.txt

cd $BASEDIR/../
export BUILD_ID=dontKillMe
nohup gunicorn --config app/gunicorn_settings.py app:app > $BASEDIR/../app.log 2>&1&
echo $! > $BASEDIR/../pid.txt
