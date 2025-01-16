(defrule property-ownership
   (real-estate (property-name ?property-name) (property-type ?property-type) (owner ?owner))
   =>
   (printout t "Property: " ?property-name ", Type: " ?property-type ", Owner: " ?owner crlf)
)
