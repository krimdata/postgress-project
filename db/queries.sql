SELECT 
    customers.name AS customer_name,
    COUNT(orders.id) AS order_count,
    AVG(orders.quantity * products.price) AS average_order_value
FROM orders
JOIN customers ON orders.customer_id = customers.id
JOIN products ON orders.product_id = products.id
GROUP BY customers.id;
