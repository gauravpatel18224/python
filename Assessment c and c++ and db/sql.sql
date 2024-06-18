SELECT 
    c.cust_name AS Customer_Name,
    c.city AS Customer_City,
    s.salesman_name AS Salesman,
    s.commission AS Commission
FROM 
    Customer c
JOIN 
    Salesman s
ON 
    c.salesman_id = s.salesman_id;
