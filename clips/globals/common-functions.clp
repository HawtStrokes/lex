(deffunction calculate-tax (?income ?deductions ?rate)
   (- (* (- ?income ?deductions) ?rate) 0))

