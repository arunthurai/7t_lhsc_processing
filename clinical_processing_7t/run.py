import argparse
import subprocess
import yaml

CONFIG_FILE = "./config/config.yaml"

def load_config():
    """Load configuration values from config.yaml."""

    with open(CONFIG_FILE, "r") as file:
        return yaml.safe_load(file)

def get_parser():
    """Create an argument parser using values from config.yaml."""

    config = load_config()
    parse_args = config.get("parse_args", {})

    parser = argparse.ArgumentParser(description="Run the clinical_processing_7T workflow")

    # required arguments
    parser.add_argument("output_dir", help=parse_args.get("output_dir", {}).get("help", ""))
    parser.add_argument("cfmm_id", help=parse_args.get("cfmm_id", {}).get("help", ""))
    
    # optional grad coeff file
    parser.add_argument("--grad_coeffs", default=parse_args.get("grad_coeffs", {}).get("default", ""), help=parse_args.get("grad_coeffs", {}).get("help", ""))
    
    # snakemake arguments
    parser.add_argument("-np", action="store_true", help=parse_args.get("np", {}).get("help", ""))
    parser.add_argument("--use-singularity", action="store_true", help=parse_args.get("use-singularity", {}).get("help", ""))

    return parser

def main():
    
    """Main execution function."""
    parser = get_parser()
    args = parser.parse_args()

    output_dir = args.output_dir
    cfmm_id = args.cfmm_id
    grad_coeffs = args.grad_coeffs

    # make sure both required args are included
    if not output_dir or not cfmm_id:
        parser.error("Both output_dir and cfmm_id must be provided.")

    snakemake_command = [
        "snakemake",
        "--cores", "all",
        "--config",
        f"output_dir={output_dir}",
        f"cfmm_id={cfmm_id}",
        f"grad_coeffs={grad_coeffs}",
        "-np",
        "--use-singularity"
    ]

    subprocess.run(snakemake_command, check=True)

if __name__ == "__main__":
    main()



