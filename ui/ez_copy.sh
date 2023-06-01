#!/bin/sh
file1="main_window"
file2="new_patient"
file3="progress_window"
file4="first_patient_selection"
file5="add_to_existing_patient"
input_suffix=".ui"
output_suffix=".py"


input_file1=$file1$input_suffix
input_file2=$file2$input_suffix
input_file3=$file3$input_suffix
input_file4=$file4$input_suffix
input_file5=$file5$input_suffix

output_file1=$file1$output_suffix
output_file2=$file2$output_suffix
output_file3=$file3$output_suffix
output_file4=$file4$output_suffix
output_file5=$file5$output_suffix


pyuic5 -x /home/gizem/catkin_ws/src/appirh_project_helse_frde/ui/$input_file1 -o /home/gizem/catkin_ws/src/appirh_project_helse_frde/src/Classes/$output_file1
pyuic5 -x /home/gizem/catkin_ws/src/appirh_project_helse_frde/ui/$input_file2 -o /home/gizem/catkin_ws/src/appirh_project_helse_frde/src/Classes/$output_file2
pyuic5 -x /home/gizem/catkin_ws/src/appirh_project_helse_frde/ui/$input_file3 -o /home/gizem/catkin_ws/src/appirh_project_helse_frde/src/Classes/$output_file3
pyuic5 -x /home/gizem/catkin_ws/src/appirh_project_helse_frde/ui/$input_file4 -o /home/gizem/catkin_ws/src/appirh_project_helse_frde/src/Classes/$output_file4
pyuic5 -x /home/gizem/catkin_ws/src/appirh_project_helse_frde/ui/$input_file5 -o /home/gizem/catkin_ws/src/appirh_project_helse_frde/src/Classes/$output_file5
