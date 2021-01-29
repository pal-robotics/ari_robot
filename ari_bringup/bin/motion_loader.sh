#!/bin/bash

if [[ -d ~/.pal/motions ]]; then
        echo "Loading motions"
        for motion_file in ~/.pal/motions/*.yaml; do
                echo "Loading file $motion_file"
                rosparam load $motion_file
        done
fi
echo "Done"
