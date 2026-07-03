# Information Security Policy
**Nexora Technologies, Inc.**
**Version 5.1 | Effective Date: February 1, 2026**

---

## 1. Purpose and Scope

This Information Security Policy defines Nexora Technologies, Inc.'s ("Nexora") requirements for protecting the confidentiality, integrity, and availability of company information assets. It applies to all employees, contractors, consultants, and any third parties who access Nexora systems, networks, or data.

Non-compliance with this policy may result in disciplinary action up to and including termination of employment or contract, and may also expose the individual and the Company to legal liability.

Security inquiries and incident reports should be directed to the Security team at security@nexora-internal.com.

---

## 2. Information Classification

All Nexora data is classified into one of four tiers:

| Classification | Description | Examples |
|----------------|-------------|----------|
| **Public** | Information approved for external distribution | Marketing materials, public documentation |
| **Internal** | General business information for employee use | Internal wikis, meeting notes, org charts |
| **Confidential** | Sensitive business information with limited distribution | Customer contracts, financial forecasts, product roadmaps |
| **Restricted** | Highest sensitivity; access strictly controlled | Customer PII, authentication credentials, audit logs, M&A materials |

Data must be handled, stored, transmitted, and disposed of according to its classification level. When in doubt, treat data as the next higher classification.

---

## 3. Access Control

### 3.1 Least Privilege Principle
Access to Nexora systems and data is granted on a need-to-know basis. Employees receive only the minimum access required to perform their job functions. Access requests must be submitted through the IT portal and approved by the employee's manager and the Data Owner for Restricted data.

### 3.2 Access Reviews
IT conducts quarterly access reviews for all Restricted and Confidential data systems. Managers are required to certify or revoke access for their direct reports within 10 business days of receiving a review request.

### 3.3 Terminated Employees
All system access must be revoked within 1 business hour of an employee's termination or resignation effective date. People Operations is responsible for triggering access revocation workflows. IT and Security must be notified on the same day.

### 3.4 Third-Party Access
Vendors and contractors who require access to Nexora systems must be approved by the Data Owner and the Security team. Access is time-limited, logged, and reviewed quarterly. Third-party access is governed by the Vendor Management Policy.

---

## 4. Authentication Requirements

### 4.1 Passwords
All accounts must use strong passwords that meet the following criteria:
- Minimum 14 characters
- At least one uppercase letter, one lowercase letter, one number, and one special character
- Not reused from any of the previous 12 passwords
- Not containing the user's name, username, or "Nexora"

Passwords must not be written down or shared with anyone, including IT staff. The IT team will never ask for your password.

### 4.2 Multi-Factor Authentication (MFA)
MFA is mandatory for all Nexora accounts and systems, with no exceptions. MFA must use an authenticator app (e.g., Okta Verify, Google Authenticator, or Microsoft Authenticator). SMS-based MFA is not permitted for Restricted systems. Hardware security keys (FIDO2/WebAuthn) are required for privileged admin accounts.

### 4.3 Single Sign-On (SSO)
All enterprise applications must be integrated with Nexora's Okta SSO environment. Employees must use SSO to authenticate to approved applications. Local account credentials for SSO-enabled apps must be disabled.

### 4.4 Privileged Access
Admin and privileged accounts must be separate from standard user accounts. Privileged actions must be logged. Shared admin credentials are prohibited. Privileged Access Management (PAM) tools are required for all infrastructure-level access.

---

## 5. Device Security

### 5.1 Approved Devices
Only company-issued devices or BYOD devices registered in Nexora's Mobile Device Management (MDM) system may access Nexora corporate data. Devices must have:
- Full-disk encryption enabled (FileVault for macOS, BitLocker for Windows)
- Automatic screen lock after 5 minutes of inactivity
- Remote wipe capability enabled via MDM
- Current operating system and security patches (no OS version more than 2 major versions behind current)
- Nexora-approved endpoint detection and response (EDR) agent installed

### 5.2 Patch Management
Security patches rated Critical or High must be applied within 7 days of release. Other patches must be applied within 30 days. IT will push critical patches automatically; employees must not defer required updates.

