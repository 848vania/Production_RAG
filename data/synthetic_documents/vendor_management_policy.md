# Vendor Management Policy
**Nexora Technologies, Inc.**
**Version 2.0 | Effective Date: January 1, 2026**

---

## 1. Purpose and Scope

This Vendor Management Policy establishes Nexora Technologies, Inc.'s ("Nexora") standards for selecting, onboarding, managing, and offboarding third-party vendors, suppliers, and service providers ("vendors"). It is designed to ensure that vendors who access Nexora data, systems, or facilities meet appropriate security, privacy, and compliance standards, and that Nexora's business relationships are governed by appropriate contractual protections.

This policy applies to all employees who engage, manage, or have oversight of vendor relationships. It covers all categories of vendor:
- Software and SaaS providers
- Professional services and consulting firms
- Cloud infrastructure and hosting providers
- Hardware and equipment suppliers
- Facilities and maintenance contractors
- Staffing and contingent workforce agencies

---

## 2. Vendor Risk Tiers

Vendors are classified into three risk tiers based on the sensitivity of data they access and the criticality of services they provide:

| Tier | Description | Examples |
|------|-------------|---------|
| **Tier 1 – Critical** | Access to Restricted data or systems; or service disruption would directly impact Nexora's ability to operate | Cloud infrastructure providers, payroll processor, primary ERP |
| **Tier 2 – Significant** | Access to Confidential data; or service disruption would significantly impair operations | CRM, HRIS, employee benefits administrator |
| **Tier 3 – Standard** | Access to Internal data only or no data access; low operational criticality | Office supplies, catering, low-risk SaaS tools |

Tier assignment is made by the Vendor Manager in consultation with IT Security and Legal. Tier 1 and Tier 2 vendors are subject to additional due diligence requirements.

---

## 3. Vendor Approval Process

No vendor engagement may proceed until the vendor has completed Nexora's approval process. Employees must not engage vendors informally, sign contracts without authorization, or share Nexora data with unapproved vendors.

### 3.1 Initiation
The business owner (employee initiating the vendor relationship) submits a Vendor Request Form through the Procurement portal at procurement.nexora-internal.com. The form requires:
- Vendor name and contact information
- Description of services to be provided
- Estimated annual contract value
- Data types and systems the vendor will access
- Business justification

### 3.2 Due Diligence
Due diligence requirements by tier:

| Requirement | Tier 1 | Tier 2 | Tier 3 |
|-------------|--------|--------|--------|
| Vendor questionnaire (security/privacy) | Required | Required | Optional |
| SOC 2 Type II report review | Required | Required (or equivalent) | Not required |
| Penetration test report review | Required (annual) | Recommended | Not required |
| Financial stability check | Required | Recommended | Not required |
| Reference checks | Required | Recommended | Not required |
| Privacy impact assessment | Required if PII accessed | Required if PII accessed | Not required |
| Legal review | Required | Required | Standard contract only |
| IT Security approval | Required | Required | Self-service if no data access |

The Procurement and IT Security teams jointly conduct Tier 1 and Tier 2 due diligence. Tier 3 approvals may be handled through an automated workflow for standard purchases under $10,000.

### 3.3 Approval Authority
| Contract Value | Approval Required |
|---------------|-------------------|
| Under $10,000/year | Manager |
| $10,000–$50,000/year | Director + Finance |
| $50,000–$250,000/year | VP + Finance + Legal |
| Over $250,000/year | C-Level + Finance + Legal |

All Tier 1 vendors require CISO sign-off regardless of contract value.

---

## 4. Contractual Requirements

Before any work begins or data is shared, appropriate agreements must be in place.

### 4.1 Master Services Agreement (MSA)
All vendors providing services must sign Nexora's standard MSA or an equivalent vendor-provided agreement reviewed and approved by Legal. Key required provisions include:
- Scope of authorized activities
- Confidentiality and non-disclosure obligations
- Intellectual property ownership
- Liability limitations and indemnification
- Audit rights for Nexora
- Termination rights

### 4.2 Data Processing Agreement (DPA)
A DPA is required for any vendor that processes personal data on Nexora's behalf. The DPA must comply with applicable data protection law (CCPA, GDPR where applicable) and specify:
- Categories of personal data processed
- Processing purposes and instructions
- Sub-processor obligations and approval process
- Data security requirements
- Breach notification obligations (vendor must notify Nexora within 24 hours of discovery)
- Data return and deletion upon contract termination

