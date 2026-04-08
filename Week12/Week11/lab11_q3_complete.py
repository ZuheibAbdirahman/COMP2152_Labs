# lab11_q3_complete.py

class Finding:
    """Represents a single vulnerability finding"""
    
    def __init__(self, target, severity, description):
        """Initialize a finding with target, severity, and description"""
        self.target = target
        self.severity = severity  # HIGH, MEDIUM, or LOW
        self.description = description
    
    def __str__(self):
        """String representation of the finding"""
        return f"[{self.severity}] {self.target} — {self.description}"


class Report:
    """Collects and manages multiple vulnerability findings"""
    
    def __init__(self, team_name):
        """Initialize a report with a team name"""
        self.team_name = team_name
        self.findings = []
    
    def add_finding(self, finding):
        """Add a finding to the report"""
        self.findings.append(finding)
        print(f"  Added: {finding}")
    
    def get_by_severity(self, severity):
        """Return list of findings with the specified severity"""
        return [f for f in self.findings if f.severity == severity]
    
    def summary(self):
        """Print a formatted summary of the report"""
        print(f"Team: {self.team_name}")
        print(f"Total findings: {len(self.findings)}")
        
        # Count by severity
        high_count = len(self.get_by_severity("HIGH"))
        medium_count = len(self.get_by_severity("MEDIUM"))
        low_count = len(self.get_by_severity("LOW"))
        
        print(f"HIGH:   {high_count}")
        print(f"MEDIUM: {medium_count}")
        print(f"LOW:    {low_count}")
        print("-" * 40)
        
        # Print each finding
        for finding in self.findings:
            print(finding)


def main():
    print("=" * 60)
    print("  Q3: VULNERABILITY REPORT")
    print("=" * 60)
    print()
    
    # Create a report
    report = Report("CyberHunters")
    
    # Create some findings
    findings = [
        Finding("ssh.0x10.cloud", "HIGH", "Default credentials admin:admin"),
        Finding("blog.0x10.cloud", "LOW", "No HTTPS (cleartext)"),
        Finding("ftp.0x10.cloud", "HIGH", "Anonymous FTP access"),
        Finding("api.0x10.cloud", "MEDIUM", "Server version exposed in headers"),
        Finding("cdn.0x10.cloud", "LOW", "Missing security headers")
    ]
    
    # Add findings to report
    print("--- Adding Findings ---")
    for f in findings:
        report.add_finding(f)
    
    print()
    print("--- Full Report ---")
    report.summary()
    
    print()
    print("--- HIGH Severity Only ---")
    high_severity = report.get_by_severity("HIGH")
    for finding in high_severity:
        print(finding)
    
    print()
    print("=" * 60)


if __name__ == "__main__":
    main()