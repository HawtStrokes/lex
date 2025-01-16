(defrule tax-calculation
   (tax-data (income ?income) (deductions ?deductions) (tax-rate ?tax-rate))
   =>
   (bind ?taxable-income (- ?income ?deductions))
   (bind ?tax ?taxable-income * ?tax-rate)
   (printout t "Calculated Tax: " ?tax crlf)
)
