# main.py
import subprocess
import sys
import os

# Paths to scripts
GEN_SCRIPT = os.path.join("scripts", "generate_prompts.py")
TEST_SCRIPT = os.path.join("scripts", "test_target.py")
REPORT_SCRIPT = os.path.join("scripts", "report_results.py")

def run(script):
    print(f"\n>>> Running: {script}\n")
    result = subprocess.run([sys.executable, script], capture_output=False)
    if result.returncode != 0:
        print(f"Script {script} failed with return code {result.returncode}")
        sys.exit(result.returncode)

if __name__ == "__main__":
    # 1) generate prompts
    run(GEN_SCRIPT)

    # 2) test prompts on vulnerable model
    run(TEST_SCRIPT)

    # 3) analyze and report
    run(REPORT_SCRIPT)

    print("\n=== Pipeline finished. Reports in prompts/report.csv and prompts/ai_responses.txt ===")
