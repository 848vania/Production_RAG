# Incident Response Policy
**Nexora Technologies, Inc.**
**Version 3.0 | Effective Date: January 1, 2026**

---

## 1. Purpose

This policy establishes Nexora Technologies, Inc.'s ("Nexora") framework for identifying, managing, containing, and recovering from security incidents and operational disruptions. It defines roles, responsibilities, escalation paths, and communication protocols to minimize impact and restore normal operations as quickly as possible.

This policy applies to all employees, contractors, and third parties who may discover, report, or respond to an incident affecting Nexora systems, data, or operations.

---

## 2. Definitions

| Term | Definition |
|------|-----------|
| **Security Incident** | Any event that potentially compromises the confidentiality, integrity, or availability of Nexora's information assets |
| **Data Breach** | A confirmed or suspected unauthorized access to, disclosure of, or loss of personal data or confidential company data |
| **Service Disruption** | An unplanned outage or degradation of a Nexora internal or customer-facing system |
| **Severity Level** | A rating (P1–P4) assigned to an incident based on its actual or potential impact |
| **Incident Commander (IC)** | The individual responsible for coordinating the response to a declared incident |
| **Incident Response Team (IRT)** | The cross-functional group assembled to respond to a specific incident |

---

## 3. Incident Severity Levels

All incidents are assigned a severity level at declaration. Severity may be upgraded or downgraded as more information becomes available.

| Level | Name | Criteria | Example |
|-------|------|----------|---------|
| **P1** | Critical | Immediate, widespread impact on production systems or confirmed breach of Restricted data | Ransomware on production servers; confirmed exfiltration of customer PII |
| **P2** | High | Significant impact on internal operations or unconfirmed suspected breach | Phishing attack with credential compromise; major internal system outage |
| **P3** | Medium | Limited impact, contained, workaround available | Single endpoint malware (contained); failed unauthorized access attempt |
| **P4** | Low | Minimal or no operational impact; informational | Suspicious email reported; policy violation with no data exposure |

---

## 4. Incident Response Team

The Incident Response Team (IRT) is composed of permanent members and additional responders assembled based on the nature of the incident.

### 4.1 Core IRT Members
| Role | Primary Contact | Backup |
|------|----------------|--------|
| CISO (IRT Lead) | ciso@nexora-internal.com | VP Engineering |
| Security Engineering Lead | seceng@nexora-internal.com | Security Engineer On-Call |
| IT Operations Lead | itops@nexora-internal.com | IT On-Call |
| Legal Counsel | legal@nexora-internal.com | Outside Counsel |
| Data Privacy Officer | privacy@nexora-internal.com | Legal Counsel |
| Communications Lead | comms@nexora-internal.com | VP Marketing |

### 4.2 Additional Responders (as needed)
- Engineering (affected systems)
- Customer Success (if customers impacted)
- Finance (if financial systems involved)
- Executive Sponsor (P1 only: CEO or COO)
- External forensics firm (Nexora retainer: CyberGuard Forensics, 1-800-CYB-FRNS)

---

## 5. Incident Response Phases

### Phase 1: Detection and Reporting

Anyone who discovers or suspects an incident must report it immediately through one of the following channels:

- **Email**: security@nexora-internal.com
- **Hotline**: 1-866-NEX-SECU (24/7)
- **Slack**: #security-incidents (for non-urgent matters)
- **In-person**: Any member of the Security team

Reports should include: what was observed, when it was discovered, which systems or data may be affected, and any actions already taken. Employees must not attempt to investigate or remediate incidents independently—report and preserve.

**Preservation**: Do not power off, reimage, or delete anything on a potentially affected system. Preserve logs, emails, and any evidence. Notify your manager as well as the Security team.

### Phase 2: Triage and Severity Assignment

