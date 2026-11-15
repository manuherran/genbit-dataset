-- =====================================================================
-- GenBit Dataset (ES) — base de datos relacional de ejemplo
-- Universo: GenBit, conglomerado científico del año 2188 (genética,
-- física cuántica, neurociencia, terraformación...).
-- Todos los datos son ficticios. Moneda: créditos galácticos (CG).
-- Licencia: CC BY 4.0 — https://github.com/manuherran/genbit-dataset
-- Generado automáticamente por generator/build.py .
-- =====================================================================

-- 1. Todos los planetas habitables, del más cercano al más lejano
SELECT nombre, sistema_estelar, distancia_al, gravedad_g, poblacion
FROM t_planeta
WHERE habitable = TRUE
ORDER BY distancia_al, nombre;

-- 2. INNER JOIN: empleados que también son inversores
SELECT e.nombre, e.apellidos, e.puesto, i.numero_acciones, em.siglas AS empresa
FROM t_empleado e
INNER JOIN t_inversor i ON i.id_empleado = e.id
INNER JOIN t_empresa em ON em.id = i.id_empresa
ORDER BY i.numero_acciones DESC;

-- 3. LEFT JOIN: acciones de cada empleado (0 si no invierte)
SELECT e.id, e.nombre, e.apellidos, COALESCE(SUM(i.numero_acciones), 0) AS acciones
FROM t_empleado e
LEFT JOIN t_inversor i ON i.id_empleado = e.id
GROUP BY e.id, e.nombre, e.apellidos
ORDER BY acciones DESC, e.id;

-- 4. Relación reflexiva: cada empleado con su jefe
SELECT emp.nombre AS empleado, emp.puesto, jef.nombre AS jefe
FROM t_empleado emp
LEFT JOIN t_empleado jef ON emp.id_jefe = jef.id
ORDER BY jef.id, emp.id;

-- 5. Móviles sin asignar y empleados sin móvil
SELECT m.numero, m.modelo, e.nombre AS empleado
FROM t_movil m
LEFT JOIN t_empleado e ON e.id = m.id_empleado
WHERE e.id IS NULL
UNION ALL
SELECT NULL, NULL, e.nombre
FROM t_empleado e
WHERE e.id NOT IN (SELECT id_empleado FROM t_movil WHERE id_empleado IS NOT NULL);

-- 6. Facturación por línea de producto
SELECT l.nombre AS linea,
       COUNT(DISTINCT lp.id_pedido) AS pedidos,
       SUM(lp.cantidad) AS unidades,
       ROUND(SUM(lp.cantidad * lp.precio_unitario * (1 - lp.descuento_pct / 100.0)), 2) AS facturacion_cg
FROM t_linea_de_producto l
LEFT JOIN t_producto p ON p.id_linea = l.id
LEFT JOIN t_linea_de_pedido lp ON lp.id_producto = p.id
GROUP BY l.id, l.nombre
ORDER BY facturacion_cg DESC;

-- 7. Top 5 clientes por importe pagado (neto de devoluciones)
SELECT c.nombre, c.apellidos, c.especie, ROUND(SUM(pg.importe), 2) AS pagado_cg
FROM t_cliente c
JOIN t_pedido pe ON pe.id_cliente = c.id
JOIN t_pago pg ON pg.id_pedido = pe.id
GROUP BY c.id, c.nombre, c.apellidos, c.especie
ORDER BY pagado_cg DESC
LIMIT 5;

-- 8. Pedidos entregados con deuda pendiente
SELECT pe.id, pe.fecha_pedido, c.nombre AS cliente, t.total, COALESCE(pg.pagado, 0) AS pagado,
       ROUND(t.total - COALESCE(pg.pagado, 0), 2) AS pendiente
FROM t_pedido pe
JOIN t_cliente c ON c.id = pe.id_cliente
JOIN (SELECT id_pedido, ROUND(SUM(cantidad * precio_unitario * (1 - descuento_pct / 100.0)), 2) AS total
      FROM t_linea_de_pedido GROUP BY id_pedido) t ON t.id_pedido = pe.id
