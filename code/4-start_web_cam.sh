#!/bin/bash

read -p "Enter the number: " number
echo "This is the test number $number"
python web_camera.py $number
exec bash