import clips
import sys
import os
import logging
import tempfile

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def generate_clips_facts(data):
    facts = ""
    for item in data:
        fact = f"(assert ({item['type']} "
        for key, value in item['attributes'].items():
            fact += f"({key} \"{value}\") "
        fact += "))\n"
        facts += fact
    return facts

def initialize_inference_engine(facts):
    env = clips.Environment()
    # Define the base path for templates and rules
    base_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../clips'))
    logger.debug(f"Base path: {base_path}")

    # Define paths to templates, rules, and globals
    templates_path = os.path.join(base_path, 'templates')
    rules_path = os.path.join(base_path, 'rules')
    globals_path = os.path.join(base_path, 'globals')

    # Log the absolute paths
    logger.debug(f"Templates path: {templates_path}")
    logger.debug(f"Rules path: {rules_path}")
    logger.debug(f"Globals path: {globals_path}")

    # Load templates
    env.load(os.path.join(templates_path, 'business-entity.clp'))
    env.load(os.path.join(templates_path, 'tax-data.clp'))
    env.load(os.path.join(templates_path, 'employee.clp'))
    env.load(os.path.join(templates_path, 'contract.clp'))
    env.load(os.path.join(templates_path, 'real-estate.clp'))

    # Load rules
    env.batch_star(os.path.join(rules_path, 'business-rules.clp'))
    env.batch_star(os.path.join(rules_path, 'tax-rules.clp'))
    env.batch_star(os.path.join(rules_path, 'labor-rules.clp'))
    env.batch_star(os.path.join(rules_path, 'contract-rules.clp'))
    env.batch_star(os.path.join(rules_path, 'real-estate-rules.clp'))

    # Load global rules and functions
    env.batch_star(os.path.join(globals_path, 'global-rules.clp'))
    env.batch_star(os.path.join(globals_path, 'common-functions.clp'))

    # Write facts to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.clp') as temp_file:
        temp_file.write(facts)
        temp_file_path = temp_file.name
        logger.debug(f"Temporary facts file created at: {temp_file_path}")

    # Load facts from the temporary file
    env.batch_star(temp_file_path)
    return env

def run_inference(env):
    env.run()

if __name__ == "__main__":
    # Retrieve command-line arguments
    args = sys.argv[1:]

    # Ensure the correct number of arguments
    if len(args) != 15:
        print("Error: Expected 15 arguments.")
        sys.exit(1)

    # Parse the arguments
    business_name = args[0]
    business_type = args[1]
    business_status = args[2]
    income = float(args[3])
    deductions = float(args[4])
    tax_rate = float(args[5])
    employee_name = args[6]
    position = args[7]
    salary = float(args[8])
    contract_terms = args[9]
    parties = args[10]
    duration = args[11]
    property_name = args[12]
    property_type = args[13]
    owner = args[14]

    # Prepare the data
    data = [
        {'type': 'business-entity', 'attributes': {'name': business_name, 'type': business_type, 'status': business_status}},
        {'type': 'tax-data', 'attributes': {'income': income, 'deductions': deductions, 'tax-rate': tax_rate}},
        {'type': 'employee', 'attributes': {'name': employee_name, 'position': position, 'salary': salary}},
        {'type': 'contract', 'attributes': {'terms': contract_terms, 'parties': parties, 'duration': duration}},
        {'type': 'real-estate', 'attributes': {'property-name': property_name, 'property-type': property_type, 'owner': owner}}
    ]

    # Generate facts
    facts = generate_clips_facts(data)

    # Initialize the inference engine
    env = initialize_inference_engine(facts)

    # Run the inference engine
    run_inference(env)

