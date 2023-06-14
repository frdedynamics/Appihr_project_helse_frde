#!/bin/bash
# Input Files Array
input_files=("main_window.ui" "new_patient.ui" "threshold_selection_window.ui" "first_patient_selection.ui" "add_to_existing_patient.ui" "real_time_measurement.ui")

# Paths
ui_dir="/home/gizem/catkin_ws/src/appirh_project_helse_frde/ui/"
output_dir="/home/gizem/catkin_ws/src/appirh_project_helse_frde/src/Classes/"

# Output Files Array (derived from Input Files)
output_files=()

# Loop through the input files array and generate the corresponding output files
for input_file in "${input_files[@]}"
do
    # Derive the output file name from the input file name
    output_file="${input_file%.ui}.py"
    output_files+=("$output_file")

    pyuic5 -x "$ui_dir$input_file" -o "$output_dir$output_file"
done
