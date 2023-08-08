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
