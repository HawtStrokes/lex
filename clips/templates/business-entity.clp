(deftemplate business-entity
   (slot name)
   (slot type) ;; e.g., Corporation, Partnership
   (slot status) ;; e.g., Active, Inactive
   (slot tax-id) ;; TIN or other identifiers
   (slot ownership) ;; Filipino, Foreign, Mixed
   (slot primary-industry) ;; Retail, IT, etc.
   (slot location) ;; Address
   (slot date-established)) ;; Date of registration

