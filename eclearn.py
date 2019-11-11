from canvasapi import Canvas
from consolemenu import *
from consolemenu.items import *

with open('api-key') as f:
    API_KEY = f.read()
API_URL = "https://eclearn.emmanuel.edu"

canvas = Canvas(API_URL, API_KEY)

# Intro to Programming Course Fall 2019
COURSE_ID = 2597391


def see_assignment(assignment_id):
    assignment = course.get_assignment(assignment_id)
    submissions = [s for s in assignment.get_submissions()]
    users = [course.get_user(s.user_id) for s in submissions]
    selection = SelectionMenu.get_selection([u.sortable_name for u in users], title=assignment.name)
    download_submission_file(submissions[selection])


def get_submissions(assignment_id):
    return course.get_assignment(assignment_id).get_submissions()


def download_submission_file(submission):
    """
    Once you get the submissions from the assignment, you then need to
    do another call to get_submission(user_id) to get the REAL submission.
    :param submission:
    """
    file_data = submission.attachments[0]
    file_name = file_data['filename']
    file_id = file_data['id']
    file = canvas.get_file(file_id)
    file.download(file_name)       # location can be specified by prefixing to the file name


course = canvas.get_course(COURSE_ID)

# Generate the Main Menu
menu = ConsoleMenu(course.name)
items = [FunctionItem(a.name, see_assignment, [a.id], should_exit=True) for a in course.get_assignments()]
for item in items:
    menu.append_item(item)
menu.show()


