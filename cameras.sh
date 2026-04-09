
ustreamer --device=/dev/video0 --host=192.168.1.68 --format=MJPEG --port=8080 --device-timeout 2 -r 800x600 -b 2 --workers 2 --encoder=HW -n & sleep 2 &
ustreamer --device=/dev/video2 --host=192.168.1.68 --format=MJPEG --port=8081 --device-timeout 2 -r 800x600 -b 2 --workers 2 --encoder=HW -n & sleep 2 &
ustreamer --device=/dev/video4 --host=192.168.1.68 --format=MJPEG --port=8082 --device-timeout 2 -r 800x600 -b 2 --workers 2 --encoder=HW -n & sleep 2 &
ustreamer --device=/dev/video6 --host=192.168.1.68 --format=MJPEG --port=8083 --device-timeout 2 -r 800x600 -b 2 --workers 2 --encoder=HW -n & sleep 2 &