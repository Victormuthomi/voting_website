import random
from django.utils import timezone
from elections.models import Election
from candidates.models import Candidate
from django.contrib.auth.models import User

# Create sample users
def create_users():
    users = []
    for i in range(5):
        user = User.objects.create_user(
            username=f"user{i}",
            password="password",
            email=f"user{i}@example.com",
        )
        users.append(user)
    return users

# Create sample elections
def create_elections():
    elections = []
    for i in range(3):
        election = Election.objects.create(
            title=f"Election {i + 1}",
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=7),
            description=f"This is the description for Election {i + 1}."
        )
        elections.append(election)
    return elections

# Create sample candidates
def create_candidates(elections):
    for election in elections:
        for j in range(3):
            Candidate.objects.create(
                first_name=f"Candidate {j + 1}",
                last_name=f"Last Name {j + 1}",
                motto=f"Motto of Candidate {j + 1}",
                id_number=f"ID{random.randint(1000, 9999)}",
                phone_number=f"07123456{random.randint(10, 99)}",
                seat=f"Seat {j + 1} for {election.title}",
                manifesto=f"This is the manifesto of Candidate {j + 1} for {election.title}.",
                picture=f"media/candidate_pictures/download_{j + 1}.jpeg",  # Assuming you have images named accordingly
                election=election
            )

# Main function to create data
def create_sample_data():
    users = create_users()
    elections = create_elections()
    create_candidates(elections)
    print("Sample data created successfully!")

# Run the data creation
create_sample_data()