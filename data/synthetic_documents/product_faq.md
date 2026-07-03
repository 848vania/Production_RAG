# Product FAQ — Nexora FlowOps Platform
**Nexora Technologies, Inc.**
**Version 1.8 | Last Updated: March 2026**

---

## Overview

This document provides answers to frequently asked questions about the Nexora FlowOps platform. FlowOps is Nexora's core product: a B2B financial operations automation platform that helps mid-market and enterprise companies automate accounts payable, accounts receivable, and procurement workflows.

This FAQ is intended for internal use by Sales, Customer Success, and Support teams.

---

## General Product Questions

### What is Nexora FlowOps?
FlowOps is a cloud-native financial operations automation platform. It connects to a company's ERP, accounting software, and banking systems to automate manual workflows such as invoice processing, payment approvals, vendor onboarding, and reconciliation. Key capabilities include:
- AI-powered invoice data extraction and coding
- Configurable multi-step approval workflows
- Real-time payment execution (ACH, wire, virtual card)
- Vendor portal for self-service document submission
- Analytics dashboards and audit trails

### Who is FlowOps designed for?
FlowOps is designed for mid-market companies (100–2,500 employees) and enterprise organizations with complex AP/AR workflows. Target buyers include CFOs, Controllers, VP of Finance, and Director of AP/AR. The platform is particularly well-suited for companies processing more than 500 invoices per month.

### What ERP systems does FlowOps integrate with?
FlowOps has certified, out-of-the-box integrations with:
- NetSuite (Oracle)
- SAP S/4HANA and SAP Business One
- Microsoft Dynamics 365 Finance
- Sage Intacct
- QuickBooks Online (mid-market edition)
- Workday Financial Management

Custom integrations via the FlowOps REST API are available for customers on the Enterprise tier. Integration setup typically takes 2–4 weeks depending on complexity.

### Is FlowOps cloud-based or on-premise?
FlowOps is 100% cloud-based, hosted on AWS in US-East and US-West regions (with EU-West-1 available for customers with EU data residency requirements). There is no on-premise deployment option at this time.

### What is FlowOps' uptime SLA?
FlowOps guarantees 99.9% uptime (excluding scheduled maintenance) on Standard and Professional tiers and 99.95% uptime on the Enterprise tier. Scheduled maintenance is communicated at least 72 hours in advance and occurs between 11:00 PM and 3:00 AM CT on weekends. Current and historical uptime is available at status.nexoratech.com.

---

## Pricing and Plans

### What pricing tiers are available?
FlowOps is available in three tiers:

| Tier | Target Company Size | Starting Price |
|------|--------------------|--------------------|
| Standard | 100–300 employees | $2,500/month |
| Professional | 300–1,000 employees | $6,500/month |
| Enterprise | 1,000+ employees | Custom (contact Sales) |

All tiers are priced annually. Monthly billing is available at a 15% premium on Standard and Professional tiers.

### What is included in each tier?

| Feature | Standard | Professional | Enterprise |
|---------|----------|--------------|------------|
| Invoice processing (AI extraction) | ✓ | ✓ | ✓ |
| Approval workflows | Up to 5 | Up to 20 | Unlimited |
| ERP integrations | 1 | 3 | Unlimited |
| Payment methods (ACH, wire) | ACH only | ACH + wire | ACH + wire + virtual card |
| Vendor portal | ✓ | ✓ | ✓ |
| Analytics & reporting | Standard | Advanced | Custom |
| API access | Read-only | Full | Full + webhooks |
| Dedicated CSM | ✗ | ✓ | ✓ |
| SSO/SAML | ✗ | ✓ | ✓ |
| Data residency options | US only | US only | US or EU |
| SLA | 99.9% | 99.9% | 99.95% |
| Support | Email | Email + chat | 24/7 phone |

### Are there implementation fees?
Yes. Implementation fees depend on tier and complexity:
- Standard: $3,000–$6,000 (3–4 week implementation)
- Professional: $8,000–$20,000 (6–10 week implementation)
- Enterprise: Custom (10–20+ weeks; scoped separately)

Implementation is managed by Nexora's Professional Services team in collaboration with the customer's IT and Finance teams.

### Is there a free trial?
Yes. A 14-day free trial is available for the Professional tier, with access to all features except live payment execution. Trial accounts can process up to 50 invoices. No credit card is required to start a trial. Sales-assisted POC (proof of concept) environments are also available for Enterprise prospects.

---

## Features and Capabilities