LEFT JOIN (SELECT id_pedido, SUM(importe) AS pagado FROM t_pago GROUP BY id_pedido) pg ON pg.id_pedido = pe.id
WHERE pe.estado = 'Entregado' AND t.total - COALESCE(pg.pagado, 0) > 0.01
ORDER BY pendiente DESC;

-- 9. Productos que nunca se han vendido
SELECT p.id, p.nombre, p.stock
FROM t_producto p
WHERE NOT EXISTS (SELECT 1 FROM t_linea_de_pedido lp WHERE lp.id_producto = p.id);

-- 10. Coste de fabricación vs. precio (margen) de cada producto
SELECT p.nombre, p.precio, ROUND(SUM(pp.cantidad * pz.coste), 2) AS coste_piezas,
       ROUND(p.precio - SUM(pp.cantidad * pz.coste), 2) AS margen
FROM t_producto p
JOIN t_producto_pieza pp ON pp.id_producto = p.id
JOIN t_pieza pz ON pz.id = pp.id_pieza
GROUP BY p.id, p.nombre, p.precio
ORDER BY margen;

-- 11. Proyectos con su responsable, nº de personas y horas semanales
SELECT pr.nombre AS proyecto, pr.area, pr.estado, r.nombre AS responsable,
       COUNT(a.id_empleado) AS personas, COALESCE(SUM(a.horas_semana), 0) AS horas_semana
FROM t_proyecto pr
LEFT JOIN t_empleado r ON r.id = pr.id_responsable
LEFT JOIN t_asignacion a ON a.id_proyecto = pr.id
GROUP BY pr.id, pr.nombre, pr.area, pr.estado, r.nombre
ORDER BY horas_semana DESC;

-- 12. Pacientes por proyecto y estado
SELECT COALESCE(pr.nombre, '(sin proyecto)') AS proyecto, pa.estado, COUNT(*) AS pacientes
FROM t_paciente pa
LEFT JOIN t_proyecto pr ON pr.id = pa.id_proyecto
GROUP BY pr.nombre, pa.estado
ORDER BY proyecto, pacientes DESC;

-- 13. Suscriptores que son empleados, clientes o ninguno (cruce por email)
SELECT s.email, s.boletin,
       CASE WHEN e.id IS NOT NULL THEN 'Empleado'
            WHEN c.id IS NOT NULL THEN 'Cliente'
            ELSE 'Desconocido' END AS tipo
FROM t_suscriptor s
LEFT JOIN t_empleado e ON e.email = s.email
LEFT JOIN t_cliente c ON c.email = s.email
ORDER BY tipo, s.email;

-- 14. Ventas mensuales y acumulado (funciones de ventana)
SELECT mes, ventas_cg, ROUND(SUM(ventas_cg) OVER (ORDER BY mes), 2) AS acumulado_cg
FROM (
  SELECT SUBSTR(pe.fecha_pedido, 1, 7) AS mes,
         ROUND(SUM(lp.cantidad * lp.precio_unitario * (1 - lp.descuento_pct / 100.0)), 2) AS ventas_cg
  FROM t_pedido pe
  JOIN t_linea_de_pedido lp ON lp.id_pedido = pe.id
  WHERE pe.estado <> 'Cancelado'
  GROUP BY SUBSTR(pe.fecha_pedido, 1, 7)
) m
ORDER BY mes;

-- 15. Ranking de vendedores por facturación
SELECT COALESCE(e.nombre, '(web)') AS vendedor, COUNT(DISTINCT pe.id) AS pedidos,
       ROUND(SUM(lp.cantidad * lp.precio_unitario * (1 - lp.descuento_pct / 100.0)), 2) AS facturacion_cg,
       RANK() OVER (ORDER BY SUM(lp.cantidad * lp.precio_unitario * (1 - lp.descuento_pct / 100.0)) DESC) AS puesto
FROM t_pedido pe
JOIN t_linea_de_pedido lp ON lp.id_pedido = pe.id
LEFT JOIN t_empleado e ON e.id = pe.id_empleado
GROUP BY e.id, e.nombre;

