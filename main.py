def main():
    ticket = {
        "id": 1,
        "subject": "Cannot log in",
        "description": "My password is not working.",
        "category": "account",
        "status": "open",
    }

    print(f"Ticket ID: {ticket['id']}")
    print(f"Subject: {ticket['subject']}")
    print(f"Description: {ticket['description']}")
    print(f"Category: {ticket['category']}")
    print(f"Status: {ticket['status']}")


if __name__ == "__main__":
    main()