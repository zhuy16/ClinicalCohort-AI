-- Example cohort definition: Type 2 diabetes (ICD-10 E11%)
-- Customize the WHERE clause and icd10_code prefix for your disease/condition of interest
CREATE OR REPLACE VIEW t2d_patients AS
SELECT DISTINCT patient_id
FROM conditions
WHERE icd10_code LIKE 'E11%';