The Security On-Call engineer acknowledges all reports within 15 minutes (P1/P2) or 2 hours (P3/P4) and performs initial triage to:
- Confirm the incident is real (vs. false positive)
- Assign a preliminary severity level (P1–P4)
- Notify the CISO for P1/P2 incidents
- Open a dedicated incident channel in Slack (#inc-YYYY-MM-DD-[name])
- Create an incident ticket in Jira (Security project)

For P1 incidents, the Security On-Call has authority to immediately engage the full IRT, begin containment, and notify the CISO and General Counsel without waiting for additional approvals.

### Phase 3: Containment

Containment actions are designed to stop the spread of the incident and prevent further damage. Actions depend on the incident type:

**Common containment actions:**
- Disable compromised user accounts (immediate, via Okta)
- Isolate affected endpoints from the network (via CrowdStrike or IT remote access)
- Revoke API keys, tokens, or certificates suspected of compromise
- Block malicious IP addresses or domains at the network perimeter
- Take affected systems offline (requires IC approval for production systems)
- Preserve forensic evidence before containment where possible

All containment actions must be documented in the incident ticket with timestamp, action taken, and person responsible.

### Phase 4: Investigation and Analysis

The Security team leads the investigation to determine:
- Root cause of the incident
- Full scope of affected systems and data
- Timeline of attacker/unauthorized activity
- Whether data exfiltration occurred
- Identity of compromised accounts or credentials

External forensics support (CyberGuard) is engaged at the IC's discretion for P1 incidents or when internal capabilities are insufficient.

### Phase 5: Eradication

After investigation, the Security team removes the root cause and all attacker footholds:
- Removing malware or unauthorized access mechanisms
- Resetting all compromised credentials
- Applying patches or configuration fixes that allowed the incident
- Conducting adversary hunt to identify any remaining persistence

The Incident Commander must approve eradication completion before moving to recovery.

### Phase 6: Recovery

Recovery restores affected systems to normal operation:
- Restore from clean backups where necessary
- Reconnect isolated systems after Security sign-off
- Monitor closely for 72 hours post-recovery for signs of recurrence
- Validate system integrity before returning to production

Customers impacted by a service disruption are notified via the StatusPage (status.nexoratech.com) as soon as practicable. Customer-facing communications are drafted by the Customer Success and Communications leads and approved by the CISO and General Counsel.

### Phase 7: Post-Incident Review

A post-incident review (PIR) must be completed within:
- 5 business days: P1 and P2 incidents
- 15 business days: P3 incidents
- P4 incidents may be documented in the ticket only, at the IC's discretion

The PIR documents:
- Incident timeline
- Root cause analysis
- Impact assessment (systems, data, customers, financial)
- Response effectiveness
- Corrective and preventive actions (CAPA) with owners and due dates

PIR reports for P1/P2 incidents are reviewed by the CISO and presented to the Executive Team.

---

## 6. Notification Requirements

### 6.1 Internal Escalation
| Severity | CISO | CEO/COO | General Counsel | Board |
|----------|------|---------|----------------|-------|
| P1 | Immediate | Within 1 hour | Within 1 hour | Within 24 hours |
| P2 | Within 15 min | Within 4 hours | Within 4 hours | As needed |
| P3 | Within 2 hours | Not required | Advise as needed | No |
| P4 | Daily summary | No | No | No |

### 6.2 Regulatory and Legal Notification
Data breaches involving personal data may require notification to:
- **Regulatory authorities**: GDPR requires notification to the lead supervisory authority within **72 hours** of discovery. US state breach notification laws vary (typically 30–72 hours or 30–45 days for affected individuals).
- **Affected individuals**: If the breach creates risk to rights and freedoms, affected individuals must be notified without undue delay.

The Privacy Officer and Legal Counsel jointly determine notification obligations. No notification is sent to regulators or individuals without General Counsel approval.

### 6.3 Customer Notification
If a breach involves customer data, the Customer Success Lead and VP of Sales must be informed within 4 hours of a confirmed P1 breach. Customer notification content and timing is coordinated by Legal, Communications, and Customer Success.

---

## 7. Evidence Handling

All digital evidence must be collected and preserved in a forensically sound manner. Evidence handling procedures:
- Create forensic images before analysis where possible
- Maintain chain of custody documentation
- Store evidence in the designated secure evidence folder on the Security team's drive
- Retain evidence for a minimum of 3 years, or longer if subject to litigation hold

---

## 8. Communication Protocols

During an active incident:
- All incident communication occurs in the dedicated incident Slack channel (#inc-YYYY-MM-DD-[name])
- Status updates are posted at minimum every hour for P1, every 4 hours for P2
- External communication (media, customers, regulators) requires CISO, Legal, and Communications approval
- Employees must not discuss the incident on personal social media, with family members, or with anyone outside the IRT
- Press inquiries must be directed to communications@nexoratech.com

---

## 9. Training and Testing

- All IRT members complete incident response training annually
- Nexora conducts a tabletop exercise at least twice per year simulating realistic incident scenarios
- A full incident response simulation (red team exercise) is conducted annually with the external security firm
- After each exercise, the IRT documents lessons learned and updates this policy and runbooks accordingly

---

## 10. Runbooks

Detailed technical runbooks for specific incident types are maintained by the Security team at wiki.nexora-internal.com/security/runbooks. Runbooks exist for:
- Phishing and credential compromise
- Ransomware and malware
- Unauthorized data access or exfiltration
- Insider threat
- Third-party/vendor compromise
- DDoS and service availability incidents
- Lost or stolen devices

---

*Last reviewed: December 2025*
*Document owner: Chief Information Security Officer (CISO)*
*Approved by: CEO and General Counsel*
