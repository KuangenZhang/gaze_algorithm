#!/bin/bash

read -p "Enter the number: " number
echo "This is the test number $number"
python tobii_gaze.py $number
exec bash