### 5.3 Lost or Stolen Devices
Report any lost or stolen device immediately (within 1 hour of discovery) to IT Security at security@nexora-internal.com and the IT Hotline at 1-866-NEX-SECU. IT will remotely wipe the device. Delay in reporting may constitute a policy violation.

---

## 6. Network Security

### 6.1 VPN
Employees must connect through the Nexora VPN (GlobalProtect) when accessing Internal, Confidential, or Restricted systems from outside a Nexora office network. VPN must remain active throughout the work session. Split-tunneling is not permitted for Restricted data access.

### 6.2 Public Wi-Fi
Employees must not access Nexora systems from unsecured public Wi-Fi (e.g., cafes, airports, hotels) without the VPN active. If the VPN cannot be established, the employee must use a personal mobile hotspot or postpone the work.

### 6.3 Home Networks
Home networks used for remote work must use WPA2 or WPA3 encryption and a strong router password. Default router credentials must be changed. Employees must not connect company devices to networks shared with unknown third parties.

---

## 7. Data Handling and Storage

### 7.1 Approved Storage Locations
Nexora data must be stored only in approved company systems:
- Google Drive (for Internal and Confidential data)
- Nexora's internal document management system (for Restricted data)
- Approved databases and cloud environments (AWS, GCP with Nexora-managed controls)

Personal cloud storage (Dropbox, iCloud, personal Google Drive, etc.) must never be used to store company data.

### 7.2 Data Transmission
Confidential and Restricted data must be encrypted in transit using TLS 1.2 or higher. Email is not an approved transmission method for Restricted data; use the secure file transfer tool (SecureDrop) accessible at securedrop.nexora-internal.com.

### 7.3 Data Retention and Disposal
Data must be retained per the schedule defined in the Data Retention Schedule (wiki.nexora-internal.com/legal/data-retention). When data reaches end of retention, it must be securely deleted using approved methods (cryptographic erasure for digital data, cross-cut shredding for physical documents). Unapproved deletion of data subject to legal holds is prohibited.

---

## 8. Acceptable Use

### 8.1 Permitted Use
Company systems are provided for business use. Incidental personal use that does not interfere with job performance, consume significant resources, or create security or legal risk is permitted.

### 8.2 Prohibited Activities
The following are strictly prohibited on any company system or network:
- Accessing, storing, or distributing illegal content (including pirated software)
- Disabling or bypassing security controls
- Attempting to access systems or data without authorization
- Installing unapproved software or browser extensions on company devices
- Using company systems for cryptocurrency mining
- Sending Restricted data via personal email or unapproved channels
- Sharing credentials with colleagues or third parties

---

## 9. Phishing and Social Engineering

Employees must be vigilant against phishing emails and social engineering attacks. If an email looks suspicious:
- Do not click links or open attachments
- Forward the email as an attachment to phishing@nexora-internal.com
- Report it using the Phish Alert button in Gmail

Employees who repeatedly click simulated phishing links will be required to complete additional security awareness training. Security awareness training is mandatory for all employees annually.

---

## 10. Incident Reporting

Any suspected security incident—including unauthorized access, data exposure, malware, or lost devices—must be reported immediately to the Security team:
- Email: security@nexora-internal.com
- Hotline: 1-866-NEX-SECU (available 24/7)
- Slack: #security-incidents (for non-urgent matters)

Early reporting is critical. Employees who report incidents promptly are protected from retaliation under this policy, regardless of whether they contributed to the incident.

---

## 11. Security Awareness Training

All employees must complete the annual security awareness training course within 30 days of hire and within 30 days of each annual renewal. Completion is tracked in the LMS. Employees who do not complete training within the required window will have system access suspended until training is finished.

---

## 12. Exceptions

Requests for exceptions to this policy must be submitted to the Security team with a business justification, risk assessment, and proposed compensating controls. Exceptions must be approved by the CISO and reviewed annually.

---

*Last reviewed: January 2026*
*Document owner: Chief Information Security Officer (CISO)*
*Approved by: CTO and CEO*
