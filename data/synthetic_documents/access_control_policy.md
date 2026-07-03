# Access Control Policy
**Nexora Technologies, Inc.**
**Version 2.5 | Effective Date: January 1, 2026**

---

## 1. Purpose and Scope

This Access Control Policy establishes Nexora Technologies, Inc.'s ("Nexora") requirements for managing logical and physical access to systems, data, networks, and facilities. Its goal is to ensure that access is granted only to authorized individuals, for legitimate business purposes, and at the minimum level required to perform their function.

This policy applies to:
- All employees, contractors, temporary workers, and vendors
- All Nexora-owned or Nexora-managed systems, networks, cloud environments, and physical locations
- All access types: user accounts, service accounts, API keys, privileged access, physical badges

Questions should be directed to the IT Security team at security@nexora-internal.com.

---

## 2. Governing Principles

### 2.1 Least Privilege
Every user, process, and system component must be granted only the minimum access required to perform its intended function. Broad or permissive access should never be used as a convenience.

### 2.2 Need to Know
Access to data is governed by whether the user has a legitimate need to view, process, or modify it—not solely by their role or seniority.

### 2.3 Separation of Duties
Critical functions must be divided among multiple individuals to prevent fraud and error. No single person should be able to initiate and approve a sensitive transaction, or deploy and approve their own code to production.

### 2.4 Defense in Depth
Access controls are layered: network controls, application controls, and data-level controls all operate independently. Failure of one layer must not be sufficient to expose sensitive resources.

---

## 3. User Account Management

### 3.1 Account Provisioning
New user accounts are provisioned through Nexora's identity management system (Okta) based on a request from the employee's manager. The request must specify:
- The user's role and department
- The systems required for job function
- The access level needed (e.g., read-only, contributor, admin)
- The expected duration (permanent or time-limited)

Accounts are not created until the provisioning request is approved by both the manager and the relevant system's Data Owner. Provisioning must be completed within 1 business day of a new hire's start date for standard access.

### 3.2 Account Naming Convention
User accounts follow the format **firstname.lastname@nexoratech.com**. Service accounts use a descriptive name in the format **svc-[purpose]-[environment]** (e.g., svc-billing-prod). Generic or shared user accounts are prohibited.

### 3.3 Account Modification
Changes to access level, role, or system permissions must follow the same approval process as provisioning. Manager- or role-driven changes are automatically triggered in Okta when a job change is processed in Workday.

### 3.4 Account Deprovisioning
Access must be revoked promptly in the following scenarios:

| Trigger | Revocation Deadline |
|---------|-------------------|
| Employee termination (voluntary or involuntary) | Within 1 business hour |
| Contractor/vendor engagement end | Within 1 business hour |
| Role change (loss of need for certain access) | Within 1 business day |
| Leave of absence exceeding 30 days | Within 2 business days |
| Failed access review (recertification) | Within 3 business days |

People Operations is responsible for triggering termination workflows in Okta, which automatically propagate to all integrated systems. IT Security must receive a termination notification on the same day.

---

## 4. Privileged Access

### 4.1 Definition
Privileged access includes accounts with system administrator rights, root access, database administrator access, network device access, cloud IAM admin roles, and any account with the ability to modify security configurations, audit logs, or access control settings.

### 4.2 Privileged Account Requirements
- Privileged accounts must be separate from standard user accounts (e.g., a user may have `jane.doe@nexoratech.com` and a separate `jane.doe-admin@nexoratech.com` account)
- All privileged accounts must use hardware security keys (FIDO2/WebAuthn) for MFA—no exceptions
- Privileged sessions must be brokered through the Nexora Privileged Access Management (PAM) tool (CyberArk)
- All privileged sessions are recorded and retained for 12 months
- Privileged access requests require CISO approval for production systems

### 4.3 Emergency "Break Glass" Access
A small set of emergency privileged credentials ("break glass") are maintained for disaster recovery scenarios where normal access mechanisms are unavailable. These credentials are stored in CyberArk's offline vault. Use of break glass access is logged, automatically alerts the CISO, and requires a post-use justification within 4 hours.

### 4.4 Service Accounts and API Keys
- Service accounts must have documented purpose, owner, and expiry date
- Service account passwords must meet the same requirements as user passwords and rotate every 90 days
- API keys must be stored in Nexora's secrets management system (HashiCorp Vault), not in source code, configuration files, or environment variables accessible outside the deployment pipeline
- Unused service accounts or API keys must be disabled within 30 days of inactivity

---

## 5. Access Reviews

