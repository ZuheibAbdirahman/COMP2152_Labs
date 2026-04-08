# lab12_q2_starter.py

class Finding:
    """Represents a security finding with severity level"""
    
    def __init__(self, title, severity):
        """Initialize finding with title and severity (1-5, 5 is highest)"""
        self.title = title
        self.severity = severity
    
    def __eq__(self, other):
        """TODO: Implement equality comparison (==)
        Two findings are equal if they have the SAME severity level
        """
        if not isinstance(other, Finding):
            return False
        return self.severity == other.severity
    
    def __lt__(self, other):
        """TODO: Implement less-than comparison (<)
        This enables sorting with sorted()
        One finding is less than another if its severity is LOWER
        """
        if not isinstance(other, Finding):
            return NotImplemented
        return self.severity < other.severity
    
    def __repr__(self):
        """String representation for debugging"""
        return f"Finding('{self.title}', {self.severity})"
    
    def __str__(self):
        """User-friendly string representation"""
        severity_label = {1: "LOW", 2: "MEDIUM-LOW", 3: "MEDIUM", 
                          4: "HIGH", 5: "CRITICAL"}.get(self.severity, "UNKNOWN")
        return f"{self.title} [{severity_label}]"

class Report:
    """Collection of findings"""
    
    def __init__(self, name):
        """Initialize report with a name"""
        self.name = name
        self.findings = []
    
    def add_finding(self, finding):
        """Add a finding to the report"""
        self.findings.append(finding)
    
    def __len__(self):
        """TODO: Implement len() support
        Should return the number of findings in the report
        """
        return len(self.findings)
    
    def __add__(self, other):
        """TODO: Implement merging with + operator
        Should create a NEW Report that contains findings from BOTH reports
        The new report name should be f"{self.name} + {other.name}"
        """
        if not isinstance(other, Report):
            return NotImplemented
        
        merged_report = Report(f"{self.name} + {other.name}")
        merged_report.findings = self.findings.copy()  # Copy findings from self
        merged_report.findings.extend(other.findings)  # Add findings from other
        return merged_report
    
    def __repr__(self):
        """String representation for debugging"""
        return f"Report('{self.name}', {len(self.findings)} findings)"
    
    def __str__(self):
        """User-friendly string representation"""
        output = f"\n{'='*50}\nReport: {self.name}\n{'='*50}\n"
        if not self.findings:
            output += "No findings in this report.\n"
        else:
            for i, finding in enumerate(self.findings, 1):
                output += f"{i}. {finding}\n"
        return output

# Test the classes
if __name__ == "__main__":
    print("=" * 50)
    print("Q2: Dunder Methods Test")
    print("=" * 50)
    
    # Test Finding __eq__ and __lt__
    print("\n--- Testing Finding Comparisons ---")
    finding1 = Finding("SQL Injection", 5)  # CRITICAL
    finding2 = Finding("XSS Vulnerability", 3)  # MEDIUM
    finding3 = Finding("Buffer Overflow", 5)  # CRITICAL
    
    print(f"finding1 == finding2: {finding1 == finding2}")  # Should be False
    print(f"finding1 == finding3: {finding1 == finding3}")  # Should be True (both severity 5)
    print(f"finding2 < finding1: {finding2 < finding1}")    # Should be True (3 < 5)
    
    # Test sorting findings
    print("\n--- Testing Finding Sorting (LOW to HIGH) ---")
    findings_list = [
        Finding("Remote Code Execution", 5),
        Finding("Information Disclosure", 2),
        Finding("CSRF", 4),
        Finding("Weak Password Policy", 1),
        Finding("Missing Security Headers", 3)
    ]
    
    print("Original order:")
    for f in findings_list:
        print(f"  {f}")
    
    sorted_findings = sorted(findings_list)  # Uses __lt__
    print("\nSorted by severity (LOW to HIGH):")
    for f in sorted_findings:
        print(f"  {f}")
    
    # Test Report __len__
    print("\n--- Testing Report __len__ ---")
    report1 = Report("Daily Scan Report")
    report1.add_finding(finding1)
    report1.add_finding(finding2)
    report1.add_finding(finding3)
    
    print(f"Report has {len(report1)} findings")  # Should be 3
    
    # Test Report __add__ (merging)
    print("\n--- Testing Report __add__ (Merging) ---")
    report2 = Report("Weekly Summary")
    report2.add_finding(Finding("Open S3 Bucket", 4))
    report2.add_finding(Finding("Hardcoded Credentials", 5))
    
    print("Report 1:")
    print(report1)
    print("Report 2:")
    print(report2)
    
    merged_report = report1 + report2  # Uses __add__
    print("Merged Report:")
    print(merged_report)
    print(f"Merged report has {len(merged_report)} findings")  # Should be 5