# TwoSuns.ai Email Routing (Website-edits slide 30)

Backend task ("directed emails to be done"), NOT a website change. Set these up as forwarding addresses or distribution groups in the twosuns.ai email admin (Google Workspace or the domain's email forwarding). Owner: Raihaan (holds the domain / Google account).

| Alias | Purpose | Forwards to |
|---|---|---|
| info@twosuns.ai | Sales and General requests | nour@aepg.ca, michelle@aepg.ca, mariam@aepg.ca, belen@aepg.ca, alexa@aepg.ca |
| invest@twosuns.ai | Investor Relations | belen@aepg.ca, aiman@aepg.ca |
| partners@twosuns.ai | Partnerships | nour@aepg.ca, michelle@aepg.ca, mariam@aepg.ca |
| trust@twosuns.ai | Trust & Security | ryan@aepg.ca, kalpesh@aepg.ca |
| careers@twosuns.ai | Recruiting | sara@aepg.ca, alexa@aepg.ca |

## Typos in the deck to confirm
- "nour@aepg" was missing ".ca" → assumed nour@aepg.ca.
- "mariam" vs "marium" appeared both ways → assumed the same person (confirm spelling).

## Connects to the open form-delivery issue
The contact form (and the other site forms) currently do not submit anywhere (no backend). For leads to actually reach these inboxes, the contact form should post to / notify **info@twosuns.ai**, which then fans out per the table above. So two things are needed together:
1. Wire the contact form to a backend (Formspree / HubSpot / web3forms) that delivers to info@twosuns.ai.
2. Set up the forwarding/distribution groups above so info@ (etc.) reach the team.
