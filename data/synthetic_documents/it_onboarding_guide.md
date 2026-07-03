# IT Onboarding Guide
**Nexora Technologies, Inc.**
**Version 3.4 | Effective Date: January 1, 2026**

---

## Welcome

This guide walks you through everything you need to set up your Nexora technology environment. Complete all steps in this guide during your first week. If you run into problems, contact IT Help Desk at ithelp@nexora-internal.com or submit a ticket at helpdesk.nexora-internal.com.

IT Help Desk hours: Monday–Friday, 7:00 AM – 8:00 PM CT. For urgent after-hours issues, call 1-866-NEX-TECH.

---

## Step 1: Receive and Unbox Your Equipment

Your equipment will be shipped to your home address (for remote/hybrid hires) or available for pickup at the office IT desk (for on-site hires) before your start date. Standard equipment includes:

- Apple MacBook Pro 14" (M-series) or Dell Latitude 15" (Windows) — based on your role
- USB-C hub or dock
- Wired keyboard and mouse
- Plantronics Voyager headset
- Monitor (for remote/hybrid roles approved for home office setup)

If any items are missing or damaged, email ithelp@nexora-internal.com immediately with your employee ID and a description.

---

## Step 2: Power On and Complete Initial Setup

### macOS
1. Power on the MacBook. Follow the macOS Setup Assistant until you reach the "Sign In with Apple ID" screen.
2. **Skip** signing in with a personal Apple ID. Select "Set Up Later."
3. Create a local admin account with your Nexora-issued temporary password (sent via SMS to your mobile on your start date).
4. Enable FileVault disk encryption when prompted. Save the recovery key to a secure location—IT will also escrow a copy via MDM.

### Windows
1. Power on the laptop. At the "Let's set things up for your organization" prompt, click **Set up for work or school**.
2. Sign in with your Nexora email (firstname.lastname@nexoratech.com) and temporary password.
3. The device will automatically join Azure Active Directory and install required policies.
4. BitLocker encryption will be enabled automatically.

---

## Step 3: Enroll in Okta and Set Up MFA

Nexora uses Okta as its identity provider for Single Sign-On (SSO).

1. Open a browser and navigate to **nexora.okta.com**
2. Sign in with your Nexora email and temporary password
3. You will be prompted to change your password. Set a new password meeting the requirements in the Security Policy (minimum 14 characters, mixed case, numbers, and special characters)
4. Enroll in Multi-Factor Authentication (MFA):
   - Download **Okta Verify** from the App Store or Google Play on your personal or company mobile device
   - Scan the QR code displayed on-screen
   - Test the MFA push notification to confirm enrollment
5. Add your personal phone number as a backup MFA method

> **Note**: SMS-based MFA is not permitted as the primary MFA method for any system. Okta Verify (push) is required.

---

## Step 4: Install Nexora MDM (If Using a Personal Device)

If you are using a personal mobile phone or tablet to access company email, Slack, or any Nexora system, you must enroll in Mobile Device Management (MDM) before doing so.

1. On your personal device, open a browser and navigate to **mdm.nexora-internal.com/enroll**
2. Sign in with your Nexora Okta credentials
3. Follow the device-specific instructions to install the Nexora MDM profile
4. The MDM profile enables remote wipe of company data only (not personal data). IT cannot read personal messages or photos on your device.

Devices not enrolled in MDM may not access Nexora systems. This is enforced technically by Okta device trust policies.

---

## Step 5: Install Required Applications

Once enrolled in Okta, your device's application management system (Jamf for Mac, Intune for Windows) will automatically push required applications. This may take 20–45 minutes. Required applications include:

| Application | Purpose |
|-------------|---------|
| Slack | Internal messaging and collaboration |
| Google Chrome | Primary web browser |
| Google Drive for Desktop | File sync and access |
| Zoom | Video meetings |
| GlobalProtect | VPN client |
| CrowdStrike Falcon | Endpoint protection (EDR) |
| Okta Verify | MFA authenticator |
| 1Password | Password manager |

Do not install additional software without IT approval. Submit software requests via the IT portal at helpdesk.nexora-internal.com under "Software Request."

---

## Step 6: Set Up VPN

The VPN client (GlobalProtect) is required when accessing Nexora internal systems from any network that is not a Nexora office.

