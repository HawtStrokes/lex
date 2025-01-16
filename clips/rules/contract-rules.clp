(defrule contract-terms
   (contract (terms ?terms) (parties ?parties) (duration ?duration))
   =>
   (printout t "Contract: Terms = " ?terms ", Parties = " ?parties ", Duration = " ?duration crlf)
)
