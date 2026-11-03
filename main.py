import csv
from pathlib import Path


def load_tickets(file_path):
    with open(file_path, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def main():
    project_folder = Path(__file__).resolve().parent
    file_path = project_folder / "data" / "sample_tickets.csv"

    tickets = load_tickets(file_path)

    print(f"Total tickets: {len(tickets)}")
    print()

    for ticket in tickets:
        print(f"Ticket ID: {ticket['id']}")
        print(f"Subject: {ticket['subject']}")
        print(f"Description: {ticket['description']}")
        print(f"Category: {ticket['category']}")
        print(f"Status: {ticket['status']}")
        print()


if __name__ == "__main__":
    main()