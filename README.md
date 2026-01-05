# 🔐 Security Scan GitHub Actions Workflow

This repository uses an automated **Security Scan GitHub Actions workflow** to enforce code quality, security, and infrastructure best practices across all environments.

The workflow integrates multiple industry‑standard tools (SonarQube, Bandit, Trivy, Hadolint, Terraform + Checkov) and posts **inline PR comments** and a **single up‑to‑date summary report** on every Pull Request.

---

## 📌 Purpose

The Security Scan workflow ensures that:

* Vulnerabilities and misconfigurations are detected **early**
* Only reviewed and scanned code reaches **develop**, **uat**, and **main**
* Developers get **actionable feedback directly on changed lines** in PRs

---

## 🌳 Branching Strategy (Simplified GitFlow)

```
main     → Production (stable, release‑ready)
  ↑
uat      → User Acceptance Testing
  ↑
develop  → Integration branch
  ↑
feature/* → Individual tasks / features
```

### Allowed PR Flows

| Source Branch | Target Branch | Purpose             |
| ------------- | ------------- | ------------------- |
| feature/*     | develop       | Feature development |
| develop       | uat           | UAT promotion       |
| uat           | main          | Production release  |

🚫 Direct commits to `main`, `uat`, or `develop` are not allowed.

---

## ⚙️ When the Workflow Runs

The workflow triggers **only on Pull Requests**:

```yaml
on:
  pull_request:
    types: [opened, synchronize, reopened]
```

### Job‑level Conditions

```yaml
if: |
  (startsWith(github.head_ref, 'feature/') && github.base_ref == 'develop') ||
  (github.head_ref == 'develop' && github.base_ref == 'uat') ||
  (github.head_ref == 'uat' && github.base_ref == 'main')
```

This enforces the branching rules directly in CI.

---

## 🔑 Permissions Used

```yaml
permissions:
  contents: read
  pull-requests: write
  id-token: write
```

| Permission           | Why it’s needed                |
| -------------------- | ------------------------------ |
| contents: read       | Read repository files          |
| pull-requests: write | Post inline comments & summary |
| id-token: write      | Assume AWS IAM role via OIDC   |

---

## 🧰 Tools Used in the Pipeline

| Tool          | Purpose                                  |
| ------------- | ---------------------------------------- |
| **SonarQube** | Static code analysis & code quality      |
| **Bandit**    | Python security vulnerability scanning   |
| **Trivy**     | Dockerfile misconfiguration scanning     |
| **Hadolint**  | Dockerfile linting                       |
| **Terraform** | Infrastructure planning                  |
| **Checkov**   | Terraform security & compliance scanning |

---

## 🛠️ Workflow Steps (High Level)

### 1️⃣ Setup

* Checkout repository
* Configure AWS credentials using GitHub OIDC
* Install required CLI tools (`jq`, `curl`, `wget`)

---

### 2️⃣ SonarQube – Static Analysis

* Installs SonarScanner CLI
* Runs scan using `sonar-project.properties`
* Fetches issues via SonarQube REST API
* Saves results to `sonar_issues.json`

**Reported as:**

* Inline PR comments
* Summary + detailed report section

---

### 3️⃣ Bandit – Python Security Scan

```bash
bandit -r . -f json -o bandit-report.json
```

* Scans Python files recursively
* Detects insecure coding patterns

---

### 4️⃣ Trivy – Dockerfile Scan

```bash
trivy config --severity HIGH,CRITICAL Dockerfile
```

* Detects Docker misconfigurations
* Focuses on HIGH and CRITICAL severity

---

### 5️⃣ Hadolint – Dockerfile Linting

* Validates Dockerfile best practices
* Outputs structured JSON for reporting

---

### 6️⃣ Terraform + Checkov (Conditional)

Runs **only if a `Terraform/` folder exists**.

#### Terraform Steps

* `terraform init`
* `terraform plan`
* Convert plan to JSON

#### Environment Selection

| PR Type           | TFVARS      |
| ----------------- | ----------- |
| feature → develop | dev.tfvars  |
| develop → uat     | dev.tfvars  |
| uat → main        | prod.tfvars |

#### Checkov

* Scans Terraform plan JSON
* Detects cloud security misconfigurations

---

## 📄 Reporting

### 🔍 report.md

A single markdown report is generated containing:

* Summary of failures per tool
* Detailed findings with:

  * File paths
  * Line numbers
  * Severity
  * Direct GitHub links

---

## 💬 PR Feedback

### Inline Review Comments

* Posted only on **lines present in the PR diff**
* Batched and rate‑limit safe
* Covers all tools (SonarQube, Bandit, Trivy, Hadolint, Checkov)

### Summary Comment

* One reusable PR comment
* Automatically updated on every workflow run
* Contains full `report.md`

---

## 👨‍💻 Developer Responsibilities

Before merging any PR:

✅ Ensure **Security Scan workflow passes**

✅ Review:

* Inline comments on files
* Summary report comment

✅ Fix all valid findings

⚠️ If a finding cannot be fixed:

* Add a **clear justification comment** (false positive / accepted risk / follow‑up ticket)
* Get team approval before merging

---

## 🚀 Merge Rules

A PR can be merged **only if**:

* Security Scan completed
* Issues are fixed or explicitly justified
* Code review approvals are met

---

## 🧠 Key Takeaway

> **This pipeline acts as an automated security reviewer.**
> If it comments on your PR, read it carefully — it’s protecting production.

---

✅ *This README documents the complete Security Scan workflow and developer expectations.*
