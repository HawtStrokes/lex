from flask import Blueprint, render_template, request, jsonify
from .utils.inference_engine import generate_clips_facts, run_inference, initialize_inference_engine

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Retrieve user input from the form and ensure numeric fields are cast properly
        business_name = request.form["business_name"]
        business_type = request.form["business_type"]
        business_status = request.form["business_status"]
        
        # Convert to float for numeric fields
        try:
            income = float(request.form["income"])
        except ValueError:
            income = 0.0  # Default to 0.0 if the value cannot be converted

        try:
            deductions = float(request.form["deductions"])
        except ValueError:
            deductions = 0.0  # Default to 0.0 if the value cannot be converted

        try:
            tax_rate = float(request.form["tax_rate"])
        except ValueError:
            tax_rate = 0.0  # Default to 0.0 if the value cannot be converted

        # Employee fields
        employee_name = request.form["employee_name"]
        position = request.form["position"]
        try:
            salary = float(request.form["salary"])
        except ValueError:
            salary = 0.0  # Default to 0.0 if the value cannot be converted

        # Contract fields
        contract_terms = request.form["contract_terms"]
        parties = request.form["parties"]
        duration = request.form["duration"]
        
        # Real estate fields
        property_name = request.form["property_name"]
        property_type = request.form["property_type"]
        owner = request.form["owner"]

        # Prepare the data in a structured format
        data = [
            {
                "type": "business-entity",
                "attributes": {
                    "name": business_name,
                    "type": business_type,
                    "status": business_status
                }
            },
            {
                "type": "tax-data",
                "attributes": {
                    "income": income,
                    "deductions": deductions,
                    "tax-rate": tax_rate
                }
            },
            {
                "type": "employee",
                "attributes": {
                    "name": employee_name,
                    "position": position,
                    "salary": salary
                }
            },
            {
                "type": "contract",
                "attributes": {
                    "terms": contract_terms,
                    "parties": parties,
                    "duration": duration
                }
            },
            {
                "type": "real-estate",
                "attributes": {
                    "property-name": property_name,
                    "property-type": property_type,
                    "owner": owner
                }
            }
        ]

        # Generate CLIPS facts
        facts_file = generate_clips_facts(data)

        # Initialize the inference engine with the facts file
        env = initialize_inference_engine(facts_file)

        # Run the inference engine
        inference_result = run_inference(env)
        print("Captured Inference Output:", inference_result)  # Debugging step
        # Return the results to the template (you can change this based on your preferred display method)
        return render_template("inference_result.html", result=inference_result)

    return render_template("index.html")


