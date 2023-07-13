-- script that creates a trigger that decreases the quantity
-- of an item after adding a new order.

DELIMITER $$ 
CREATE TRIGGER update_quantity
AFTER INSERT ON orders FOR EACH ROW 
BEGIN
    UPDATE items
    SET quantity = quantity - 1
    WHERE items.id = NEW.item_id;
END$$
