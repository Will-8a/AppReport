-------------------------------------------------------------------------
-- Create procedures
-------------------------------------------------------------------------
-- Create usuario_estudiante
delimiter $
create procedure create_usuario_estudiante(
    in ced varchar(20), in nom1 varchar(32), in nom2 varchar(32),
    in app varchar(32), in apm varchar(32), in e_mail varchar(45),
    in con char(105), in tu varchar(20), in id_t varchar(20),
    in car varchar(64), in can_r int, in horas_a decimal(10, 2)
)
begin
    insert into usuario values (ced, nom1, nom2, app, apm, e_mail, con, tu);
    insert into estudiante values(ced, id_t, car, can_r, horas_a);
    insert into tutor values (id_t, ced);
end$

-- Create usuario_tutor
delimiter $
create procedure create_usuario_tutor(
    in ced varchar(20), in nom1 varchar(32), in nom2 varchar(32),
    in app varchar(32), in apm varchar(32), in e_mail varchar(45),
    in con char(105), in tu varchar(20)
)
begin
    insert into usuario values (ced, nom1, nom2, app, apm, e_mail, con, tu);
end$

-------------------------------------------------------------------------
-- Read procedures
-------------------------------------------------------------------------
-- Read usuario_estudiante
delimiter $
create procedure read_usuario_estudiante(
    in ced varchar(20)
)
begin
    select usuario.cedula, usuario.nombre_1, usuario.nombre_2, usuario.apellido_p,
    usuario.apellido_m, usuario.email, usuario.contrasena, usuario.tipo_de_usuario,
    estudiante.id_tutor, estudiante.carrera, estudiante.cantidad_de_reportes,
    estudiante.horas_acumuladas
    from usuario
    inner join estudiante
    on usuario.cedula = estudiante.id_estudiante
    where usuario.cedula = ced;
end$

-- Read usuario_tutor
delimiter $
create procedure read_usuario_tutor(
    in ced varchar(20)
)
begin
    select * from usuario where cedula = ced;
end$

-------------------------------------------------------------------------
-- Update procedures
-------------------------------------------------------------------------
-- Update usuario_estudiante
delimiter $
create procedure update_usuario_estudiante(
    in ced varchar(20), in nom1 varchar(32), in nom2 varchar(32),
    in app varchar(32), in apm varchar(32),in e_mail varchar(45),
    in tu varchar(20), in id_t varchar(20), in car varchar(64)
)
begin
    update usuario set nombre_1 = nom1, nombre_2 = nom2,
    apellido_p = app, apellido_m = apm, email = e_mail,
    tipo_de_usuario = tu where cedula = ced;

    update estudiante set id_tutor = id_t, carrera = car
    where id_estudiante = ced;

    update tutor set id_tutor = id_t where id_estudiante = ced;
end$

-- Update usuario_tutor
delimiter $
create procedure update_usuario_tutor(
    in ced varchar(20), in nom1 varchar(32), in nom2 varchar(32),
    in app varchar(32), in apm varchar(32), in e_mail varchar(45),
    in tu varchar(20)
)
begin
    update usuario set nombre_1 = nom1, nombre_2 = nom2,
    apellido_p = app, apellido_m = apm, email = e_mail,
    tipo_de_usuario = tu where cedula = ced;
end$

-- Update estatus_reporte (administrador)
delimiter $
create procedure update_estatus_reporte_administrador(
    in id_r int, in estatus varchar(12)
)
begin
    update reportes_semanales set aprobacion_coordinador = estatus
    where id_reporte = id_r;
end$

-------------------------------------------------------------------------
-- Delete procedures
-------------------------------------------------------------------------
-- Delete usuario_estudiante
delimiter $
create procedure delete_usuario_estudiante(in ced varchar(20))
begin
    delete from usuario where cedula = ced;
    delete from estudiante where id_estudiante = ced;
    delete from tutor where id_estudiante = ced;
end$

-- Delete usuario_tutor
delimiter $
create procedure delete_usuario_tutor(in ced varchar(20))
begin
    delete from usuario where cedula = ced;
end$
