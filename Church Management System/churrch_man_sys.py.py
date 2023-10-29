class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SimpleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

class ChurchMember:
    def __init__(self, member_id, name, contact):
        self.member_id = member_id
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"ID: {self.member_id}, Name: {self.name}, Contact: {self.contact}"

class DonationRecord:
    def __init__(self, donor_name, amount):
        self.donor_name = donor_name
        self.amount = amount

    def __str__(self):
        return f"Donor: {self.donor_name}, Amount: ${self.amount}"

class ChurchEvent:
    def __init__(self, event_name, date):
        self.event_name = event_name
        self.date = date

    def __str__(self):
        return f"Event: {self.event_name}, Date: {self.date}"

class ChurchVolunteer:
    def __init__(self, volunteer_name, task):
        self.volunteer_name = volunteer_name
        self.task = task

    def __str__(self):
        return f"Volunteer: {self.volunteer_name}, Task: {self.task}"

class Prayer:
    def __init__(self, requestor_name, request):
        self.requestor_name = requestor_name
        self.request = request

    def __str__(self):
        return f"Requestor: {self.requestor_name}, Prayer Request: {self.request}"

class ChildrenMinistrySession:
    def __init__(self, session_name, date):
        self.session_name = session_name
        self.date = date

    def __str__(self):
        return f"Session: {self.session_name}, Date: {self.date}"

class MissionOutreach:
    def __init__(self, program_name, location):
        self.program_name = program_name
        self.location = location

    def __str__(self):
        return f"Program: {self.program_name}, Location: {self.location}"

class WorshipMusic:
    def __init__(self, title, artist, album):
        self.title = title
        self.artist = artist
        self.album = album

    def __str__(self):
        return f"Title: {self.title}, Artist: {self.artist}, Album: {self.album}"

class FinancialRecord:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"Description: {self.description}, Amount: ${self.amount}"

class ChurchManagementSystem:
    def __init__(self):
        self.members = SimpleLinkedList()
        self.donations = SimpleLinkedList()
        self.events = SimpleLinkedList()
        self.volunteers = SimpleLinkedList()
        self.prayers = SimpleLinkedList()
        self.children_sessions = SimpleLinkedList()
        self.outreach_programs = SimpleLinkedList()
        self.music_tracks = SimpleLinkedList()
        self.financial_records = SimpleLinkedList()

    def add_member(self):
        member_id = input("Enter member ID: ")
        name = input("Enter member name: ")
        contact = input("Enter member contact: ")
        self.members.append(ChurchMember(member_id, name, contact))

    def view_members(self):
        print("\n--- Members Listing ---")
        self.members.print_list()

    def add_donation(self):
        donor_name = input("Enter donor name: ")
        amount = float(input("Enter donation amount: "))
        self.donations.append(DonationRecord(donor_name, amount))

    def view_donations(self):
        print("\n--- Donations Listing ---")
        self.donations.print_list()

    def add_event(self):
        event_name = input("Enter event name: ")
        date = input("Enter date (dd/mm/yyyy): ")
        self.events.append(ChurchEvent(event_name, date))

    def view_events(self):
        print("\n--- Events Listing ---")
        self.events.print_list()

    def add_volunteer(self):
        volunteer_name = input("Enter volunteer name: ")
        task = input("Enter task: ")
        self.volunteers.append(ChurchVolunteer(volunteer_name, task))

    def view_volunteers(self):
        print("\n--- Volunteers Listing ---")
        self.volunteers.print_list()

    def add_prayer(self):
        requestor_name = input("Enter requestor name: ")
        request = input("Enter prayer request: ")
        self.prayers.append(Prayer(requestor_name, request))

    def view_prayers(self):
        print("\n--- Prayers Listing ---")
        self.prayers.print_list()

    def add_children_session(self):
        session_name = input("Enter session name: ")
        date = input("Enter date: ")
        self.children_sessions.append(ChildrenMinistrySession(session_name, date))

    def view_children_sessions(self):
        print("\n--- Children Ministry Sessions Listing ---")
        self.children_sessions.print_list()

    def add_outreach_program(self):
        program_name = input("Enter program name: ")
        location = input("Enter location: ")
        self.outreach_programs.append(MissionOutreach(program_name, location))

    def view_outreach_programs(self):
        print("\n--- Outreach Programs Listing ---")
        self.outreach_programs.print_list()

    def add_music_track(self):
        title = input("Enter song title: ")
        artist = input("Enter artist: ")
        album = input("Enter album: ")
        self.music_tracks.append(WorshipMusic(title, artist, album))

    def view_music_tracks(self):
        print("\n--- Worship Music Listing ---")
        self.music_tracks.print_list()

    def add_financial_record(self):
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))
        self.financial_records.append(FinancialRecord(description, amount))

    def view_financial_records(self):
        print("\n--- Financial Records Listing ---")
        self.financial_records.print_list()

def main():
    church_system = ChurchManagementSystem()

    while True:
        print("\nChurch Management System")
        
        # Add Section
        print("\n-- Add Records --")
        print("1. Add Church Member")
        print("2. Add Donation")
        print("3. Add Event")
        print("4. Add Volunteer")
        print("5. Add Prayer")
        print("6. Add Children Ministry Session")
        print("7. Add Outreach Program")
        print("8. Add Worship Music")
        print("9. Add Financial Record")

        # View Section
        print("\n-- View Records --")
        print("10. View Church Members")
        print("11. View Donations")
        print("12. View Events")
        print("13. View Volunteers")
        print("14. View Prayers")
        print("15. View Children Ministry Sessions")
        print("16. View Outreach Programs")
        print("17. View Worship Music")
        print("18. View Financial Records")

        # Exit
        print("\n0. Exit")
        
        choice = int(input("\nEnter your choice: "))

        # Add choices
        if choice == 1:
            church_system.add_member()
        elif choice == 2:
            church_system.add_donation()
        elif choice == 3:
            church_system.add_event()
        elif choice == 4:
            church_system.add_volunteer()
        elif choice == 5:
            church_system.add_prayer()
        elif choice == 6:
            church_system.add_children_session()
        elif choice == 7:
            church_system.add_outreach_program()
        elif choice == 8:
            church_system.add_music_track()
        elif choice == 9:
            church_system.add_financial_record()
            
        # View choices
        elif choice == 10:
            church_system.view_members()
        elif choice == 11:
            church_system.view_donations()
        elif choice == 12:
            church_system.view_events()
        elif choice == 13:
            church_system.view_volunteers()
        elif choice == 14:
            church_system.view_prayers()
        elif choice == 15:
            church_system.view_children_sessions()
        elif choice == 16:
            church_system.view_outreach_programs()
        elif choice == 17:
            church_system.view_music_tracks()
        elif choice == 18:
            church_system.view_financial_records()

        # Exit
        elif choice == 0:
            break

if __name__ == "__main__":
    main()