### How does AI invoice extraction work?
FlowOps uses a proprietary large language model fine-tuned on financial documents to extract structured data from invoices in any format (PDF, image, email body). Extracted fields include vendor name, invoice number, invoice date, due date, line items, amounts, and tax information. Extraction accuracy on standard invoices exceeds 97%. The system flags low-confidence extractions for human review. Customers can train FlowOps on their specific vendor invoice formats to improve accuracy further.

### What payment methods does FlowOps support?
- **ACH** (Standard, Professional, Enterprise): Domestic US transfers, settlement in 1–3 business days. Same-day ACH available on Enterprise.
- **Wire transfers** (Professional, Enterprise): Domestic and international. USD and 12 foreign currencies supported.
- **Virtual cards** (Enterprise only): Single-use virtual Mastercard numbers issued per payment. Accepted by any merchant with a Mastercard terminal.

Payment execution requires a linked funding bank account and completion of KYB (Know Your Business) verification, which takes 1–3 business days.

### Can FlowOps handle multi-entity accounting?
Yes. Multi-entity support is available on Professional and Enterprise tiers. Each entity can have its own chart of accounts, approval workflows, bank accounts, and reporting. Consolidated reporting across entities is available on Enterprise.

### Does FlowOps support purchase orders (POs)?
Yes. FlowOps can match incoming invoices to open purchase orders using 2-way or 3-way matching (invoice + PO, or invoice + PO + receipt). PO matching is available on Professional and Enterprise tiers. PO data can be imported from the connected ERP or entered manually in FlowOps.

### How are approval workflows configured?
Approval workflows are configured in the FlowOps Workflow Builder (no-code). Workflows can be triggered by amount thresholds, vendor category, cost center, department, or any custom field. Approvers can be individuals, roles, or groups. Escalation rules (e.g., auto-approve after 48 hours of inactivity, escalate to manager after 24 hours) are configurable. Audit trails for all approval actions are maintained indefinitely.

### Is there a mobile app?
Yes. FlowOps has iOS and Android apps that allow approvers to review and approve/reject invoices and payments on the go. The mobile app supports biometric authentication (Face ID, fingerprint). Invoice data entry and configuration changes are not available on mobile.

### Does FlowOps support OCR for paper invoices?
Yes. Customers can submit physical invoices by scanning or photographing them and uploading to FlowOps via the web interface, mobile app, or email-to-invoice feature (a unique email address is provisioned per customer). OCR and AI extraction then process the invoice as normal.

---

## Security and Compliance

### Is FlowOps SOC 2 compliant?
Yes. Nexora maintains SOC 2 Type II certification covering Security, Availability, and Confidentiality trust service criteria. The most recent report is available under NDA to qualified prospects and customers. Request via your Customer Success Manager or securitydocs@nexoratech.com.

### Is FlowOps PCI DSS compliant?
FlowOps does not store full cardholder data. Virtual card numbers are tokenized and never stored in plaintext. Nexora is PCI DSS Level 1 certified for applicable card data handling. Certification documentation is available upon request.

### Does FlowOps support SSO?
SAML 2.0-based SSO is supported on Professional and Enterprise tiers and can be configured with any compliant identity provider (Okta, Azure AD, Google Workspace, Ping Identity). SSO setup is handled during implementation. SCIM provisioning for automated user lifecycle management is available on Enterprise.

### Where is data stored?
By default, all customer data is stored in AWS US-East-1 (Northern Virginia) with replication to US-West-2 (Oregon) for disaster recovery. Customers with EU data residency requirements can elect AWS EU-West-1 (Ireland) as their primary region on the Enterprise tier.

---

## Support

### How do I contact support?
- **Email** (all tiers): support@nexoratech.com
- **In-app chat** (Professional, Enterprise): Available during business hours (8 AM–8 PM CT)
- **Phone** (Enterprise): 1-888-NEX-SUPP, 24/7
- **Customer portal**: portal.nexoratech.com/support

### What are support response time SLAs?

| Severity | Definition | Standard | Professional | Enterprise |
|----------|-----------|----------|--------------|------------|
| P1 – Critical | Production down, no workaround | 4 hours | 2 hours | 30 minutes |
| P2 – High | Major feature unavailable | 8 hours | 4 hours | 2 hours |
| P3 – Medium | Feature impaired, workaround available | 2 business days | 1 business day | 4 hours |
| P4 – Low | General questions, feature requests | 3 business days | 2 business days | 1 business day |

### Does Nexora offer training?
Yes. FlowOps includes access to Nexora University (university.nexoratech.com) with self-paced video courses, role-based learning paths, and certification exams. Live virtual training sessions are included in Professional and Enterprise implementations. Onsite training is available for Enterprise customers at an additional fee.

---

*Last reviewed: March 2026*
*Document owner: Product Marketing*
*Contact: productfaq@nexora-internal.com*
