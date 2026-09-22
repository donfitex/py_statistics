CREATE DATABASE bincom_test;

-- After connecting to bincom_test, the application creates the table.
-- Verify saved data with:
SELECT colour, frequency
FROM colour_frequency
ORDER BY frequency DESC;
