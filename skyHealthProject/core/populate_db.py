#The code below was done by Iqra Shah (w1973224)
from core.models import User, Department, Team, SessionAssignment, Session, Vote, Card

# ------ Users ------ #
users = [
    # Engineers
    ("jsmith", "John", "Smith", "jsmith@sky.com", "Pword123!", "engineer"),
    ("engineer1", "Emma", "Watson", "emma1@sky.com", "Pword123!", "engineer"),
    ("engineer2", "Liam", "Jones", "liam1@sky.com", "Pword123!", "engineer"),
    ("engineer3", "Noah", "Taylor", "noah1@sky.com", "Pword123!", "engineer"),
    ("engineer4", "Olivia", "Brown", "olivia1@sky.com", "Pword123!", "engineer"),
    ("engineer5", "Sophia", "Davis", "sophia1@sky.com", "Pword123!", "engineer"),
    # Team Leaders
    ("akhan", "Aisha", "Khan", "akhan@sky.com", "Pword456!", "teamLead"),
    ("ptart", "Peter", "Tart", "ptart@sky.com", "Pword655!", "teamLead"),
    ("jthomas", "Jones", "Thomas", "jthomas@sky.com", "Pword987!", "teamLead"),
    ("rpatel", "Rishi", "Patel", "rpatel@sky.com", "Pword432!", "teamLead"),
    ("lroberts", "Lewis", "Roberts", "lroberts@sky.com", "Pword111!", "teamLead"),
    # Department Leads
    ("fsheikh", "Fuad", "Sheikh", "fsheikh@sky.com", "Pword789!", "departmentLead"),
    ("dnguyen", "Don", "Nguyen", "dnguyen@sky.com", "Pword777!", "departmentLead"),
    # Senior Manager
    ("msingh", "Mandeep", "Singh", "msingh@sky.com", "Pword000!", "seniorManager"),
]

for u in users:
    User.objects.get_or_create(username=u[0], firstName=u[1], lastName=u[2], email=u[3], password=u[4], role=u[5])

# ------ Departments ------ #
departments = [
    ("networkEngineering", "msingh", "fsheikh"),
    ("fieldEngineering", "msingh", "dnguyen"),
]

for d in departments:
    Department.objects.get_or_create(deptName=d[0], seniorManager=User.objects.get(username=d[1]), deptLeader=User.objects.get(username=d[2]))

# ------ Teams ------ #
teams = [
    # Network Engineering Department
    ("fibrePlanningTeam", "networkEngineering", "akhan"),
    ("networkSupportTeam", "networkEngineering", "ptart"),
    ("wirelessSolutionsTeam", "networkEngineering", "rpatel"),
    
    # Field Engineering Department
    ("homeInstallationTeam", "fieldEngineering", "jthomas"),
    ("fieldSupportTeam", "fieldEngineering", "lroberts"),
    ("remoteMonitoringTeam", "fieldEngineering", "fsheikh"),
]

for t in teams:
    Team.objects.get_or_create(teamName=t[0], deptName=Department.objects.get(deptName=t[1]), teamLeader=User.objects.get(username=t[2]))

# ------ Sessions ------ #
sessions = [
    ("S2025Q1", "2025", "Q1"),
    ("S2025Q2", "2025", "Q2"),
]

for s in sessions:
    Session.objects.get_or_create(sessionId=s[0], sessionYear=s[1], sessionQuarter=s[2])

# ------ Session Assignment ------ #
assignments = [
    ("A1", "jsmith", "S2025Q1", "There has been a noticeable improvement in receiving support since the last time I took the quiz."),
    ("A2", "jsmith", "S2025Q2", "I don’t feel like the work I’m currently doing is delivering value."),
]

for a in assignments:
    SessionAssignment.objects.get_or_create(assignId=a[0], username=User.objects.get(username=a[1]), sessionId=Session.objects.get(sessionId=a[2]), additionalComments=a[3])

# ------ Cards ------ #
cards = [
    ("C1", "Support", "Do you feel that you receive support when needed and know exactly who to approach for help?"),
    ("C2", "Teamwork", "Do you feel like your team works together smoothly, with good communication, towards a common goal?"),
    ("C3", "Mission", "Do you understand and believe in your squad's purpose?"),
    ("C4", "Delivering Value", "Think about the quality of your output and how stakeholders react to it. Is the team delivering meaningful value that you're excited about? Or is it frustrating, rushed, or poorly received?"),
    ("C5", "Easy to Release", "How smooth is your release process?"),
    ("C6", "Fun", "How enjoyable is it to work in your squad?"),
    ("C7", "Health of Codebase", "Is the code clean, testable, and a pleasure to work with? Or is it full of quick fixes, bugs, and technical debt that slows everyone down?"),
    ("C8", "Speed", "Do you have momentum and flow, or are you constantly blocked by issues and waiting on others?"),
    ("C9", "Pawns or Players", "Do you feel empowered to shape decisions, propose ideas, and own the work? Or do you just follow orders without any say in the process?"),
    ("C10", "Learning", "Are you growing and learning new things?"),
    ("C11", "Suitable Process", "Do you feel like the current way of working suits your needs and allows you to be productive without unnecessary obstacles?"),
]

for c in cards:
    Card.objects.get_or_create(cardId=c[0], cardName=c[1], cardDesc=c[2])