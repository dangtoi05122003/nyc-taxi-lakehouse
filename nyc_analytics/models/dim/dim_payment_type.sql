SELECT 1 AS payment_type, 'Credit Card' AS description, TRUE AS is_valid UNION ALL
SELECT 2, 'Cash', TRUE UNION ALL
SELECT 3, 'No Charge', TRUE UNION ALL
SELECT 4, 'Dispute', TRUE UNION ALL
SELECT 5, 'Unknown', TRUE UNION ALL
SELECT -1, 'Missing', TRUE