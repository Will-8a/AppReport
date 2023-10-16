-------------------------------------------------------------------------
-- Read procedures
-------------------------------------------------------------------------
-- Read usuario
delimiter $
create procedure read_usuario(in ced varchar(20))
begin
    select * from usuario where cedula = ced;
end$

-- Read usuario except contrasena
delimiter $
create procedure read_usuario_except_password(in ced varchar(20))
begin
    select cedula, nombre_1, nombre_2, apellido_p, apellido_m, email,
    tipo_de_usuario from usuario where cedula = ced;
end$

-- Read reportes_estudiante_especifico
delimiter $
create procedure read_reportes_estudiante_especifico(
    in id_e varchar(20)
)
begin
    select * from reportes_semanales
    where id_estudiante = id_e;
end$

-- Read reporte_especifico
create procedure read_reporte_especifico(
    in id_e varchar(20), in num_rep int
)
begin
    select * from reportes_semanales
    where id_estudiante = id_e
    and numero_reporte = num_rep;
end$