### 5.1 Recertification Schedule
Access reviews (recertification) are conducted on the following schedule:

| Access Type | Review Frequency | Reviewer |
|-------------|-----------------|---------|
| Restricted data systems | Quarterly | Data Owner + Manager |
| Confidential data systems | Semi-annual | Manager |
| General (Internal) systems | Annual | Manager |
| Privileged accounts | Quarterly | CISO + System Owner |
| Third-party / vendor access | Quarterly | Data Owner |

### 5.2 Recertification Process
Managers and Data Owners receive recertification tasks in the Nexora access governance tool (SailPoint). Reviewers must:
- Confirm that each listed access is still necessary and appropriate
- Revoke any access that is no longer needed
- Escalate any suspicious or unexplained access to IT Security

Reviewers who do not complete recertification within the 10-business-day window will have their own access suspended until the review is complete.

---

## 6. Authentication Requirements

All accounts must comply with Nexora's authentication standards, as defined in the Security Policy:

- **Standard accounts**: 14-character minimum password; Okta Verify (TOTP/push) MFA required
- **Privileged accounts**: Hardware security key (FIDO2) MFA required; PAM session brokering required
- **Service accounts**: Certificate-based or secret-manager-vaulted credentials; no interactive login permitted
- **SSO**: All applications must enforce Okta SSO. Local credential bypass is prohibited
- **Session timeouts**: Interactive sessions must time out after 30 minutes of inactivity for Internal systems and 15 minutes for Restricted systems

---

## 7. Remote Access

Remote access to Nexora systems is permitted only through:
- Nexora GlobalProtect VPN (for general internal access)
- Nexora CyberArk PAM portal (for privileged infrastructure access)
- Nexora-approved jump hosts or bastion servers (for cloud infrastructure access)

Direct remote desktop access (RDP) to production servers from employee endpoints is prohibited. SSH access to production servers must use certificate-based authentication and must be brokered through CyberArk.

---

## 8. Physical Access Controls

### 8.1 Office Access
Access to Nexora office facilities is controlled through electronic badge readers. Badges are issued by Facilities on the first day of employment. Badge access is tied to the employee's Workday profile and automatically deactivated upon termination.

### 8.2 Restricted Physical Areas
The following areas require elevated badge authorization:
- Server rooms and network closets: IT Operations staff only
- Executive suite: Senior leadership and authorized escorts only
- Finance and Legal areas: Department staff only, with visitor log for guests

Visitors must be escorted at all times in all office areas. Tailgating through secure doors is strictly prohibited and must be reported to Facilities.

### 8.3 Lost or Stolen Badges
Report a lost or stolen badge immediately to Facilities (facilities@nexora-internal.com) during business hours, or to the building security desk after hours. The badge will be deactivated within 30 minutes of the report.

---

## 9. Cloud Access Controls

### 9.1 AWS, GCP, and Azure
All cloud platform access must be:
- Managed through Nexora's cloud identity federation (Okta → cloud IAM)
- Granted per-role using Infrastructure as Code (Terraform) rather than manual console operations
- Logged in the SIEM (Splunk) and reviewed for anomalies weekly by IT Security
- Subject to access reviews per Section 5

Console access to cloud production environments is restricted to engineers with an approved need and must use MFA. Direct access to production databases from developer laptops is prohibited; production database access requires use of the PAM bastion.

### 9.2 SaaS Applications
All SaaS applications must be provisioned through Okta's application catalog. Shadow IT (SaaS apps accessed with personal credentials or outside Okta) is prohibited. Employees who discover unauthorized SaaS usage must report it to IT Security.

---

## 10. Monitoring and Enforcement

IT Security monitors access activity through:
- SIEM correlation rules for anomalous login patterns (off-hours, impossible travel, brute force)
- Privileged session recording and review
- Data Loss Prevention (DLP) policies on endpoints and email
- Quarterly access reviews

Detected anomalies trigger alerts in the SIEM, which are triaged by the Security On-Call. Confirmed unauthorized access is handled as a security incident under the Incident Response Policy.

---

## 11. Policy Violations

Violation of this policy—including sharing credentials, bypassing access controls, or failing to report unauthorized access—may result in disciplinary action up to and including termination, and may expose the violator to personal legal liability.

---

## 12. Exceptions

Exceptions to this policy require written approval from the CISO. All exceptions must include a business justification, risk assessment, compensating controls, and expiry date. Exceptions are reviewed quarterly.

---

*Last reviewed: December 2025*
*Document owner: Chief Information Security Officer (CISO)*
*Approved by: CTO*
