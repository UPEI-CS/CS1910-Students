In each HWX folder are 3 subfolders:

- student
  - the student version
  - exists in the public git
  - shared with the students
- autograder
  - the otter grade copy along with a grading script
  - download the student submissions and put them into this folder and run the script to grade the submissions
    - script: `grade_wp.py`
    - add the path to the autograder .zip and the folder containing the student submissions, redirect output to a .csv file
- main template
  - the otter grade template used to produce the student version and autograding
  - this contains the solutions, etc
  - otter assign is used to turn the template into the student and autograder versions


otter documentation:
https://otter-grader.readthedocs.io/en/latest/index.html
