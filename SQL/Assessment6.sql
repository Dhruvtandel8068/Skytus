CREATE TABLE accounts1(
    account_id INT PRIMARY KEY,
    account_name VARCHAR(50),
    balance Decimal(10,2)
);

BEGIN TRANSACTION;

INSERT INTO accounts1 (account_id, account_name, balance)
VALUES (101, 'Dhruv', 10000);

ROLLBACK;

BEGIN TRANSACTION;

INSERT INTO accounts1 (account_id, account_name, balance)
VALUES (102, 'Tandel', 15000);

COMMIT;

BEGIN TRANSACTION;

-- Deduct from Dhruv
UPDATE accounts1
SET balance = balance - 5000
WHERE account_name = 'Dhruv';

-- Add to Tandel
UPDATE accounts1
SET balance = balance + 5000
WHERE account_name = 'Tandel';

COMMIT;

SELECT * FROM accounts1;