import time
from attack_surface_mapper.modules import execute_modules
from attack_surface_mapper.risk_engine import calculate_risk


def run_attack_surface(domain, selected_modules):

    start = time.time()

    report = {

        "target": domain,

        "started": time.strftime("%d-%m-%Y %H:%M:%S"),

        "selected_modules": selected_modules,

        "modules_requested": len(selected_modules),

        "modules_completed": 0,

        "modules": {},

        "findings": [],

        "recommendations": [],

        "risk": {

            "score": 0,

            "grade": "Unknown",

            "severity": "Unknown"

        }

    }

    report["modules"] = execute_modules(
        domain,
        selected_modules
    )

    report["modules_completed"] = len(
        report["modules"]
    )
    risk = calculate_risk(report)

    report["risk"]["score"] = risk["score"]

    report["risk"]["severity"] = risk["severity"]

    report["findings"] = risk["findings"]

    report["recommendations"] = risk["recommendations"]

    report["duration"] = round(
        time.time() - start,
        2
    )

    return report