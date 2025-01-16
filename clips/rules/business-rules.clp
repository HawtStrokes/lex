(defrule business-entity-rule
   (business-entity (name ?name) (type ?type) (status ?status))
   =>
   (printout t "Business Entity: " ?name " of type " ?type " is currently " ?status crlf)
)
