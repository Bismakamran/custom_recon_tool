from datetime import datetime
import os

def save_report(domain, report_data, format="txt"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/{domain}_{timestamp}.{format}"
    os.makedirs("reports", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(report_data)

    print(f"✅ {format.upper()} report saved to: {filename}")

def generate_html_report(domain, report_data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = report_data.strip().splitlines()
    if not lines:
        print("❌ No report data to render.")
        return

    # Extract core details
    domain_val, ip_val, time_val = "", "", ""
    for line in lines:
        if line.startswith("Target Domain"):
            domain_val = line.split(":", 1)[1].strip()
        elif line.startswith("Resolved IP"):
            ip_val = line.split(":", 1)[1].strip()
        elif line.startswith("Timestamp"):
            time_val = line.split(":", 1)[1].strip()

    # Parse sections
    html_sections = ""
    current_title = None
    current_content = []
    parsed_data = {}

    for line in lines:
        if line.strip().startswith("[") and line.strip().endswith("]"):
            if current_title:
                section_content = "\n".join(current_content)
                html_sections += _wrap_collapsible(current_title, section_content)
                parsed_data[current_title] = current_content.copy()
            current_title = line.strip("= []").strip()
            current_content = []
        elif current_title:
            current_content.append(line)

    if current_title:
        section_content = "\n".join(current_content)
        html_sections += _wrap_collapsible(current_title, section_content)
        parsed_data[current_title] = current_content.copy()

    chart_script = _generate_chart_script(parsed_data)

    # HTML Template
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Recon Report for {domain_val or domain}</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{
            font-family: 'Segoe UI', sans-serif;
            background-color: #f4f4f4;
            padding: 30px;
        }}
        .container {{
            max-width: 950px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            margin-bottom: 10px;
        }}
        .meta p {{
            margin: 5px 0;
            color: #555;
        }}
        details {{
            margin-top: 20px;
            border: 1px solid #ccc;
            border-radius: 6px;
            padding: 10px;
            background-color: #f9f9f9;
        }}
        summary {{
            font-weight: bold;
            font-size: 15px;
            cursor: pointer;
            outline: none;
        }}
        pre {{
            background: #f0f0f0;
            padding: 15px;
            overflow-x: auto;
            white-space: pre-wrap;
            border-radius: 5px;
            margin: 0;
        }}
        canvas {{
            margin-top: 30px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Reconnaissance Report</h1>
        <div class="meta">
            <p><b>Target Domain:</b> {domain_val or domain}</p>
            <p><b>Resolved IP:</b> {ip_val}</p>
            <p><b>Generated:</b> {time_val or timestamp}</p>
        </div>
        <canvas id="chart" width="800" height="300"></canvas>
        {html_sections or "<p>No module results available.</p>"}
    </div>
    <script>
        {chart_script}
    </script>
</body>
</html>
"""

    filename = f"reports/{domain}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ HTML report saved to: {filename}")

def _wrap_collapsible(title, content):
    return f"""
<details>
    <summary>{title}</summary>
    <pre>{content}</pre>
</details>
"""

def _generate_chart_script(parsed_data):
    module_counts = {
        section: len([line for line in lines if line.strip()])
        for section, lines in parsed_data.items()
    }

    labels = list(module_counts.keys())
    values = list(module_counts.values())

    return f"""
    const ctx = document.getElementById('chart').getContext('2d');
    new Chart(ctx, {{
        type: 'bar',
        data: {{
            labels: {labels},
            datasets: [{{
                label: 'Entries per Module',
                data: {values},
                backgroundColor: 'rgba(54, 162, 235, 0.6)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }}]
        }},
        options: {{
            responsive: true,
            scales: {{
                y: {{
                    beginAtZero: true,
                    ticks: {{
                        precision: 0
                    }}
                }}
            }}
        }}
    }});
    """
