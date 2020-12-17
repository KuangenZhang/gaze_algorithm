#!/bin/bash

read -p "Enter the number: " number
echo "This is the test number $number"
python2 data_record.py $number
exec bash