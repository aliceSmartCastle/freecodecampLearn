import datetime
import sys
from typing import Any


class Email:
    def __init__(self, receiver: "User", sender: "User", subject: str, body: str):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False

    def mark_as_read(self) -> None:
        self.read = True

    def display_full_email(self) -> str:
        self.mark_as_read()
        Email_header = f'\n--- Email ---'
        From = f'From: {self.sender.name}'
        To = f'To: {self.receiver.name}'
        subject = f'Subject: {self.subject}'
        received = f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
        body = f'Body: {self.body}'
        line = '------------\n'
        return Email_header + '\n' + From + '\n' + To + '\n' + subject + '\n' + received + '\n' + body + '\n' + line

    def __str__(self) -> str:
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


class Inbox:
    def __init__(self):
        self.emails = []

    def receive_email(self, email: Email) -> None:
        self.emails.append(email)

    def list_emails(self) -> str:
        if not self.emails:
            return 'Your inbox is empty.\n'
        get_email = '\nYour Emails:'
        email_item = ""
        for i, email in enumerate(self.emails, start=1):
            email_item += f'{i}. {email}'
        return get_email + '\n' + email_item

    def read_email(self, index: int) -> str | Any:
        if not self.emails:
            return 'Inbox is empty.\n'
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            return 'Invalid email number.\n'
        return self.emails[actual_index].display_full_email()

    def delete_email(self, index: int) -> str:
        if not self.emails:
            return 'Inbox is empty.\n'
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            return 'Invalid email number.\n'
        del self.emails[actual_index]
        return 'Email deleted.\n'


class User:
    def __init__(self, name: str):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver: "User", subject: str, body: str) -> str:
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        return f'Email sent from {self.name} to {receiver.name}!\n'


    def check_inbox(self) -> str:
        name_info = f"\n{self.name}'s Inbox:"
        inbox_certain = self.inbox.list_emails()
        return name_info + '\n' + inbox_certain

    def read_email(self, index: int) -> str:
        return self.inbox.read_email(index=index)

    def delete_email(self, index: int) -> str:
        return self.inbox.delete_email(index=index)


def determines_email_life(Users: User) -> None:
    print(f"--------email send start---------\n")
    print(Users.check_inbox())
    print(Users.read_email(index=1))
    print(Users.delete_email(index=1))
    print(Users.check_inbox())
    print("-------email receiver end----------\n")


def main() -> None:
    tory = User(name='Tory')
    ramy = User(name='Ramy')
    print(ramy.send_email(receiver=tory, subject='Re: Hello', body='Hi Tory, hope you has free time.'))
    print(tory.send_email(receiver=ramy, subject='Hello', body='Hi Ramy, just saying hello!'))
    determines_email_life(Users=ramy)



if __name__ == '__main__':
    main()

