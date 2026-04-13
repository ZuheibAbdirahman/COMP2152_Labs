def bar_chart(data, title, max_width=30):
    print(f"\n{title}")
    print("-" * (max_width + 20))
    
    if isinstance(data, dict):
        data = list(data.items())
    
    if not data:
        print("No data to display")
        return
    
    max_value = max(count for _, count in data) if data else 1
    
    for label, count in data:
        if max_value > 0:
            bar_length = max(1, int((count / max_value) * max_width))
        else:
            bar_length = 0
        
        bar = "█" * bar_length
        print(f"{label:15} | {bar} {count}")
    
    print("-" * (max_width + 20))

def severity_summary(findings):
    severity_counts = {}
    for finding in findings:
        severity = finding.get("severity", "UNKNOWN")
        severity_counts[severity] = severity_counts.get(severity, 0) + 1
    
    priority_order = ["HIGH", "CRITICAL", "MEDIUM", "LOW"]
    sorted_severities = []
    for priority in priority_order:
        if priority in severity_counts:
            sorted_severities.append((priority, severity_counts[priority]))
    
    for severity, count in severity_counts.items():
        if severity not in priority_order:
            sorted_severities.append((severity, count))
    
    return sorted_severities

def timeline(findings):
    date_counts = {}
    for finding in findings:
        date = finding.get("date", "Unknown")
        date_counts[date] = date_counts.get(date, 0) + 1
    
    sorted_dates = sorted(date_counts.items(), key=lambda x: x[0])
    return sorted_dates

def create_sample_data():
    sample_data = [
        {"subdomain": "ssh.0x10.cloud", "type": "default_creds", "severity": "HIGH", "date": "2024-03-01"},
        {"subdomain": "admin.0x10.cloud", "type": "sql_injection", "severity": "CRITICAL", "date": "2024-03-01"},
        {"subdomain": "api.0x10.cloud", "type": "weak_ssl", "severity": "MEDIUM", "date": "2024-03-01"},
        {"subdomain": "ssh.0x10.cloud", "type": "open_port", "severity": "LOW", "date": "2024-03-02"},
        {"subdomain": "mail.0x10.cloud", "type": "default_creds", "severity": "HIGH", "date": "2024-03-02"},
        {"subdomain": "admin.0x10.cloud", "type": "weak_password", "severity": "HIGH", "date": "2024-03-02"},
        {"subdomain": "api.0x10.cloud", "type": "info_leak", "severity": "MEDIUM", "date": "2024-03-03"},
        {"subdomain": "ssh.0x10.cloud", "type": "bruteforce", "severity": "HIGH", "date": "2024-03-03"},
        {"subdomain": "db.0x10.cloud", "type": "default_creds", "severity": "CRITICAL", "date": "2024-03-03"},
        {"subdomain": "admin.0x10.cloud", "type": "xss", "severity": "MEDIUM", "date": "2024-03-04"},
        {"subdomain": "dev.0x10.cloud", "type": "weak_ssl", "severity": "LOW", "date": "2024-03-04"},
        {"subdomain": "dev.0x10.cloud", "type": "info_leak", "severity": "LOW", "date": "2024-03-05"},
        {"subdomain": "staging.0x10.cloud", "type": "default_creds", "severity": "CRITICAL", "date": "2024-03-05"},
        {"subdomain": "staging.0x10.cloud", "type": "sql_injection", "severity": "HIGH", "date": "2024-03-06"},
        {"subdomain": "api.0x10.cloud", "type": "weak_password", "severity": "MEDIUM", "date": "2024-03-06"},
    ]
    return sample_data

def main():
    findings = create_sample_data()
    
    print("=" * 60)
    print("SECURITY DASHBOARD - ASCII VISUALIZATION")
    print("=" * 60)
    
    print("\n" + "=" * 60)
    severity_data = severity_summary(findings)
    bar_chart(severity_data, "SEVERITY DISTRIBUTION (HIGH Priority First)", max_width=30)
    
    print("\n" + "=" * 60)
    timeline_data = timeline(findings)
    bar_chart(timeline_data, "FINDINGS TIMELINE (Chronological)", max_width=30)
    
    print("\n" + "=" * 60)
    type_counts = {}
    for finding in findings:
        vuln_type = finding.get("type", "Unknown")
        type_counts[vuln_type] = type_counts.get(vuln_type, 0) + 1
    
    sorted_types = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)
    bar_chart(sorted_types, "VULNERABILITY TYPE DISTRIBUTION", max_width=30)
    
    print("\n" + "=" * 60)
    print("DASHBOARD COMPLETE")
    print("=" * 60)
    
    print("\nSUMMARY STATISTICS:")
    print(f"Total Findings: {len(findings)}")
    print(f"Unique Subdomains: {len(set(f['subdomain'] for f in findings))}")
    print(f"Unique Vulnerability Types: {len(set(f['type'] for f in findings))}")
    print(f"Date Range: {min(f['date'] for f in findings)} to {max(f['date'] for f in findings)}")

if __name__ == "__main__":
    main()