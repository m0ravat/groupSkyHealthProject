from django.contrib.auth.models import User, Group
from core.models import Department, Team
from quiz.models import SessionAssignment, Session, Vote, Card

# ------ Users ------ #
users = [
    # Engineers
    ("jsmith", "John", "Smith", "jsmith@sky.com", "Pword123!", "engineer"),#
    ("ewatson", "Emma", "Watson", "emma1@sky.com", "Pword123!", "engineer"),#
    ("ljones", "Liam", "Jones", "liam1@sky.com", "Pword123!", "engineer"),#
    ("ntaylor", "Noah", "Taylor", "noah1@sky.com", "Pword123!", "engineer"),#
    ("obrown", "Olivia", "Brown", "olivia1@sky.com", "Pword123!", "engineer"),#
    ("sdavis", "Sophia", "Davis", "sophia1@sky.com", "Pword123!", "engineer"),#
    # Team Leaders
    ("akhan", "Aisha", "Khan", "akhan@sky.com", "Pword456!", "teamLead"),#
    ("ptart", "Peter", "Tart", "ptart@sky.com", "Pword655!", "teamLead"),#
    ("jthomas", "Jones", "Thomas", "jthomas@sky.com", "Pword987!", "teamLead"),#
    ("rpatel", "Rishi", "Patel", "rpatel@sky.com", "Pword432!", "teamLead"),#
    ("lroberts", "Lewis", "Roberts", "lroberts@sky.com", "Pword111!", "teamLead"),#
    # Department Leads
    ("fsheikh", "Fuad", "Sheikh", "fsheikh@sky.com", "Pword789!", "departmentLead"),#
    ("dnguyen", "Don", "Nguyen", "dnguyen@sky.com", "Pword777!", "departmentLead"),#
    # Senior Manager
    ("msingh", "Mandeep", "Singh", "msingh@sky.com", "Pword000!", "seniorManager"),#
]

# Create users first
for u in users:
    user, created = User.objects.get_or_create(username=u[0], first_name=u[1], last_name=u[2], email=u[3])
    if created:
        user.set_password(u[4])  # Set password securely
        
        # Assign user to the corresponding role group
        role_group, created = Group.objects.get_or_create(name=u[5])  # Create the group if it doesn't exist
        user.groups.add(role_group)  # Assign user to this group
        user.save()

# ------ Departments ------ #
departments = [
    ("networkEngineering", "msingh", "fsheikh"),
    ("fieldEngineering", "msingh", "dnguyen"),
]

# Create departments ensuring the seniorManager and deptLeader users exist
for d in departments:
    senior_manager = User.objects.get(username=d[1])
    dept_leader = User.objects.get(username=d[2])
    
    # Get or create the department
    dept, created = Department.objects.get_or_create(deptName=d[0])
    if created:
        dept.seniorManager = senior_manager
        dept.deptLeader = dept_leader
        dept.save()
    else:
        # If it already exists, just update the fields
        dept.seniorManager = senior_manager
        dept.deptLeader = dept_leader
        dept.save()

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

# Create teams ensuring the teamLeader and deptName users exist
for t in teams:
    dept = Department.objects.get(deptName=t[1])
    team_leader = User.objects.get(username=t[2])
    
    # Get or create the team
    team, created = Team.objects.get_or_create(teamName=t[0], deptName=dept)
    if created:
        team.teamLeader = team_leader
        team.save()
    else:
        # If the team exists, just update the teamLeader
        team.teamLeader = team_leader
        team.save()

# ------ Sessions ------ #
sessions = [
    ("S2025Q1", "2025", "Q1"),
    ("S2025Q2", "2025", "Q2"),
]

# Create sessions
for s in sessions:
    Session.objects.get_or_create(sessionId=s[0], sessionYear=s[1], sessionQuarter=s[2])

# ------ Session Assignment ------ #
assignments = [
    ("A1", "jsmith", "S2025Q1", "There has been a noticeable improvement in receiving support since the last time I took the quiz."),
    ("A2", "jsmith", "S2025Q2", "I don’t feel like the work I’m currently doing is delivering value."),
]

# Assign session assignments
for a in assignments:
    session = Session.objects.get(sessionId=a[2])
    user = User.objects.get(username=a[1])
    
    # Get or create session assignment
    SessionAssignment.objects.get_or_create(assignId=a[0], username=user, sessionId=session, additionalComments=a[3])

# ------ Votes ------ #
votes = [
    ("V1", 3, 60, "C1", "S2025Q1", "jsmith", "A1"),
    ("V2", 4, 70, "C2", "S2025Q1", "jsmith", "A1"),
    ("V3", 5, 65, "C3", "S2025Q1", "jsmith", "A1"),
    ("V4", 4, 55, "C4", "S2025Q1", "jsmith", "A1"),
    ("V5", 3, 60, "C5", "S2025Q1", "jsmith", "A1"),
    ("V6", 3, 72, "C6", "S2025Q1", "jsmith", "A1"),
    ("V7", 5, 64, "C7", "S2025Q1", "jsmith", "A1"),
    ("V8", 5, 50, "C8", "S2025Q1", "jsmith", "A1"),
    ("V9", 3, 62, "C9", "S2025Q1", "jsmith", "A1"),
    ("V10", 4, 68, "C10", "S2025Q1", "jsmith", "A1"),
    ("V11", 3, 70, "C11", "S2025Q1", "jsmith", "A1"),
    ("V12", 5, 85, "C1", "S2025Q2", "jsmith", "A2"),
    ("V13", 4, 80, "C2", "S2025Q2", "jsmith", "A2"),
    ("V14", 5, 85, "C3", "S2025Q2", "jsmith", "A2"),
    ("V15", 5, 65, "C4", "S2025Q2", "jsmith", "A2"),
    ("V16", 4, 70, "C5", "S2025Q2", "jsmith", "A2"),
    ("V17", 5, 70, "C6", "S2025Q2", "jsmith", "A2"),
    ("V18", 3, 60, "C7", "S2025Q2", "jsmith", "A2"),
    ("V19", 3, 74, "C8", "S2025Q2", "jsmith", "A2"),
    ("V20", 4, 80, "C9", "S2025Q2", "jsmith", "A2"),
    ("V21", 4, 90, "C10", "S2025Q2", "jsmith", "A2"),
    ("V22", 3, 67, "C11", "S2025Q2", "jsmith", "A2"),
]

# Create votes ensuring the referenced users and sessions exist
for v in votes:
    session = Session.objects.get(sessionId=v[4])
    assign = SessionAssignment.objects.get(assignId=v[6])
    card = Card.objects.get(cardId=v[3])
    user = User.objects.get(username=v[5])
    
    # Get or create the vote
    Vote.objects.get_or_create(voteId=v[0], rating=v[1], progress=v[2], cardId=card, sessionId=session, username=user, assignId=assign)
