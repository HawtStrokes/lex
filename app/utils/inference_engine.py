import clips

def initialize_inference_engine():
    # Initialize the CLIPS environment
    env = clips.Environment()

    # Load templates
    env.load('templates/business-entity.clp')
    env.load('templates/tax-data.clp')
    env.load('templates/employee.clp')
    env.load('templates/contract.clp')
    env.load('templates/real-estate.clp')
    # env.load('templates/environmental.clp')  # Uncomment if needed

    # Load rules
    env.batch_star('rules/business-rules.clp')
    env.batch_star('rules/tax-rules.clp')
    env.batch_star('rules/labor-rules.clp')
    env.batch_star('rules/contract-rules.clp')
    env.batch_star('rules/real-estate-rules.clp')
    # env.batch_star('rules/environmental-rules.clp')  # Uncomment if needed

    # Load global rules
    env.batch_star('globals/global-rules.clp')
    env.batch_star('globals/common-functions.clp')

    # Load sample facts
    env.batch_star('facts/sample-facts.clp')

    return env

def run_inference(env):
    # Run the inference engine
    env.run()

if __name__ == "__main__":
    # Initialize the inference engine
    env = initialize_inference_engine()

    # Run the inference engine
    run_inference(env)

