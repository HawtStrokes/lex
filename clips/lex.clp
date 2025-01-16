(load "templates/business-entity.clp")
(load "templates/tax-data.clp")
(load "templates/employee.clp")
(load "templates/contract.clp")
(load "templates/real-estate.clp")
;; (load "templates/environmental.clp")

;; Batch rules
(batch "rules/business-rules.clp")
(batch "rules/tax-rules.clp")
(batch "rules/labor-rules.clp")
(batch "rules/contract-rules.clp")
(batch "rules/real-estate-rules.clp")
;; (batch "rules/environmental-rules.clp")

;; Batch global rules
(batch "globals/global-rules.clp")
(batch "globals/common-functions.clp")

;; Batch sample facts
(batch "facts/sample-facts.clp")