1. Open **GlobalProtect** from your applications
2. When prompted for a gateway, enter: **vpn.nexoratech.com**
3. Sign in with your Okta credentials (it will use SSO)
4. Click **Connect** — you will receive an Okta Verify MFA push
5. Approve the push; the VPN will connect automatically

GlobalProtect is configured to connect automatically when you leave the office network. You can disconnect manually if needed, but do so only when you do not need to access internal systems.

---

## Step 7: Set Up Email and Calendar

Nexora uses Google Workspace for email and calendar.

1. Open **Google Chrome** and navigate to **mail.google.com**
2. Sign in with your Nexora email address (Okta SSO will handle authentication)
3. Your email signature template will be pre-populated. Update it with your title and direct phone number
4. Open **calendar.google.com** and set your working hours and time zone in Settings → Working Hours

Your Nexora email address is: **firstname.lastname@nexoratech.com**
Aliases and distribution groups will be configured by your manager or team admin.

---

## Step 8: Join Slack Workspaces

1. Open the **Slack** application
2. Sign in to the workspace: **nexora.slack.com** (Okta SSO)
3. You will be automatically added to your department channels
4. Join the following company-wide channels manually:
   - **#announcements** — Company-wide news
   - **#it-help** — IT questions and tips
   - **#security-alerts** — Security notices
   - **#all-hands** — All-hands meeting recordings and notes
5. Set your Slack display name to match your full name as it appears in Workday
6. Upload a professional headshot as your profile photo

---

## Step 9: Set Up 1Password

Nexora provides 1Password Business licenses for all employees.

1. Open **1Password** from your applications
2. Sign in with your Nexora email (Okta SSO)
3. Install the 1Password browser extension for Chrome
4. Generate and save your Nexora Okta master password recovery kit using 1Password
5. Use 1Password to create and store unique passwords for any non-SSO accounts you need

Do not store Nexora passwords in browser-native password managers (Chrome Passwords, Safari Keychain). Only 1Password is approved.

---

## Step 10: Request Access to Core Systems

Your manager will submit access provisioning requests for the systems you need on or before your start date. Common systems include:

| System | Access Requested By |
|--------|-------------------|
| GitHub (Engineering) | Engineering Manager |
| Salesforce (Sales/CS) | Sales/CS Manager |
| AWS Console (Engineering) | Engineering Manager via IT |
| Looker (Analytics) | Manager + Analytics team |
| Workday | Auto-provisioned |
| Jira / Confluence | Auto-provisioned |
| Zendesk (Support) | Support Manager |

If you need access to a system not listed above, submit a request at helpdesk.nexora-internal.com under "Access Request." Access to Restricted systems requires Data Owner approval in addition to manager approval.

---

## Step 11: Complete Required Training

Within your first 30 days, you must complete the following training courses in Nexora's LMS (learning.nexora-internal.com):

1. **Security Awareness Training** — Annual requirement; start immediately
2. **Data Privacy Fundamentals** — Required for all employees
3. **Anti-Harassment and Code of Conduct** — Required by People Operations
4. **Role-Specific Compliance Training** — Assigned based on your department

Training completions are tracked automatically. Overdue training may result in system access suspension.

---

## Troubleshooting Quick Reference

| Issue | Action |
|-------|--------|
| Can't log in to Okta | Email ithelp@nexora-internal.com or call IT Hotline |
| MFA not working | Ensure Okta Verify app is up to date; try backup method |
| VPN won't connect | Check that GlobalProtect is installed and gateway is vpn.nexoratech.com |
| Missing application | Check Jamf Self Service (Mac) or Company Portal (Windows) |
| Phishing email | Use Phish Alert button in Gmail or forward to phishing@nexora-internal.com |
| Lost or stolen device | Call IT Security immediately: 1-866-NEX-SECU |

---

## IT Contacts

| Contact | Channel |
|---------|---------|
| IT Help Desk | ithelp@nexora-internal.com / helpdesk.nexora-internal.com |
| IT Hotline | 1-866-NEX-TECH (Mon–Fri 7 AM–8 PM CT) |
| Security Team | security@nexora-internal.com / 1-866-NEX-SECU (24/7) |
| Slack | #it-help |

---

*Last reviewed: December 2025*
*Document owner: Director of IT Operations*
*Approved by: CTO*
