-- Sentencias de busqueda y consultas en SQL

select * from customer -- Seleccionar todo de una tabla

select first_name as primer_nombre from customer -- darle nombre a las tablas con as

select * from customer where first_name='Jamie' and last_name='Rice'
-- tambien podemos usar or, in o tambien not, depende de lo que necesitamos.

--Estructura de como se busca
select 	
	* 
from 
	customer as c  
where 
	first_name in ('Ann','Jamie','Anne') -- otra forma de buscar
	
select 	
	* 
from 
	customer as c  
where 
	first_name like ('An%') -- like es para buscar que tenga eso que pongo
-- por ejemplo ('An%') me muestra todos los nombres que empiezen por An
-- y tenga lo que sea despues de An...
-- tambien puede ser al final ('%An') o por los dos lados ('%An%')

-- Seleccionar los nombres que tengas entre 3 y 5 caracteres
select 
	first_name,
	length(first_name) as nombre_longitud -- te dice que longitud tiene algo
from 
	customer
where 
	first_name like ('A%')
	and length(first_name) between 3 and 5 -- entre cuanto y cuanto
	order by nombre_longitud -- ordena de menor a mayor
	limit 7 -- traigame 7 nada más

-- si quiero saber cuantos son en total
select count(*)   -- me cuenta cuantos cumplen, es una consulta dentro de otra
from(             -- me cuenta cuantos cumplen, es una consulta dentro de otra
select 
	first_name,
	length(first_name) as nombre_longitud -- te dice que longitud tiene algo
from 
	customer
where 
	first_name like ('A%')
	and length(first_name) between 3 and 5 -- entre cuanto y cuanto
	order by nombre_longitud -- ordena de menor a mayor
	--limit 7 -- traigame 7 nada más
	) as cumple
	
-- otra forma que consume menos recursos CTE
with cumple as (           -- me cuenta cuantos cumplen, es una consulta dentro de otra
select 
	first_name,
	length(first_name) as nombre_longitud -- te dice que longitud tiene algo
from 
	customer
where 
	first_name like ('A%')
	and length(first_name) between 3 and 5 -- entre cuanto y cuanto
	order by nombre_longitud -- ordena de menor a mayor
	) select count(*) from cumple -- select count(*) te cuenta los resultados
	
-- JOINS  (left, Inner y Right)
-- Caso inner join (solo muestra lo que cumple la condición)
select 
	customer.customer_id,
	customer.first_name,
	customer.last_name,
	payment.amount,
	payment.payment_date
from 
	customer  -- porque saco mas columnas de este que del otro
inner join
	payment  -- del que saco menos columnas
on 
	customer.customer_id = payment.customer_id -- intercepto que coinciden
order by
	payment.payment_date desc

-- Left Join (Muestro lo que cumple la condición más lo que está en From o en el de la izquierda)
select 
	film.film_id, -- left (inicio)
	film.title, -- left (inicio)
	inventory.inventory_id 
from
	film -- porque inicio con esas columnas
left join 
	inventory -- fianlizo con estos 
on
	film.film_id = inventory.film_id 


-- Left Join (Muestro lo que cumple la condición más lo que está en Rigth Joing o en el de la derecha)
select 
	film.film_id, -- left (inicio)
	film.title, -- left (inicio)
	inventory.inventory_id 
from
	film -- porque inicio con esas columnas
right join 
	inventory -- fianlizo con estos 
on
	film.film_id = inventory.film_id
