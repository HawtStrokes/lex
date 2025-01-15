;; Declare facts and templates for user inputs
(deftemplate organization
   (slot name)
   (slot type) ;; e.g., "Filipino" or "foreign"
   (slot practice)) ;; e.g., "fair" or "unfair"

(deftemplate land-ownership
   (slot owner-type) ;; e.g., "Filipino" or "foreign"
   (slot percentage-owned)) ;; Percentage owned by Filipinos

(deftemplate contract
   (slot status)) ;; e.g., "valid" or "impaired"

(deftemplate taxation
   (slot type)) ;; e.g., "uniform", "progressive", etc.

;; Define rules
(defrule protect-filipino-enterprises
   (organization (type "Filipino") (practice "unfair"))
   =>
   (printout t "Action: Protect Filipino enterprises from unfair foreign competition." crlf))

(defrule promote-filipino-labor
   (organization (type "Filipino"))
   =>
   (printout t "Action: Promote the preferential use of Filipino labor, materials, and goods." crlf))

(defrule enforce-land-ownership
   (land-ownership (owner-type "foreign") (percentage-owned ?percent&:(< ?percent 60)))
   =>
   (printout t "Violation: Land ownership is restricted to Filipinos or corporations with at least 60% Filipino ownership." crlf))

(defrule uphold-contracts
   (contract (status "impaired"))
   =>
   (printout t "Violation: No law shall impair the obligation of contracts." crlf))

(defrule ensure-uniform-taxation
   (taxation (type "non-uniform"))
   =>
   (printout t "Violation: Taxation must be uniform and equitable." crlf))

(defrule ensure-progressive-taxation
   (taxation (type "non-progressive"))
   =>
   (printout t "Recommendation: Congress should evolve a progressive taxation system." crlf))