### 4.3 Information Security Addendum (ISA)
Tier 1 and Tier 2 vendors must execute Nexora's Information Security Addendum, which requires the vendor to:
- Maintain an information security program appropriate to the sensitivity of data handled
- Implement encryption in transit and at rest for Nexora data
- Comply with Nexora's access control requirements for vendor employees accessing Nexora systems
- Promptly notify Nexora of security incidents involving Nexora data
- Submit to annual security assessments or provide third-party audit reports

### 4.4 Non-Disclosure Agreement (NDA)
An NDA is required before sharing any Confidential or Restricted Nexora information during vendor evaluation. Nexora's standard NDA is managed by Legal and available in the Procurement portal.

---

## 5. Vendor Onboarding

After contracts are executed and approvals are complete, the Procurement team coordinates onboarding:

- IT Security provisions vendor access per the Access Control Policy (time-limited, least-privilege)
- Vendor contacts are registered in Nexora's vendor directory in Workday
- A primary business owner and a secondary owner are designated for each vendor relationship
- Tier 1 and Tier 2 vendors are added to the quarterly vendor review calendar
- Vendors accessing Nexora offices or physical facilities are issued temporary access credentials through Facilities

Vendor employees who need system access must each have individual named accounts. Shared vendor accounts are prohibited.

---

## 6. Ongoing Vendor Management

### 6.1 Performance Monitoring
Business owners are responsible for monitoring vendor performance against agreed service levels and contract terms. Material performance issues must be documented and escalated to Procurement and Legal.

### 6.2 Periodic Risk Reviews

| Tier | Review Frequency | Review Type |
|------|-----------------|-------------|
| Tier 1 | Annual | Full due diligence refresh + site visit or audit |
| Tier 2 | Annual | Questionnaire + updated SOC 2 report |
| Tier 3 | Every 2 years | Basic renewal check |

The CISO and Procurement Lead must jointly approve the continuation of any Tier 1 vendor relationship following an annual review.

### 6.3 Change Notification
Vendors must notify Nexora's business owner and Procurement team in advance of any material changes that may affect the services or security posture, including:
- Change in ownership or corporate structure
- Material changes to security controls or architecture
- Changes in sub-processors handling Nexora data
- Security incidents or breaches involving Nexora data

Nexora reserves the right to re-assess or terminate a vendor relationship based on material changes.

### 6.4 Sub-Processors
Tier 1 and Tier 2 vendors must disclose all sub-processors who will handle Nexora data. Nexora must approve new sub-processors before they are engaged. Vendors must update their sub-processor list and notify Nexora at least 30 days before adding a new sub-processor.

---

## 7. Vendor Offboarding

When a vendor relationship ends—whether by contract expiration, termination, or non-renewal—the business owner must trigger the offboarding process in the Procurement portal at least 30 days before the contract end date.

Offboarding steps:
1. IT Security revokes all vendor system access within 1 business day of the contract end date
2. Facilities deactivates vendor physical access credentials
3. Vendor must confirm in writing (within 30 days of termination) that all Nexora data has been returned or securely deleted
4. Legal retains a copy of the terminated contract and offboarding confirmation for 7 years
5. Vendor is marked inactive in Nexora's vendor directory

---

## 8. Prohibited Vendor Practices

The following practices are prohibited:
- Engaging a vendor before completing the approval process
- Sharing Restricted data with any vendor that has not executed a DPA and ISA
- Allowing vendors to store Nexora data in unapproved locations (e.g., personal accounts)
- Accepting gifts from vendors exceeding the $75 limit described in the Code of Conduct
- Allowing vendor personnel unescorted access to Nexora facilities
- Renewing vendor contracts without completing the required periodic review

---

## 9. Exceptions

Exceptions to this policy for urgent business needs may be granted by the VP of the relevant function, the CISO, and Legal, with a documented business justification and compensating controls. All exceptions are time-limited (maximum 90 days) and must be reviewed before renewal.

---

## 10. Policy Ownership and Review

This policy is owned by the Procurement function and reviewed annually by Procurement, IT Security, Legal, and Finance. The current version is available at wiki.nexora-internal.com/legal/vendor-management-policy.

---

*Last reviewed: December 2025*
*Document owner: VP of Finance (Procurement)*
*Approved by: CFO, CISO, General Counsel*
