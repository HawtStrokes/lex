(deftemplate tax-data
   (slot entity-id) ;; Links to business-entity
   (slot income)
   (slot expenses)
   (slot taxable-income)
   (slot tax-credits)
   (slot vat-status) ;; VAT registered, Non-VAT registered
   (slot tax-rate)
   (slot penalties)
   (slot deductions)
   (slot payment-history)) ;; Dates of previous tax payments
 
