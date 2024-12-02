
print("Welcome to the Election Analysis App")
name = input("What's your name: ")
print(f"Welcome to the Election Analysis App: {name}")
print("What would you like to see today?")



import csv

#classes
class MP:
    def __init__(self, Member_first_name, Member_surname, Member_gender, party, constituency, votes_received):
        self.first_name = Member_first_name
        self.last_name = Member_surname
        self.gender = Member_gender
        self.party = party
        self.constituency = constituency
        self.votes = int(votes_received)

    def get_vote_percentage(self, total_votes_cast):
        return (self.total_votes / total_votes_cast) * 100 if total_votes_cast > 0 else 0


class Constituency:
    def __init__(self, name, Region_name= "",Country_name="", Electorate=0, Valid_votes=0, Majority=0, result=""):
        self.name = name
        self.region_name = Region_name
        self.country_name = Country_name
        self.electorate = Electorate
        self.valid_votes = int(Valid_votes)
        self.majority = Majority
        self.result = result
        self.mp = None

    def none_mp(self,mp):
        self.mp = mp


class Party:
    def __init__(self, party_name, Region):
        self.name = party_name
        self.region = Region
        self.total_votes = 0
        self.candidates = 0

    def increase_votes(self, votes):
        self.total_votes += votes

    def add_candidates(self):
        self.candidates += 1


#CSV

def read_data(file_path):
    Constituencies = {}
    parties = {}
    mps = []
    """
    try:
         
"""
    with open("EditedData.csv", mode="r", encoding="ISO-8859-1") as file:
            reader = csv.DictReader(file)
            for row in reader:
                
                constituency_name = row["Constituency name"]
                if constituency_name not in Constituencies:
                    Constituencies[constituency_name] = Constituency(
                        constituency_name,
                        Region_name=row["Region name"] ,
                        Country_name=row["Country name"],
                        Electorate=int(row["Electorate"]),
                        Valid_votes=int(row["Valid votes"]),
                        Majority=int(row["Majority"]),
                        result=  row["Result"]
                    )
                    
                    
                    
                    
                    
                
        
                

                party_name = row["First party"]
                if party_name not in parties:
                    parties[party_name] = Party(party_name, row["Region name"])


                parties[party_name].increase_votes(int(row["Valid votes"]))
                parties[party_name].add_candidates()


                mpss = MP(
                    row["Member first name"],
                    row["Member surname"],
                    row["Member gender"],
                    row["First party"],
                    row["Constituency name"],
                    row["Valid votes"],
                    
                )
                
                mps.append(mpss)
                Constituencies[constituency_name].none_mp(mpss)
                
        
    return Constituencies, parties, mps
"""
    except FileNotFoundError:
        print("Error: CSV file not found.")
    except Exception as e:
        print(f"Error reading data: {e}")
"""

#Main Menu

def display_menu(Constituencies, parties, mps):
  while True:
    print("\n--- Election Analysis Menu ---")
    print("1. List all MPS")
    print("2. List all Constituency")
    print("3. List all parties")
    print("4. View Candidate details")
    print("5. View Contituency details")
    print("6. View statistics for a specific party")
    print("7. Calculate vote percentage for an MP")
    print("8. Save statistics to a file")
    print("9. Exit")

    try:
        choice = int(input("Enter your choice (1-9): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        print("Here is a list of all the mps: ")
        all_mps(mps)
    elif choice == 2:
        print("Here is a list of all the Constituency")
        all_constituencies(Constituencies)
    elif choice == 3:
        print("Here is a list of all the parties: ")
        all_parties(parties)
    elif choice == 4:
        print("Here are the details for the candidate: ")
        view_candidate(parties)
    elif choice == 5:
        print("Here are the details for the required constituency: ")
        view_constituency(Constituencies)
    elif choice == 6:
        print("Here are the statistics for the required party: ")
        view_statistics(parties)
    elif choice == 7:
        print("Here is the vote percentage for the required MP: ")
        calculate_votepercentage(mps)
    elif choice == 8:
        print("A file will be saved: ")
        save_stats(parties) 
    elif choice == 9:
        print("EXITING PROGRAM!!!. THANK YOU FOR CHOOSING THE ELECTION ANALYSIS APP. HAVE A GREAT DAY!!!. BYE!!! ")
        break
    else:
        print("INVALID INPUT!!! PLEASE SELECT A VALID OPTION FROM 1-9!!! ")


#Main


def all_mps(mps):
    print("\nList of MPS: ")
    for mp in mps:
        print(f"{mp.first_name} {mp.last_name} ({mp.party} - {mp.constituency})")



def all_constituencies(constituencies):
    print("\nList of Constituencies: ")
    for name in constituencies:
        print(name)


def all_parties(parties):
    print("\nList of Parties: ")
    for Party in parties:
        print(Party)

def view_candidate(parties):
    candidate_name = input("Please enter the name of the candidate: ")
    if candidate_name in parties:
        print(candidate_name)
    else:
        print("Candidate not found!!!")


def view_constituency(constituencies):
    Constituency_name = input("Please enter the name of the constituency: ")
    if Constituency_name in constituencies:
        print(Constituency_name)
    else: 
        print("Constituency not found!!!")


def view_statistics(parties):
    view_stats_name = input("Please enter party name: ")
    if view_stats_name in parties:
        print(f"\nStatistics for {view_stats_name}")





def calculate_votepercentage(mps):
    calculate_percentage = input("Please enter the Mp name: ")






def save_stats(parties):
    save_this = input("Your file will be saved: ")









file_path = "EditedData.csv"
Constituencies, parties, mps = read_data(file_path)

if Constituencies and parties and mps:
    display_menu(Constituencies, parties, mps)
else:
    print("Failed to load data. Please check the file and try again")
       
