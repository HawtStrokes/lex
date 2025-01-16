(deftemplate log
   (slot message))

(defrule logging-rule
   ?log <- (log (message ?message))
   =>
   (printout t "Log: " ?message crlf))

