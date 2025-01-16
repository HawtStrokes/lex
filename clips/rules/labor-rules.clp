(defrule employee-salary
   (employee (name ?name) (position ?position) (salary ?salary))
   =>
   (printout t "Employee: " ?name ", Position: " ?position ", Salary: " ?salary crlf)
)
