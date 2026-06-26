class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        unique_emails = set()
        
        for email in emails:
            username, domain = email.split('@')
            username = username.split('+')[0].replace('.', '')
            unique_emails.add(username + domain)

        print(unique_emails)

        return len(unique_emails)


