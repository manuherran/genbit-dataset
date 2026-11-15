# -*- coding: utf-8 -*-
"""Example queries (portable: they run on MySQL 8+, MariaDB 10.2+ and SQLite 3.25+)."""

QUERIES = {
    "es": [
        {"title": "1. Todos los planetas habitables, del más cercano al más lejano",
         "sql": """SELECT nombre, sistema_estelar, distancia_al, gravedad_g, poblacion
FROM t_planeta
WHERE habitable = TRUE
ORDER BY distancia_al, nombre"""},
        {"title": "2. INNER JOIN: empleados que también son inversores",
         "sql": """SELECT e.nombre, e.apellidos, e.puesto, i.numero_acciones, em.siglas AS empresa
FROM t_empleado e
INNER JOIN t_inversor i ON i.id_empleado = e.id
INNER JOIN t_empresa em ON em.id = i.id_empresa
ORDER BY i.numero_acciones DESC"""},
        {"title": "3. LEFT JOIN: acciones de cada empleado (0 si no invierte)",
         "sql": """SELECT e.id, e.nombre, e.apellidos, COALESCE(SUM(i.numero_acciones), 0) AS acciones
FROM t_empleado e
LEFT JOIN t_inversor i ON i.id_empleado = e.id
GROUP BY e.id, e.nombre, e.apellidos
ORDER BY acciones DESC, e.id"""},
        {"title": "4. Relación reflexiva: cada empleado con su jefe",
         "sql": """SELECT emp.nombre AS empleado, emp.puesto, jef.nombre AS jefe
FROM t_empleado emp
LEFT JOIN t_empleado jef ON emp.id_jefe = jef.id
ORDER BY jef.id, emp.id"""},
        {"title": "5. Móviles sin asignar y empleados sin móvil",
         "sql": """SELECT m.numero, m.modelo, e.nombre AS empleado
FROM t_movil m
LEFT JOIN t_empleado e ON e.id = m.id_empleado
WHERE e.id IS NULL
UNION ALL
SELECT NULL, NULL, e.nombre
FROM t_empleado e
WHERE e.id NOT IN (SELECT id_empleado FROM t_movil WHERE id_empleado IS NOT NULL)"""},
        {"title": "6. Facturación por línea de producto",
         "sql": """SELECT l.nombre AS linea,
       COUNT(DISTINCT lp.id_pedido) AS pedidos,
       SUM(lp.cantidad) AS unidades,
       ROUND(SUM(lp.cantidad * lp.precio_unitario * (1 - lp.descuento_pct / 100.0)), 2) AS facturacion_cg
FROM t_linea_de_producto l
LEFT JOIN t_producto p ON p.id_linea = l.id
LEFT JOIN t_linea_de_pedido lp ON lp.id_producto = p.id
GROUP BY l.id, l.nombre
ORDER BY facturacion_cg DESC"""},
        {"title": "7. Top 5 clientes por importe pagado (neto de devoluciones)",
         "sql": """SELECT c.nombre, c.apellidos, c.especie, ROUND(SUM(pg.importe), 2) AS pagado_cg
FROM t_cliente c
JOIN t_pedido pe ON pe.id_cliente = c.id
JOIN t_pago pg ON pg.id_pedido = pe.id
GROUP BY c.id, c.nombre, c.apellidos, c.especie
ORDER BY pagado_cg DESC
LIMIT 5"""},
        {"title": "8. Pedidos entregados con deuda pendiente",
         "sql": """SELECT pe.id, pe.fecha_pedido, c.nombre AS cliente, t.total, COALESCE(pg.pagado, 0) AS pagado,
       ROUND(t.total - COALESCE(pg.pagado, 0), 2) AS pendiente
FROM t_pedido pe
JOIN t_cliente c ON c.id = pe.id_cliente
JOIN (SELECT id_pedido, ROUND(SUM(cantidad * precio_unitario * (1 - descuento_pct / 100.0)), 2) AS total
      FROM t_linea_de_pedido GROUP BY id_pedido) t ON t.id_pedido = pe.id
LEFT JOIN (SELECT id_pedido, SUM(importe) AS pagado FROM t_pago GROUP BY id_pedido) pg ON pg.id_pedido = pe.id
WHERE pe.estado = 'Entregado' AND t.total - COALESCE(pg.pagado, 0) > 0.01
ORDER BY pendiente DESC"""},
        {"title": "9. Productos que nunca se han vendido",
         "sql": """SELECT p.id, p.nombre, p.stock
FROM t_producto p
WHERE NOT EXISTS (SELECT 1 FROM t_linea_de_pedido lp WHERE lp.id_producto = p.id)"""},
        {"title": "10. Coste de fabricación vs. precio (margen) de cada producto",
         "sql": """SELECT p.nombre, p.precio, ROUND(SUM(pp.cantidad * pz.coste), 2) AS coste_piezas,
       ROUND(p.precio - SUM(pp.cantidad * pz.coste), 2) AS margen
FROM t_producto p
JOIN t_producto_pieza pp ON pp.id_producto = p.id
JOIN t_pieza pz ON pz.id = pp.id_pieza
GROUP BY p.id, p.nombre, p.precio
ORDER BY margen"""},
        {"title": "11. Proyectos con su responsable, nº de personas y horas semanales",
         "sql": """SELECT pr.nombre AS proyecto, pr.area, pr.estado, r.nombre AS responsable,
       COUNT(a.id_empleado) AS personas, COALESCE(SUM(a.horas_semana), 0) AS horas_semana
FROM t_proyecto pr
LEFT JOIN t_empleado r ON r.id = pr.id_responsable
LEFT JOIN t_asignacion a ON a.id_proyecto = pr.id
GROUP BY pr.id, pr.nombre, pr.area, pr.estado, r.nombre
ORDER BY horas_semana DESC"""},
        {"title": "12. Pacientes por proyecto y estado",
         "sql": """SELECT COALESCE(pr.nombre, '(sin proyecto)') AS proyecto, pa.estado, COUNT(*) AS pacientes
FROM t_paciente pa
LEFT JOIN t_proyecto pr ON pr.id = pa.id_proyecto
GROUP BY pr.nombre, pa.estado
ORDER BY proyecto, pacientes DESC"""},
        {"title": "13. Suscriptores que son empleados, clientes o ninguno (cruce por email)",
         "sql": """SELECT s.email, s.boletin,
       CASE WHEN e.id IS NOT NULL THEN 'Empleado'
            WHEN c.id IS NOT NULL THEN 'Cliente'
            ELSE 'Desconocido' END AS tipo
FROM t_suscriptor s
LEFT JOIN t_empleado e ON e.email = s.email
LEFT JOIN t_cliente c ON c.email = s.email
ORDER BY tipo, s.email"""},
        {"title": "14. Ventas mensuales y acumulado (funciones de ventana)",
         "sql": """SELECT mes, ventas_cg, ROUND(SUM(ventas_cg) OVER (ORDER BY mes), 2) AS acumulado_cg
FROM (
  SELECT SUBSTR(pe.fecha_pedido, 1, 7) AS mes,
         ROUND(SUM(lp.cantidad * lp.precio_unitario * (1 - lp.descuento_pct / 100.0)), 2) AS ventas_cg
  FROM t_pedido pe
  JOIN t_linea_de_pedido lp ON lp.id_pedido = pe.id
  WHERE pe.estado <> 'Cancelado'
  GROUP BY SUBSTR(pe.fecha_pedido, 1, 7)
) m
ORDER BY mes"""},
        {"title": "15. Ranking de vendedores por facturación",
         "sql": """SELECT COALESCE(e.nombre, '(web)') AS vendedor, COUNT(DISTINCT pe.id) AS pedidos,
       ROUND(SUM(lp.cantidad * lp.precio_unitario * (1 - lp.descuento_pct / 100.0)), 2) AS facturacion_cg,
       RANK() OVER (ORDER BY SUM(lp.cantidad * lp.precio_unitario * (1 - lp.descuento_pct / 100.0)) DESC) AS puesto
FROM t_pedido pe
JOIN t_linea_de_pedido lp ON lp.id_pedido = pe.id
LEFT JOIN t_empleado e ON e.id = pe.id_empleado
GROUP BY e.id, e.nombre"""},
    ],
    "en": [
        {"title": "1. All habitable planets, nearest first",
         "sql": """SELECT name, star_system, distance_ly, gravity_g, population
FROM t_planet
WHERE habitable = TRUE
ORDER BY distance_ly, name"""},
        {"title": "2. INNER JOIN: employees who are also investors",
         "sql": """SELECT e.first_name, e.last_name, e.job_title, i.shares, c.acronym AS company
FROM t_employee e
INNER JOIN t_investor i ON i.employee_id = e.id
INNER JOIN t_company c ON c.id = i.company_id
ORDER BY i.shares DESC"""},
        {"title": "3. LEFT JOIN: shares per employee (0 if not investing)",
         "sql": """SELECT e.id, e.first_name, e.last_name, COALESCE(SUM(i.shares), 0) AS shares
FROM t_employee e
LEFT JOIN t_investor i ON i.employee_id = e.id
GROUP BY e.id, e.first_name, e.last_name
ORDER BY shares DESC, e.id"""},
        {"title": "4. Self-join: every employee with their manager",
         "sql": """SELECT emp.first_name AS employee, emp.job_title, mgr.first_name AS manager
FROM t_employee emp
LEFT JOIN t_employee mgr ON emp.manager_id = mgr.id
ORDER BY mgr.id, emp.id"""},
        {"title": "5. Unassigned phones and employees without a phone",
         "sql": """SELECT m.number, m.model, e.first_name AS employee
FROM t_mobile m
LEFT JOIN t_employee e ON e.id = m.employee_id
WHERE e.id IS NULL
UNION ALL
SELECT NULL, NULL, e.first_name
FROM t_employee e
WHERE e.id NOT IN (SELECT employee_id FROM t_mobile WHERE employee_id IS NOT NULL)"""},
        {"title": "6. Revenue by product line",
         "sql": """SELECT l.name AS product_line,
       COUNT(DISTINCT ol.order_id) AS orders,
       SUM(ol.quantity) AS units,
       ROUND(SUM(ol.quantity * ol.unit_price * (1 - ol.discount_pct / 100.0)), 2) AS revenue_gc
FROM t_product_line l
LEFT JOIN t_product p ON p.product_line_id = l.id
LEFT JOIN t_order_line ol ON ol.product_id = p.id
GROUP BY l.id, l.name
ORDER BY revenue_gc DESC"""},
        {"title": "7. Top 5 customers by amount paid (net of refunds)",
         "sql": """SELECT c.first_name, c.last_name, c.species, ROUND(SUM(py.amount), 2) AS paid_gc
FROM t_customer c
JOIN t_order o ON o.customer_id = c.id
JOIN t_payment py ON py.order_id = o.id
GROUP BY c.id, c.first_name, c.last_name, c.species
ORDER BY paid_gc DESC
LIMIT 5"""},
        {"title": "8. Delivered orders with outstanding debt",
         "sql": """SELECT o.id, o.order_date, c.first_name AS customer, t.total, COALESCE(py.paid, 0) AS paid,
       ROUND(t.total - COALESCE(py.paid, 0), 2) AS outstanding
FROM t_order o
JOIN t_customer c ON c.id = o.customer_id
JOIN (SELECT order_id, ROUND(SUM(quantity * unit_price * (1 - discount_pct / 100.0)), 2) AS total
      FROM t_order_line GROUP BY order_id) t ON t.order_id = o.id
LEFT JOIN (SELECT order_id, SUM(amount) AS paid FROM t_payment GROUP BY order_id) py ON py.order_id = o.id
WHERE o.status = 'Delivered' AND t.total - COALESCE(py.paid, 0) > 0.01
ORDER BY outstanding DESC"""},
        {"title": "9. Products that have never been sold",
         "sql": """SELECT p.id, p.name, p.stock
FROM t_product p
WHERE NOT EXISTS (SELECT 1 FROM t_order_line ol WHERE ol.product_id = p.id)"""},
        {"title": "10. Manufacturing cost vs. price (margin) per product",
         "sql": """SELECT p.name, p.price, ROUND(SUM(pp.quantity * pc.cost), 2) AS parts_cost,
       ROUND(p.price - SUM(pp.quantity * pc.cost), 2) AS margin
FROM t_product p
JOIN t_product_piece pp ON pp.product_id = p.id
JOIN t_piece pc ON pc.id = pp.piece_id
GROUP BY p.id, p.name, p.price
ORDER BY margin"""},
        {"title": "11. Projects with lead, headcount and weekly hours",
         "sql": """SELECT pr.name AS project, pr.area, pr.status, l.first_name AS lead,
       COUNT(a.employee_id) AS people, COALESCE(SUM(a.weekly_hours), 0) AS weekly_hours
FROM t_project pr
LEFT JOIN t_employee l ON l.id = pr.lead_employee_id
LEFT JOIN t_assignment a ON a.project_id = pr.id
GROUP BY pr.id, pr.name, pr.area, pr.status, l.first_name
ORDER BY weekly_hours DESC"""},
        {"title": "12. Patients by project and status",
         "sql": """SELECT COALESCE(pr.name, '(no project)') AS project, pa.status, COUNT(*) AS patients
FROM t_patient pa
LEFT JOIN t_project pr ON pr.id = pa.project_id
GROUP BY pr.name, pa.status
ORDER BY project, patients DESC"""},
        {"title": "13. Subscribers who are employees, customers or neither (match by email)",
         "sql": """SELECT s.email, s.newsletter,
       CASE WHEN e.id IS NOT NULL THEN 'Employee'
            WHEN c.id IS NOT NULL THEN 'Customer'
            ELSE 'Unknown' END AS kind
FROM t_subscriber s
LEFT JOIN t_employee e ON e.email = s.email
LEFT JOIN t_customer c ON c.email = s.email
ORDER BY kind, s.email"""},
        {"title": "14. Monthly sales and running total (window functions)",
         "sql": """SELECT month, sales_gc, ROUND(SUM(sales_gc) OVER (ORDER BY month), 2) AS running_total_gc
FROM (
  SELECT SUBSTR(o.order_date, 1, 7) AS month,
         ROUND(SUM(ol.quantity * ol.unit_price * (1 - ol.discount_pct / 100.0)), 2) AS sales_gc
  FROM t_order o
  JOIN t_order_line ol ON ol.order_id = o.id
  WHERE o.status <> 'Cancelled'
  GROUP BY SUBSTR(o.order_date, 1, 7)
) m
ORDER BY month"""},
        {"title": "15. Sales rep ranking by revenue",
         "sql": """SELECT COALESCE(e.first_name, '(web)') AS sales_rep, COUNT(DISTINCT o.id) AS orders,
       ROUND(SUM(ol.quantity * ol.unit_price * (1 - ol.discount_pct / 100.0)), 2) AS revenue_gc,
       RANK() OVER (ORDER BY SUM(ol.quantity * ol.unit_price * (1 - ol.discount_pct / 100.0)) DESC) AS position
FROM t_order o
JOIN t_order_line ol ON ol.order_id = o.id
LEFT JOIN t_employee e ON e.id = o.employee_id
GROUP BY e.id, e.first_name"""},
    ],
}
