ps -ux | grep -E 'my_app|supervisord' | awk '{print $2}' | xargs kill -9

cd temp/log
rm *
cd ../run
rm *
cd ../..